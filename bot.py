# ============================================================
#  bot.py  —  Telegram-бот "50 фраз native speakers"
#  Стек: Python 3.10+ | aiogram 3.x | SQLite | APScheduler
#  Установка: pip install aiogram apscheduler aiosqlite
# ============================================================

import asyncio
import logging
import random
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import database as db
from phrases import PHRASES, PUSH_TEMPLATE
from config import BOT_TOKEN, PUSH_HOUR, PUSH_MINUTE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# ─── FSM States ────────────────────────────────────────────
class Training(StatesGroup):
    in_session = State()


# ─── Keyboards ─────────────────────────────────────────────
def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎯 Тренироваться")],
            [KeyboardButton(text="📊 Мой прогресс"), KeyboardButton(text="🔁 Повторить слабые")],
            [KeyboardButton(text="📖 Все фразы"), KeyboardButton(text="ℹ️ Помощь")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери действие..."
    )


def answer_kb(options: list[str], phrase_id: int, task_type: str) -> InlineKeyboardMarkup:
    """4 кнопки-варианта ответа."""
    buttons = [
        [InlineKeyboardButton(
            text=opt,
            callback_data=f"ans:{phrase_id}:{task_type}:{i}"
        )]
        for i, opt in enumerate(options)
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def next_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ Следующее задание", callback_data="next")],
        [InlineKeyboardButton(text="🏁 Завершить", callback_data="finish")]
    ])


def session_result_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Ещё раз", callback_data="start_session")],
        [InlineKeyboardButton(text="🔁 Повторить слабые", callback_data="start_weak")]
    ])


# ─── Helpers ───────────────────────────────────────────────
TASK_LABELS = {
    "type_1": "🗨 Мини-диалог",
    "type_2": "🎬 Из фильма",
    "type_3": "❓ Что значит?",
    "type_4": "🔤 Перевод",
}

TASK_TYPES = ["type_1", "type_2", "type_3", "type_4"]


def build_question_text(phrase: dict, task_type: str, num: int, total: int) -> str:
    task = phrase[task_type]
    label = TASK_LABELS[task_type]
    lines = [
        f"<b>Задание {num}/{total}</b> · {label}",
        f"📌 Фраза: <b>{phrase['phrase']}</b>",
        "",
    ]
    if task_type == "type_2":
        lines.append(f"🎬 <i>{task['scene']}</i>")
        lines.append("")
        lines.append("Что сказал герой?")
    else:
        lines.append(task["question"])
    return "\n".join(lines)


def get_session_phrases(user_stats: dict, mode: str = "random") -> list[dict]:
    """
    Возвращает список фраз для сессии (10 штук).
    mode='random'  — случайные из всех 50
    mode='weak'    — фразы с низким % правильных ответов
    """
    if mode == "weak":
        # Сортируем по accuracy (меньше — хуже)
        scored = []
        for p in PHRASES:
            pid = str(p["id"])
            stats = user_stats.get(pid, {"correct": 0, "total": 0})
            if stats["total"] > 0:
                acc = stats["correct"] / stats["total"]
            else:
                acc = 0.0
            scored.append((acc, p))
        scored.sort(key=lambda x: x[0])
        # Берём 10 худших (или меньше если фраз мало)
        return [p for _, p in scored[:10]]
    else:
        return random.sample(PHRASES, min(10, len(PHRASES)))


# ─── /start ────────────────────────────────────────────────
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await db.ensure_user(message.from_user.id)
    name = message.from_user.first_name or "друг"
    await message.answer(
        f"👋 Привет, {name}!\n\n"
        "Я помогу тебе выучить <b>50 фраз</b>, которые используют носители английского.\n\n"
        "🎯 Каждая сессия — 10 случайных фраз, 4 типа заданий.\n"
        "🔁 Когда пройдёшь все 50 — включится режим повторения слабых мест.\n"
        "🔔 Каждый день буду присылать фразу дня.\n\n"
        "Поехали?",
        reply_markup=main_menu_kb(),
        parse_mode="HTML"
    )


# ─── Помощь ────────────────────────────────────────────────
@dp.message(F.text == "ℹ️ Помощь")
async def cmd_help(message: Message):
    await message.answer(
        "<b>Как пользоваться ботом:</b>\n\n"
        "🎯 <b>Тренироваться</b> — 10 случайных фраз, 4 типа заданий\n"
        "🔁 <b>Повторить слабые</b> — фразы, в которых ты чаще ошибаешься\n"
        "📊 <b>Мой прогресс</b> — статистика по всем фразам\n"
        "📖 <b>Все фразы</b> — список всех 50 выражений с переводом\n\n"
        "<b>Типы заданий:</b>\n"
        "🗨 Мини-диалог — выбери подходящую фразу\n"
        "🎬 Из фильма — что сказал герой?\n"
        "❓ Что значит — выбери правильное значение\n"
        "🔤 Перевод — как переводится фраза?\n",
        parse_mode="HTML"
    )


