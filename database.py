# ============================================================
#  database.py  —  Работа с SQLite через aiosqlite
# ============================================================

import json
import aiosqlite

DB_PATH = "bot.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                phrase_id INTEGER NOT NULL,
                is_correct INTEGER NOT NULL,
                answered_at TEXT DEFAULT (datetime('now'))
            )
        """)
        await db.commit()


async def ensure_user(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )
        await db.commit()


async def get_all_users() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id FROM users") as cursor:
            rows = await cursor.fetchall()
    return [row[0] for row in rows]


async def record_answer(user_id: int, phrase_id: int, is_correct: bool):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO answers (user_id, phrase_id, is_correct) VALUES (?, ?, ?)",
            (user_id, phrase_id, int(is_correct))
        )
        await db.commit()


async def get_user_stats(user_id: int) -> dict:
    """
    Возвращает словарь вида:
    { "1": {"correct": 3, "total": 5}, "2": {...}, ... }
    """
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            """
            SELECT phrase_id,
                   SUM(is_correct)   AS correct,
                   COUNT(*)          AS total
            FROM answers
            WHERE user_id = ?
            GROUP BY phrase_id
            """,
            (user_id,)
        ) as cursor:
            rows = await cursor.fetchall()

    return {
        str(row[0]): {"correct": row[1], "total": row[2]}
        for row in rows
    }