# ─── Все фразы ─────────────────────────────────────────────
@dp.message(F.text == "📖 Все фразы")
async def cmd_all_phrases(message: Message):
    lines = ["<b>50 фраз носителей английского:</b>\n"]
    for p in PHRASES:
        lines.append(f"{p['id']}. <b>{p['phrase']}</b> — {p['translation']}")
    # Telegram ограничивает 4096 символов — шлём двумя сообщениями
    text = "\n".join(lines)
    if len(text) > 4000:
        mid = len(PHRASES) // 2
        part1 = "<b>50 фраз (1–25):</b>\n\n" + "\n".join(lines[1:mid+1])
        part2 = "<b>50 фраз (26–50):</b>\n\n" + "\n".join(lines[mid+1:])
        await message.answer(part1, parse_mode="HTML")
        await message.answer(part2, parse_mode="HTML")
    else:
        await message.answer(text, parse_mode="HTML")


# ─── Прогресс ──────────────────────────────────────────────
@dp.message(F.text == "📊 Мой прогресс")
async def cmd_progress(message: Message):
    user_id = message.from_user.id
    stats = await db.get_user_stats(user_id)
    total_correct = sum(s["correct"] for s in stats.values())
    total_attempts = sum(s["total"] for s in stats.values())
    phrases_seen = sum(1 for s in stats.values() if s["total"] > 0)

    if total_attempts == 0:
        await message.answer(
            "📊 Ты ещё не начал тренировки.\nНажми <b>🎯 Тренироваться</b>!",
            parse_mode="HTML"
        )
        return

    accuracy = round(total_correct / total_attempts * 100)
    bar_filled = accuracy // 10
    bar = "🟩" * bar_filled + "⬜" * (10 - bar_filled)

    # Топ-5 слабых фраз
    weak = sorted(
        [(pid, s) for pid, s in stats.items() if s["total"] > 0],
        key=lambda x: x[1]["correct"] / x[1]["total"]
    )[:5]

    weak_lines = []
    phrase_map = {str(p["id"]): p["phrase"] for p in PHRASES}
    for pid, s in weak:
        acc = round(s["correct"] / s["total"] * 100)
        weak_lines.append(f"  • {phrase_map.get(pid, pid)} — {acc}%")

    text = (
        f"📊 <b>Твой прогресс</b>\n\n"
        f"Фраз изучено: <b>{phrases_seen}/50</b>\n"
        f"Правильных ответов: <b>{total_correct}/{total_attempts}</b>\n"
        f"Точность: <b>{accuracy}%</b>\n"
        f"{bar}\n"
    )
    if weak_lines:
        text += "\n🔴 <b>Слабые места:</b>\n" + "\n".join(weak_lines)

    await message.answer(text, parse_mode="HTML")


# ─── Старт сессии ──────────────────────────────────────────
async def start_training_session(message_or_cq, state: FSMContext, mode: str = "random"):
    """Общая функция запуска сессии (из кнопки или callback)."""
    if isinstance(message_or_cq, CallbackQuery):
        user_id = message_or_cq.from_user.id
        send = message_or_cq.message.answer
    else:
        user_id = message_or_cq.from_user.id
        send = message_or_cq.answer

    user_stats = await db.get_user_stats(user_id)
    phrases = get_session_phrases(user_stats, mode=mode)

    # Для каждой фразы выбираем случайный тип задания
    queue = [(p, random.choice(TASK_TYPES)) for p in phrases]

    await state.set_state(Training.in_session)
    await state.update_data(
        queue=[(p["id"], t) for p, t in queue],
        current=0,
        correct=0,
        total=len(queue),
        answered=False
    )

    mode_label = "🔁 Повторение слабых мест" if mode == "weak" else "🎯 Новая тренировка"
    await send(
        f"<b>{mode_label}</b>\n"
        f"Будет {len(queue)} заданий. Удачи!\n\n"
        f"Начинаем ▶️",
        parse_mode="HTML"
    )
    await send_next_question(send, state, user_id)


@dp.message(F.text == "🎯 Тренироваться")
async def btn_train(message: Message, state: FSMContext):
    await start_training_session(message, state, mode="random")


@dp.message(F.text == "🔁 Повторить слабые")
async def btn_weak(message: Message, state: FSMContext):
    user_stats = await db.get_user_stats(message.from_user.id)
    has_weak = any(s["total"] > 0 for s in user_stats.values())
    if not has_weak:
        await message.answer(
            "Сначала пройди хотя бы одну тренировку — тогда я смогу найти твои слабые места 😊",
            reply_markup=main_menu_kb()
        )
        return
    await start_training_session(message, state, mode="weak")


@dp.callback_query(F.data == "start_session")
async def cb_start_session(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    await start_training_session(cq, state, mode="random")


@dp.callback_query(F.data == "start_weak")
async def cb_start_weak(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    await start_training_session(cq, state, mode="weak")


# ─── Отправка вопроса ──────────────────────────────────────
async def send_next_question(send_fn, state: FSMContext, user_id: int):
    data = await state.get_data()
    queue = data["queue"]
    current = data["current"]

    if current >= len(queue):
        await finish_session(send_fn, state)
        return

    phrase_id, task_type = queue[current]
    phrase = next(p for p in PHRASES if p["id"] == phrase_id)
    task = phrase[task_type]

    # Перемешиваем варианты ответа
    options = task["options"][:]
    random.shuffle(options)

    text = build_question_text(phrase, task_type, current + 1, data["total"])
    kb = answer_kb(options, phrase_id, task_type)

    await send_fn(text, reply_markup=kb, parse_mode="HTML")
    await state.update_data(shuffled_options=options, answered=False)


# ─── Обработка ответа ──────────────────────────────────────
@dp.callback_query(F.data.startswith("ans:"), Training.in_session)
async def cb_answer(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    data = await state.get_data()

    if data.get("answered"):
        return  # Игнорируем повторный клик

    _, phrase_id_str, task_type, option_idx_str = cq.data.split(":")
    phrase_id = int(phrase_id_str)
    option_idx = int(option_idx_str)

    phrase = next(p for p in PHRASES if p["id"] == phrase_id)
    task = phrase[task_type]
    correct_answer = task["answer"]

    shuffled = data["shuffled_options"]
    chosen = shuffled[option_idx]
    is_correct = (chosen == correct_answer)

    # Сохраняем результат в БД
    await db.record_answer(cq.from_user.id, phrase_id, is_correct)

    correct_count = data["correct"] + (1 if is_correct else 0)
    await state.update_data(
        correct=correct_count,
        answered=True
    )

    if is_correct:
        result_text = (
            f"✅ <b>Правильно!</b>\n\n"
            f"<b>{phrase['phrase']}</b> — {phrase['translation']}\n"
            f"📝 <i>{phrase['example']}</i>"
        )
    else:
        result_text = (
            f"❌ <b>Неверно.</b> Правильный ответ:\n\n"
            f"<b>{correct_answer}</b>\n\n"
            f"<b>{phrase['phrase']}</b> — {phrase['translation']}\n"
            f"📝 <i>{phrase['example']}</i>"
        )

    await cq.message.edit_reply_markup(reply_markup=None)
    await cq.message.answer(result_text, reply_markup=next_kb(), parse_mode="HTML")


@dp.callback_query(F.data == "next", Training.in_session)
async def cb_next(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    data = await state.get_data()
    await state.update_data(current=data["current"] + 1, answered=False)
    await send_next_question(cq.message.answer, state, cq.from_user.id)


@dp.callback_query(F.data == "finish", Training.in_session)
async def cb_finish(cq: CallbackQuery, state: FSMContext):
    await cq.answer()
    await finish_session(cq.message.answer, state)


# ─── Итог сессии ───────────────────────────────────────────
async def finish_session(send_fn, state: FSMContext):
    data = await state.get_data()
    correct = data["correct"]
    total = data["total"]
    answered = data["current"]  # сколько реально ответил

    if answered == 0:
        await state.clear()
        await send_fn("Сессия завершена. До следующего раза! 👋", reply_markup=main_menu_kb())
        return

    accuracy = round(correct / answered * 100)

    if accuracy >= 80:
        emoji, comment = "🏆", "Отлично! Ты прекрасно знаешь эти фразы."
    elif accuracy >= 60:
        emoji, comment = "👍", "Хороший результат! Немного практики — и будет идеально."
    else:
        emoji, comment = "💪", "Есть куда расти. Попробуй повторить слабые места!"

    text = (
        f"{emoji} <b>Сессия завершена!</b>\n\n"
        f"Правильных ответов: <b>{correct}/{answered}</b>\n"
        f"Точность: <b>{accuracy}%</b>\n\n"
        f"{comment}"
    )

    await state.clear()
    await send_fn(text, reply_markup=session_result_kb(), parse_mode="HTML")


# ─── Push уведомления ──────────────────────────────────────
async def send_daily_push():
    """Ежедневная рассылка фразы дня всем пользователям."""
    users = await db.get_all_users()
    day_index = datetime.now().timetuple().tm_yday % len(PHRASES)
    phrase = PHRASES[day_index]

    text = PUSH_TEMPLATE.format(
        phrase=phrase["phrase"],
        translation=phrase["translation"],
        example=phrase["example"]
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎯 Потренироваться", callback_data="start_session")]
    ])

    sent, failed = 0, 0
    for user_id in users:
        try:
            await bot.send_message(user_id, text, reply_markup=kb, parse_mode="HTML")
            sent += 1
        except Exception as e:
            logger.warning(f"Push failed for {user_id}: {e}")
            failed += 1

    logger.info(f"Daily push sent: {sent} ok, {failed} failed")


# ─── Запуск ────────────────────────────────────────────────
async def main():
    await db.init_db()

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        send_daily_push,
        trigger="cron",
        hour=PUSH_HOUR,
        minute=PUSH_MINUTE
    )
    scheduler.start()

    logger.info("Bot started")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
