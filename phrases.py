# ============================================================
#  phrases.py  —  Контент для TG-бота "50 фраз native speakers"
#  Уровень: A1-A2 | Язык интерфейса: Русский
#  Типы заданий:
#    type_1  — Мини-диалог: выбери подходящую фразу
#    type_2  — Из фильма/сериала: что сказал герой?
#    type_3  — Что значит фраза? (выбери значение)
#    type_4  — Как переводится? (выбери перевод на русский)
# ============================================================

PHRASES = [

    {
        "id": 1,
        "phrase": "I'm down",
        "translation": "Я за / Я согласен",
        "meaning": "Согласие, готовность что-то сделать",
        "example": "Do you want to grab a coffee? — I'm down!",

        "type_1": {
            "question": "Друг пишет: «Hey, wanna watch a movie tonight?» Что ты ответишь, если согласен?",
            "options": ["I'm down!", "I'm out.", "No way.", "I'm fine."],
            "answer": "I'm down!"
        },
        "type_2": {
            "scene": "Сериал «Friends». Росс предлагает пойти в пиццерию. Джо сразу соглашается:",
            "options": ["I'm down!", "Whatever.", "I guess not.", "Take care."],
            "answer": "I'm down!"
        },
        "type_3": {
            "question": "Что значит «I'm down»?",
            "options": ["Мне грустно", "Я согласен / Я за", "Я устал", "Мне всё равно"],
            "answer": "Я согласен / Я за"
        },
        "type_4": {
            "question": "Как перевести «I'm down»?",
            "options": ["Я вниз", "Я за / согласен", "Мне плохо", "Я упал"],
            "answer": "Я за / согласен"
        }
    },

    {
        "id": 2,
        "phrase": "Sounds good",
        "translation": "Звучит хорошо / Окей",
        "meaning": "Выражение согласия или одобрения",
        "example": "Let's meet at 6. — Sounds good!",

        "type_1": {
            "question": "Коллега говорит: «Let's finish the report by Friday.» Ты согласен. Что скажешь?",
            "options": ["Sounds good!", "No big deal.", "Fair enough.", "We'll see."],
            "answer": "Sounds good!"
        },
        "type_2": {
            "scene": "Сериал «The Office». Майкл предлагает план на встрече, и Джим коротко соглашается:",
            "options": ["Sounds good!", "Not really.", "I don't think so.", "Hold on."],
            "answer": "Sounds good!"
        },
        "type_3": {
            "question": "Что значит «Sounds good»?",
            "options": ["Громко звучит", "Хорошая музыка", "Окей, согласен", "Это странно"],
            "answer": "Окей, согласен"
        },
        "type_4": {
            "question": "Как перевести «Sounds good»?",
            "options": ["Звук хороший", "Звучит хорошо / Договорились", "Это странно", "Не очень"],
            "answer": "Звучит хорошо / Договорились"
        }
    },

    {
        "id": 3,
        "phrase": "Works for me",
        "translation": "Меня устраивает / Мне подходит",
        "meaning": "Подходящий вариант, всё ок",
        "example": "Can we meet at 3pm? — Works for me!",

        "type_1": {
            "question": "Друг предлагает встретиться в субботу в 2. Тебе удобно. Что скажешь?",
            "options": ["Works for me!", "I'm not sure.", "Deal.", "No way."],
            "answer": "Works for me!"
        },
        "type_2": {
            "scene": "Сериал «Brooklyn Nine-Nine». Капитан предлагает новый график дежурств — Эми сразу соглашается:",
            "options": ["Works for me!", "I mean...", "Sort of.", "That sucks."],
            "answer": "Works for me!"
        },
        "type_3": {
            "question": "Что значит «Works for me»?",
            "options": ["Я работаю", "Меня устраивает", "Это не работает", "Работай со мной"],
            "answer": "Меня устраивает"
        },
        "type_4": {
            "question": "Как перевести «Works for me»?",
            "options": ["Работает на меня", "Меня устраивает / Подходит", "Я за работу", "Это сложно"],
            "answer": "Меня устраивает / Подходит"
        }
    },

    {
        "id": 4,
        "phrase": "Fair enough",
        "translation": "Справедливо / Ладно, понял",
        "meaning": "Признание чужого аргумента как разумного",
        "example": "I didn't call because I was busy. — Fair enough.",

        "type_1": {
            "question": "Друг объясняет: «I was late because my bus didn't come.» Ты понимаешь его. Что скажешь?",
            "options": ["Fair enough.", "That sucks.", "No way.", "Go for it."],
            "answer": "Fair enough."
        },
        "type_2": {
            "scene": "Фильм «The Devil Wears Prada». Персонаж объясняет правила — другой герой принимает их без споров:",
            "options": ["Fair enough.", "I'm down.", "Lucky you.", "Deal."],
            "answer": "Fair enough."
        },
        "type_3": {
            "question": "Что значит «Fair enough»?",
            "options": ["Очень красиво", "Хватит уже", "Ладно, понял / справедливо", "Мне всё равно"],
            "answer": "Ладно, понял / справедливо"
        },
        "type_4": {
            "question": "Как перевести «Fair enough»?",
            "options": ["Достаточно честно", "Справедливо / Ладно, понял", "Немного", "Всё в порядке"],
            "answer": "Справедливо / Ладно, понял"
        }
    },

    {
        "id": 5,
        "phrase": "That makes sense",
        "translation": "Это логично / Понятно",
        "meaning": "Подтверждение, что объяснение понятно и логично",
        "example": "She left early because she had a flight. — That makes sense.",

        "type_1": {
            "question": "Коллега объясняет: «We changed the plan because the client asked for it.» Ты понял. Что скажешь?",
            "options": ["That makes sense.", "No worries.", "I'm not sure.", "Hold on."],
            "answer": "That makes sense."
        },
        "type_2": {
            "scene": "Сериал «Sherlock». Ватсон слушает объяснение Шерлока и соглашается, что всё логично:",
            "options": ["That makes sense.", "Why not?", "I mean...", "We'll see."],
            "answer": "That makes sense."
        },
        "type_3": {
            "question": "Что значит «That makes sense»?",
            "options": ["Это странно", "Это логично / понятно", "Это не важно", "Так не бывает"],
            "answer": "Это логично / понятно"
        },
        "type_4": {
            "question": "Как перевести «That makes sense»?",
            "options": ["Это делает смысл", "Это логично / Понятно", "Это не имеет значения", "Не понял"],
            "answer": "Это логично / Понятно"
        }
    },

    {
        "id": 6,
        "phrase": "No worries",
        "translation": "Не беспокойся / Всё ок",
        "meaning": "Успокоение или ответ на извинение",
        "example": "Sorry I'm late! — No worries, we just started.",

        "type_1": {
            "question": "Друг написал: «Sorry, I forgot to reply!» Ты не злишься. Что скажешь?",
            "options": ["No worries!", "That sucks.", "My bad.", "Go for it."],
            "answer": "No worries!"
        },
        "type_2": {
            "scene": "Сериал «Ted Lasso». Игрок извиняется за ошибку — тренер отвечает спокойно и дружелюбно:",
            "options": ["No worries!", "I'm not gonna lie.", "Deal.", "Sort of."],
            "answer": "No worries!"
        },
        "type_3": {
            "question": "Что значит «No worries»?",
            "options": ["Много проблем", "Не беспокойся / Всё ок", "Нет ничего", "Плохие новости"],
            "answer": "Не беспокойся / Всё ок"
        },
        "type_4": {
            "question": "Как перевести «No worries»?",
            "options": ["Нет забот", "Не беспокойся / Всё ок", "Без проблем с работой", "Скучно"],
            "answer": "Не беспокойся / Всё ок"
        }
    },

    {
        "id": 7,
        "phrase": "No problem",
        "translation": "Не проблема / Пожалуйста",
        "meaning": "Ответ на просьбу или благодарность",
        "example": "Thanks for helping me! — No problem at all.",

        "type_1": {
            "question": "Ты помог другу с переездом. Он говорит: «Thank you so much!» Что ответишь?",
            "options": ["No problem!", "I'm down.", "That sucks.", "We'll see."],
            "answer": "No problem!"
        },
        "type_2": {
            "scene": "Фильм «Home Alone». Продавец помогает мальчику — и спокойно отвечает на его «thank you»:",
            "options": ["No problem!", "I guess.", "Hold on.", "Why not?"],
            "answer": "No problem!"
        },
        "type_3": {
            "question": "Что значит «No problem»?",
            "options": ["Есть проблема", "Не проблема / Пожалуйста", "Нет ответа", "Всё плохо"],
            "answer": "Не проблема / Пожалуйста"
        },
        "type_4": {
            "question": "Как перевести «No problem»?",
            "options": ["Нет задачи", "Не проблема / Пожалуйста", "Без работы", "Никак"],
            "answer": "Не проблема / Пожалуйста"
        }
    },

    {
        "id": 8,
        "phrase": "No big deal",
        "translation": "Ничего страшного / Не важно",
        "meaning": "Преуменьшение значимости ситуации",
        "example": "I spilled coffee on the table. — No big deal, I'll clean it up.",

        "type_1": {
            "question": "Друг расстроен, что опоздал на 5 минут. Ты хочешь его успокоить. Что скажешь?",
            "options": ["No big deal!", "That sucks.", "My bad.", "I'm not sure."],
            "answer": "No big deal!"
        },
        "type_2": {
            "scene": "Сериал «Modern Family». Кто-то сломал небольшую вещь — хозяин машет рукой и успокаивает:",
            "options": ["No big deal!", "Fair enough.", "I'm down.", "Keep me posted."],
            "answer": "No big deal!"
        },
        "type_3": {
            "question": "Что значит «No big deal»?",
            "options": ["Очень важно", "Ничего страшного", "Плохая сделка", "Очень дорого"],
            "answer": "Ничего страшного"
        },
        "type_4": {
            "question": "Как перевести «No big deal»?",
            "options": ["Не большое дело / Ничего страшного", "Большая сделка", "Нет дела", "Неважно что"],
            "answer": "Не большое дело / Ничего страшного"
        }
    },

    {
        "id": 9,
        "phrase": "My bad",
        "translation": "Моя вина / Извини",
        "meaning": "Неформальное признание своей ошибки",
        "example": "You sent the wrong file. — Oh, my bad! I'll fix it now.",

        "type_1": {
            "question": "Ты случайно взял чужую кружку. Что скажешь?",
            "options": ["My bad!", "No worries.", "Fair enough.", "That sucks."],
            "answer": "My bad!"
        },
        "type_2": {
            "scene": "Сериал «Friends». Чендлер путает имена — и сразу признаёт ошибку коротко и неформально:",
            "options": ["My bad!", "I'm good.", "Hang on.", "Deal."],
            "answer": "My bad!"
        },
        "type_3": {
            "question": "Что значит «My bad»?",
            "options": ["Я плохой", "Моя вина / Извини", "Мне плохо", "Плохая идея"],
            "answer": "Моя вина / Извини"
        },
        "type_4": {
            "question": "Как перевести «My bad»?",
            "options": ["Мой плохой", "Моя вина / Извини", "Моя ошибка в работе", "Мне плохо"],
            "answer": "Моя вина / Извини"
        }
    },

    {
        "id": 10,
        "phrase": "That sucks",
        "translation": "Это отстой / Как жаль",
        "meaning": "Выражение сочувствия или недовольства ситуацией",
        "example": "I missed my flight. — That sucks! Are you okay?",

        "type_1": {
            "question": "Друг говорит: «I failed my exam.» Ты хочешь выразить сочувствие. Что скажешь?",
            "options": ["That sucks!", "Lucky you.", "No worries.", "Sounds good."],
            "answer": "That sucks!"
        },
        "type_2": {
            "scene": "Сериал «How I Met Your Mother». Тед рассказывает о плохом свидании — друзья реагируют сочувственно:",
            "options": ["That sucks!", "Go for it.", "Works for me.", "I'm down."],
            "answer": "That sucks!"
        },
        "type_3": {
            "question": "Что значит «That sucks»?",
            "options": ["Это хорошо", "Это отстой / Как жаль", "Пей это", "Это смешно"],
            "answer": "Это отстой / Как жаль"
        },
        "type_4": {
            "question": "Как перевести «That sucks»?",
            "options": ["Это засасывает", "Это отстой / Жаль", "Это пьют", "Это сложно"],
            "answer": "Это отстой / Жаль"
        }
    },

    {
        "id": 11,
        "phrase": "Lucky you",
        "translation": "Тебе повезло / Везунчик",
        "meaning": "Лёгкая зависть или радость за человека",
        "example": "I'm going to Hawaii next week! — Lucky you!",

        "type_1": {
            "question": "Друг говорит: «I won free concert tickets!» Ты рад за него. Что скажешь?",
            "options": ["Lucky you!", "That sucks.", "My bad.", "No way."],
            "answer": "Lucky you!"
        },
        "type_2": {
            "scene": "Сериал «Parks and Recreation». Персонаж говорит, что уходит в отпуск на месяц — коллеги реагируют с завистью:",
            "options": ["Lucky you!", "I'm not sure.", "Let me know.", "Hold on."],
            "answer": "Lucky you!"
        },
        "type_3": {
            "question": "Что значит «Lucky you»?",
            "options": ["Ты несчастный", "Тебе повезло", "Ты смешной", "Ты устал"],
            "answer": "Тебе повезло"
        },
        "type_4": {
            "question": "Как перевести «Lucky you»?",
            "options": ["Удачливый ты", "Тебе повезло / Везунчик", "Ты хороший", "Будь удачлив"],
            "answer": "Тебе повезло / Везунчик"
        }
    },

    {
        "id": 12,
        "phrase": "Good for you",
        "translation": "Молодец / Рад за тебя",
        "meaning": "Похвала или одобрение чужого успеха",
        "example": "I finally quit smoking! — Good for you, that's great!",

        "type_1": {
            "question": "Друг говорит: «I started going to the gym every day.» Ты хочешь похвалить его. Что скажешь?",
            "options": ["Good for you!", "That sucks.", "No big deal.", "I'm not sure."],
            "answer": "Good for you!"
        },
        "type_2": {
            "scene": "Сериал «New Girl». Одна из подруг говорит, что нашла новую работу — остальные искренне хвалят её:",
            "options": ["Good for you!", "We'll see.", "I guess.", "Hang on."],
            "answer": "Good for you!"
        },
        "type_3": {
            "question": "Что значит «Good for you»?",
            "options": ["Это полезно", "Молодец / Рад за тебя", "Тебе хорошо", "Ты добрый"],
            "answer": "Молодец / Рад за тебя"
        },
        "type_4": {
            "question": "Как перевести «Good for you»?",
            "options": ["Хорошо для тебя", "Молодец / Рад за тебя", "Ты хорош", "Тебе повезло"],
            "answer": "Молодец / Рад за тебя"
        }
    },

    {
        "id": 13,
        "phrase": "I guess",
        "translation": "Наверное / Полагаю",
        "meaning": "Неуверенное согласие или предположение",
        "example": "Are you tired? — I guess, a little.",

        "type_1": {
            "question": "Тебя спрашивают: «Do you want to come to the party?» Ты не очень хочешь, но не против. Что скажешь?",
            "options": ["I guess.", "No way.", "I'm down!", "Deal."],
            "answer": "I guess."
        },
        "type_2": {
            "scene": "Фильм «Clueless». Героиню спрашивают, понравился ли ей фильм — она отвечает без особого энтузиазма:",
            "options": ["I guess.", "Sounds good.", "I'm not gonna lie.", "Fair enough."],
            "answer": "I guess."
        },
        "type_3": {
            "question": "Что значит «I guess»?",
            "options": ["Я знаю точно", "Наверное / Полагаю", "Я угадываю всегда", "Мне не важно"],
            "answer": "Наверное / Полагаю"
        },
        "type_4": {
            "question": "Как перевести «I guess»?",
            "options": ["Я гадаю", "Наверное / Думаю, да", "Я считаю это неверным", "Я знаю"],
            "answer": "Наверное / Думаю, да"
        }
    },

    {
        "id": 14,
        "phrase": "I suppose",
        "translation": "Полагаю / Думаю, да",
        "meaning": "Осторожное согласие или допущение",
        "example": "Is this a good idea? — I suppose it could work.",

        "type_1": {
            "question": "Тебя спрашивают: «Is the movie good?» Ты видел, но не уверен в оценке. Что скажешь?",
            "options": ["I suppose.", "No way.", "That sucks.", "Go for it."],
            "answer": "I suppose."
        },
        "type_2": {
            "scene": "Сериал «Downtown Abbey». Леди отвечает на вопрос, стоит ли ехать в Лондон — без уверенности, но соглашается:",
            "options": ["I suppose.", "Sounds good.", "My bad.", "Deal."],
            "answer": "I suppose."
        },
        "type_3": {
            "question": "Что значит «I suppose»?",
            "options": ["Я не знаю ничего", "Полагаю / Думаю, да", "Я против", "Я устал"],
            "answer": "Полагаю / Думаю, да"
        },
        "type_4": {
            "question": "Как перевести «I suppose»?",
            "options": ["Я полагаю неправильно", "Полагаю / Думаю, да", "Я предполагаю худшее", "Я не знаю"],
            "answer": "Полагаю / Думаю, да"
        }
    },

    {
        "id": 15,
        "phrase": "I mean",
        "translation": "Я имею в виду",
        "meaning": "Уточнение или пояснение сказанного",
        "example": "It was okay. I mean, not the best, but fine.",

        "type_1": {
            "question": "Ты сказал что-то непонятно и хочешь пояснить: «The party was... ___ it was fun but too loud.»",
            "options": ["I mean,", "I guess,", "You know,", "Basically,"],
            "answer": "I mean,"
        },
        "type_2": {
            "scene": "Сериал «Friends». Росс начинает объяснять свою мысль и останавливается, чтобы уточнить её:",
            "options": ["I mean,", "Hold on,", "Deal,", "Sort of,"],
            "answer": "I mean,"
        },
        "type_3": {
            "question": "Что значит «I mean»?",
            "options": ["Я злой", "Я имею в виду", "Я понял", "Мне жаль"],
            "answer": "Я имею в виду"
        },
        "type_4": {
            "question": "Как перевести «I mean»?",
            "options": ["Я плохой", "Я имею в виду", "Я думаю иначе", "Мне грустно"],
            "answer": "Я имею в виду"
        }
    },

    {
        "id": 16,
        "phrase": "Basically",
        "translation": "В основном / По сути",
        "meaning": "Упрощённое объяснение или подведение итога",
        "example": "What happened? — Basically, we missed the train and had to walk.",

        "type_1": {
            "question": "Друг спрашивает: «What's the plan?» Ты хочешь объяснить просто: «___ we eat, then go to the cinema.»",
            "options": ["Basically,", "I mean,", "I suppose,", "You know,"],
            "answer": "Basically,"
        },
        "type_2": {
            "scene": "Сериал «The Big Bang Theory». Шелдон объясняет сложную идею очень просто, начиная с ключевого слова:",
            "options": ["Basically,", "I guess,", "Fair enough,", "Sort of,"],
            "answer": "Basically,"
        },
        "type_3": {
            "question": "Что значит «Basically»?",
            "options": ["Точно и детально", "В основном / По сути", "Случайно", "Невероятно"],
            "answer": "В основном / По сути"
        },
        "type_4": {
            "question": "Как перевести «Basically»?",
            "options": ["Базово", "В основном / По сути", "Очень сложно", "Немного"],
            "answer": "В основном / По сути"
        }
    },

    {
        "id": 17,
        "phrase": "You know",
        "translation": "Ты понимаешь / Ну ты знаешь",
        "meaning": "Слово-заполнитель или апелляция к собеседнику",
        "example": "It was just, you know, a bit awkward.",

        "type_1": {
            "question": "Ты рассказываешь историю и хочешь убедиться, что друг понимает: «It was just... ___, really weird.»",
            "options": ["you know,", "I mean,", "I guess,", "sort of,"],
            "answer": "you know,"
        },
        "type_2": {
            "scene": "Сериал «Seinfeld». Джордж объясняет ситуацию и делает паузу, ища поддержки у собеседника:",
            "options": ["you know?", "deal?", "basically?", "I suppose?"],
            "answer": "you know?"
        },
        "type_3": {
            "question": "Что значит «You know» в разговоре?",
            "options": ["Ты всё знаешь", "Слово-пауза / Апелляция к собеседнику", "Ты умный", "Ты должен знать"],
            "answer": "Слово-пауза / Апелляция к собеседнику"
        },
        "type_4": {
            "question": "Как перевести «You know» в контексте разговора?",
            "options": ["Ты знаешь всё", "Ну ты понимаешь / Ты же знаешь", "Ты должен", "Знай это"],
            "answer": "Ну ты понимаешь / Ты же знаешь"
        }
    },

    {
        "id": 18,
        "phrase": "You know what I mean",
        "translation": "Ты понимаешь, о чём я",
        "meaning": "Проверка понимания собеседника",
        "example": "It felt off, you know what I mean?",

        "type_1": {
            "question": "Ты объяснил идею и хочешь убедиться, что тебя поняли. Что добавишь в конце?",
            "options": ["You know what I mean?", "I'm not sure.", "Hold on.", "Let me know."],
            "answer": "You know what I mean?"
        },
        "type_2": {
            "scene": "Сериал «Entourage». Персонаж описывает ощущение от встречи и в конце ищет подтверждения у друга:",
            "options": ["You know what I mean?", "I'm good.", "Works for me.", "Fair enough."],
            "answer": "You know what I mean?"
        },
        "type_3": {
            "question": "Что значит «You know what I mean»?",
            "options": ["Ты знаешь, что я думаю о тебе", "Ты понимаешь, о чём я", "Ты согласен?", "Ты слышишь меня?"],
            "answer": "Ты понимаешь, о чём я"
        },
        "type_4": {
            "question": "Как перевести «You know what I mean»?",
            "options": ["Знаешь, что я имею", "Ты понимаешь, о чём я", "Ты знаешь, что значит", "Понимаешь меня буквально"],
            "answer": "Ты понимаешь, о чём я"
        }
    },

    {
        "id": 19,
        "phrase": "Kind of",
        "translation": "Как бы / Вроде того",
        "meaning": "Смягчение утверждения",
        "example": "Was it good? — Kind of, but not amazing.",

        "type_1": {
            "question": "Друг спрашивает: «Are you tired?» Ты устал, но не сильно. Что скажешь?",
            "options": ["Kind of.", "I'm down.", "That sucks.", "No way."],
            "answer": "Kind of."
        },
        "type_2": {
            "scene": "Фильм «Mean Girls». Персонаж отвечает на вопрос неопределённо, не давая чёткого «да» или «нет»:",
            "options": ["Kind of.", "Sounds good.", "Deal.", "Go for it."],
            "answer": "Kind of."
        },
        "type_3": {
            "question": "Что значит «Kind of»?",
            "options": ["Очень сильно", "Как бы / Вроде того", "Никак", "Точно да"],
            "answer": "Как бы / Вроде того"
        },
        "type_4": {
            "question": "Как перевести «Kind of»?",
            "options": ["Вид чего-то", "Как бы / Немного / Вроде того", "Добрый", "Только так"],
            "answer": "Как бы / Немного / Вроде того"
        }
    },

    {
        "id": 20,
        "phrase": "Sort of",
        "translation": "Своего рода / Примерно так",
        "meaning": "Неточное согласие или описание",
        "example": "Do you like jazz? — Sort of, it depends on the song.",

        "type_1": {
            "question": "Тебя спрашивают: «Is this your job?» Это близко к правде, но не точно. Что скажешь?",
            "options": ["Sort of.", "No way.", "I'm down.", "Deal."],
            "answer": "Sort of."
        },
        "type_2": {
            "scene": "Сериал «Brooklyn Nine-Nine». Джейк отвечает на вопрос о своих планах — не совсем «да», но близко:",
            "options": ["Sort of.", "My bad.", "No worries.", "Catch you later."],
            "answer": "Sort of."
        },
        "type_3": {
            "question": "Что значит «Sort of»?",
            "options": ["Совсем нет", "Своего рода / Примерно так", "Точно да", "Никогда"],
            "answer": "Своего рода / Примерно так"
        },
        "type_4": {
            "question": "Как перевести «Sort of»?",
            "options": ["Сортировать что-то", "Своего рода / Примерно так", "Вид сорта", "Немного другое"],
            "answer": "Своего рода / Примерно так"
        }
    },

    {
        "id": 21,
        "phrase": "Pretty much",
        "translation": "В основном / Почти что так",
        "meaning": "Подтверждение с небольшой оговоркой",
        "example": "Is everything ready? — Pretty much, just one thing left.",

        "type_1": {
            "question": "Тебя спрашивают: «Did you finish the project?» Почти всё готово. Что скажешь?",
            "options": ["Pretty much.", "Not at all.", "No way.", "I suppose not."],
            "answer": "Pretty much."
        },
        "type_2": {
            "scene": "Сериал «The Office». Майкл спрашивает, понял ли Джим задачу — тот отвечает утвердительно, но уклончиво:",
            "options": ["Pretty much.", "I'm not gonna lie.", "Hold on.", "Hang on."],
            "answer": "Pretty much."
        },
        "type_3": {
            "question": "Что значит «Pretty much»?",
            "options": ["Очень красиво", "В основном / Почти что так", "Немного", "Совсем нет"],
            "answer": "В основном / Почти что так"
        },
        "type_4": {
            "question": "Как перевести «Pretty much»?",
            "options": ["Красиво много", "В основном / Почти что так", "Немного больше", "Очень мало"],
            "answer": "В основном / Почти что так"
        }
    },

    {
        "id": 22,
        "phrase": "I feel like",
        "translation": "Мне кажется / Я как будто",
        "meaning": "Выражение субъективного мнения или ощущения",
        "example": "I feel like we've been here before.",

        "type_1": {
            "question": "Ты хочешь поделиться мнением: «___ this movie is too long.» Что вставишь в начало?",
            "options": ["I feel like", "I mean", "Basically", "I suppose"],
            "answer": "I feel like"
        },
        "type_2": {
            "scene": "Сериал «Girls». Главная героиня делится своим ощущением от отношений, начиная фразу мягко:",
            "options": ["I feel like", "You know", "I'm not gonna lie", "Sort of"],
            "answer": "I feel like"
        },
        "type_3": {
            "question": "Что значит «I feel like»?",
            "options": ["Я чувствую запах", "Мне кажется / Я как будто", "Я хочу спать", "Я похож на"],
            "answer": "Мне кажется / Я как будто"
        },
        "type_4": {
            "question": "Как перевести «I feel like»?",
            "options": ["Я чувствую похожесть", "Мне кажется / Я как будто", "Мне нравится", "Я устал как"],
            "answer": "Мне кажется / Я как будто"
        }
    },

    {
        "id": 23,
        "phrase": "I'd say",
        "translation": "Я бы сказал",
        "meaning": "Осторожное мнение или оценка",
        "example": "How long will it take? — I'd say about two hours.",

        "type_1": {
            "question": "Тебя спрашивают: «How was the food?» Ты хочешь дать осторожную оценку. Как начнёшь ответ?",
            "options": ["I'd say it was okay.", "I'm down.", "Deal.", "No big deal."],
            "answer": "I'd say it was okay."
        },
        "type_2": {
            "scene": "Сериал «Master of None». Персонаж даёт совет другу, начиная осторожно с личной оценки:",
            "options": ["I'd say", "You know what I mean", "No worries", "Hold on"],
            "answer": "I'd say"
        },
        "type_3": {
            "question": "Что значит «I'd say»?",
            "options": ["Я обязан сказать", "Я бы сказал", "Я скажу всегда", "Мне говорят"],
            "answer": "Я бы сказал"
        },
        "type_4": {
            "question": "Как перевести «I'd say»?",
            "options": ["Я сказал", "Я бы сказал", "Мне скажут", "Говори за меня"],
            "answer": "Я бы сказал"
        }
    },

    {
        "id": 24,
        "phrase": "I'm not sure",
        "translation": "Я не уверен",
        "meaning": "Выражение неопределённости или сомнения",
        "example": "Do you know the answer? — I'm not sure, let me check.",

        "type_1": {
            "question": "Тебя спрашивают: «Are you coming tomorrow?» Ты ещё не решил. Что скажешь?",
            "options": ["I'm not sure.", "I'm down!", "Sounds good.", "Deal."],
            "answer": "I'm not sure."
        },
        "type_2": {
            "scene": "Сериал «Schitt's Creek». Дэвида спрашивают о планах — он отвечает неопределённо и с паузой:",
            "options": ["I'm not sure.", "Lucky you.", "Go for it.", "Works for me."],
            "answer": "I'm not sure."
        },
        "type_3": {
            "question": "Что значит «I'm not sure»?",
            "options": ["Я точно знаю", "Я не уверен", "Мне не важно", "Я не хочу"],
            "answer": "Я не уверен"
        },
        "type_4": {
            "question": "Как перевести «I'm not sure»?",
            "options": ["Я не такой", "Я не уверен", "Мне не лечиться", "Я не стараюсь"],
            "answer": "Я не уверен"
        }
    },

    {
        "id": 25,
        "phrase": "It depends",
        "translation": "Зависит / Как когда",
        "meaning": "Ответ, что всё зависит от обстоятельств",
        "example": "Do you like mornings? — It depends on the day.",

        "type_1": {
            "question": "Тебя спрашивают: «Do you prefer coffee or tea?» Ответ непростой. Что скажешь?",
            "options": ["It depends.", "I'm down.", "No way.", "Let me know."],
            "answer": "It depends."
        },
        "type_2": {
            "scene": "Ток-шоу. Эксперта спрашивают: «Is social media good or bad?» — он даёт взвешенный ответ одним словом:",
            "options": ["It depends.", "Pretty much.", "I suppose.", "Kind of."],
            "answer": "It depends."
        },
        "type_3": {
            "question": "Что значит «It depends»?",
            "options": ["Это точно", "Зависит / Как когда", "Это не важно", "Это случайно"],
            "answer": "Зависит / Как когда"
        },
        "type_4": {
            "question": "Как перевести «It depends»?",
            "options": ["Это висит", "Зависит / Как когда", "Это зависает", "Оно зависело"],
            "answer": "Зависит / Как когда"
        }
    },

    {
        "id": 26,
        "phrase": "I don't think so",
        "translation": "Я так не думаю / Вряд ли",
        "meaning": "Вежливое несогласие или отрицание",
        "example": "Is he coming? — I don't think so.",

        "type_1": {
            "question": "Тебя спрашивают: «Will it rain today?» Ты смотришь в окно — солнечно. Что скажешь?",
            "options": ["I don't think so.", "I'm down.", "No problem.", "Sounds good."],
            "answer": "I don't think so."
        },
        "type_2": {
            "scene": "Фильм «Legally Blonde». Профессор задаёт вопрос, студентка не согласна с его предположением:",
            "options": ["I don't think so.", "Let me know.", "Go for it.", "I'm good."],
            "answer": "I don't think so."
        },
        "type_3": {
            "question": "Что значит «I don't think so»?",
            "options": ["Я не думаю вообще", "Я так не думаю / Вряд ли", "Мне не нравится думать", "Я не умею думать"],
            "answer": "Я так не думаю / Вряд ли"
        },
        "type_4": {
            "question": "Как перевести «I don't think so»?",
            "options": ["Я не думаю так всегда", "Я так не думаю / Вряд ли", "Мне не дают думать", "Я думаю не так"],
            "answer": "Я так не думаю / Вряд ли"
        }
    },

    {
        "id": 27,
        "phrase": "What's up",
        "translation": "Как дела? / Что нового?",
        "meaning": "Неформальное приветствие",
        "example": "Hey! What's up? — Not much, just chilling.",

        "type_1": {
            "question": "Ты встречаешь друга на улице. Как поздороваешься неформально?",
            "options": ["What's up?", "Take care.", "Long time no see.", "I'm good."],
            "answer": "What's up?"
        },
        "type_2": {
            "scene": "Сериал «Fresh Prince of Bel-Air». Уилл встречает знакомого и приветствует его в своей обычной манере:",
            "options": ["What's up?", "How's it going?", "I'm not sure.", "All good."],
            "answer": "What's up?"
        },
        "type_3": {
            "question": "Что значит «What's up»?",
            "options": ["Что там вверху?", "Как дела? / Что нового?", "Что случилось плохое?", "Куда ты идёшь?"],
            "answer": "Как дела? / Что нового?"
        },
        "type_4": {
            "question": "Как перевести «What's up»?",
            "options": ["Что вверх?", "Как дела? / Что нового?", "Что поднялось?", "Почему вверх?"],
            "answer": "Как дела? / Что нового?"
        }
    },

    {
        "id": 28,
        "phrase": "How's it going",
        "translation": "Как дела? / Как ты?",
        "meaning": "Неформальный вопрос о состоянии дел",
        "example": "Hey! How's it going? — Pretty good, thanks!",

        "type_1": {
            "question": "Ты звонишь другу, которого давно не видел. Как начнёшь разговор?",
            "options": ["How's it going?", "Take care.", "Catch you later.", "I'm good."],
            "answer": "How's it going?"
        },
        "type_2": {
            "scene": "Сериал «How I Met Your Mother». Барни встречает кого-то у барной стойки и задаёт стандартный вопрос:",
            "options": ["How's it going?", "What's up?", "Long time no see.", "No worries."],
            "answer": "How's it going?"
        },
        "type_3": {
            "question": "Что значит «How's it going»?",
            "options": ["Куда это идёт?", "Как дела? / Как ты?", "Как это работает?", "Что происходит плохого?"],
            "answer": "Как дела? / Как ты?"
        },
        "type_4": {
            "question": "Как перевести «How's it going»?",
            "options": ["Как это идёт?", "Как дела? / Как ты?", "Куда это движется?", "Как оно ходит?"],
            "answer": "Как дела? / Как ты?"
        }
    },

    {
        "id": 29,
        "phrase": "Long time no see",
        "translation": "Сто лет не виделись",
        "meaning": "Фраза при встрече после долгой разлуки",
        "example": "Oh wow, long time no see! How have you been?",

        "type_1": {
            "question": "Ты встречаешь старого одноклассника, которого не видел 5 лет. Что скажешь?",
            "options": ["Long time no see!", "What's up?", "How's it going?", "Take care."],
            "answer": "Long time no see!"
        },
        "type_2": {
            "scene": "Фильм «Ratatouille». Персонаж встречает кого-то из прошлого и сразу комментирует давнее отсутствие:",
            "options": ["Long time no see!", "All good.", "I'm good.", "Catch you later."],
            "answer": "Long time no see!"
        },
        "type_3": {
            "question": "Что значит «Long time no see»?",
            "options": ["Долго смотреть нельзя", "Сто лет не виделись", "Давно не смотрел", "Я долго ждал"],
            "answer": "Сто лет не виделись"
        },
        "type_4": {
            "question": "Как перевести «Long time no see»?",
            "options": ["Долгое время не смотрел", "Сто лет не виделись", "Давно не было видно", "Видел давно"],
            "answer": "Сто лет не виделись"
        }
    },

    {
        "id": 30,
        "phrase": "Take care",
        "translation": "Береги себя / Пока",
        "meaning": "Тёплое прощание",
        "example": "Bye! Take care of yourself!",

        "type_1": {
            "question": "Ты прощаешься с другом после встречи. Как попрощаешься тепло?",
            "options": ["Take care!", "What's up?", "Long time no see!", "I'm good."],
            "answer": "Take care!"
        },
        "type_2": {
            "scene": "Сериал «Gilmore Girls». Мать прощается с дочерью по телефону тёплой привычной фразой:",
            "options": ["Take care!", "Catch you later.", "How's it going?", "All good."],
            "answer": "Take care!"
        },
        "type_3": {
            "question": "Что значит «Take care»?",
            "options": ["Возьми это", "Береги себя / Пока", "Будь осторожен с вещами", "Помоги мне"],
            "answer": "Береги себя / Пока"
        },
        "type_4": {
            "question": "Как перевести «Take care»?",
            "options": ["Возьми заботу", "Береги себя / Пока", "Позаботься о нём", "Принеси помощь"],
            "answer": "Береги себя / Пока"
        }
    },

    {
        "id": 31,
        "phrase": "Catch you later",
        "translation": "Увидимся / Пока",
        "meaning": "Неформальное прощание",
        "example": "Alright, I gotta run — catch you later!",

        "type_1": {
            "question": "Ты торопишься уходить и хочешь попрощаться неформально. Что скажешь?",
            "options": ["Catch you later!", "Long time no see.", "What's up?", "I'm not sure."],
            "answer": "Catch you later!"
        },
        "type_2": {
            "scene": "Сериал «The Fresh Prince». Уилл убегает на встречу и бросает фразу через плечо на ходу:",
            "options": ["Catch you later!", "Take care.", "I'm good.", "How's it going?"],
            "answer": "Catch you later!"
        },
        "type_3": {
            "question": "Что значит «Catch you later»?",
            "options": ["Поймаю тебя потом", "Увидимся / Пока", "Перезвоню позже", "Найду тебя"],
            "answer": "Увидимся / Пока"
        },
        "type_4": {
            "question": "Как перевести «Catch you later»?",
            "options": ["Поймаю тебя позже", "Увидимся / Пока", "Встречу позже специально", "Позвоню потом"],
            "answer": "Увидимся / Пока"
        }
    },

    {
        "id": 32,
        "phrase": "I'm good",
        "translation": "Я в порядке / Спасибо, не нужно",
        "meaning": "Ответ на «как дела» или вежливый отказ",
        "example": "Want more coffee? — I'm good, thanks.",

        "type_1": {
            "question": "Официант спрашивает: «More water?» Тебе не нужно. Что скажешь вежливо?",
            "options": ["I'm good, thanks.", "I'm down.", "Go for it.", "Deal."],
            "answer": "I'm good, thanks."
        },
        "type_2": {
            "scene": "Сериал «Brooklyn Nine-Nine». Эми отвечает на вопрос «всё ок?» после стрессового дня — коротко и спокойно:",
            "options": ["I'm good.", "I'm not sure.", "Sort of.", "Kind of."],
            "answer": "I'm good."
        },
        "type_3": {
            "question": "Что значит «I'm good» в ответ на предложение?",
            "options": ["Я хороший человек", "Я в порядке / Не нужно, спасибо", "Мне хорошо сейчас", "Я добрый"],
            "answer": "Я в порядке / Не нужно, спасибо"
        },
        "type_4": {
            "question": "Как перевести «I'm good»?",
            "options": ["Я добрый", "Я в порядке / Всё хорошо", "Я красивый", "Мне хорошо работать"],
            "answer": "Я в порядке / Всё хорошо"
        }
    },

    {
        "id": 33,
        "phrase": "All good",
        "translation": "Всё хорошо / Всё окей",
        "meaning": "Подтверждение, что всё в порядке",
        "example": "Sorry about the noise! — All good, don't worry.",

        "type_1": {
            "question": "Сосед извиняется за шум. Тебе не мешало. Что скажешь?",
            "options": ["All good!", "That sucks.", "I'm not sure.", "No way."],
            "answer": "All good!"
        },
        "type_2": {
            "scene": "Сериал «Ted Lasso». Тренер проверяет, как дела у игрока — тот отвечает бодро и спокойно:",
            "options": ["All good!", "I mean...", "It depends.", "I suppose."],
            "answer": "All good!"
        },
        "type_3": {
            "question": "Что значит «All good»?",
            "options": ["Все добрые", "Всё хорошо / Всё окей", "Все хорошие люди", "Много хорошего"],
            "answer": "Всё хорошо / Всё окей"
        },
        "type_4": {
            "question": "Как перевести «All good»?",
            "options": ["Все добрые", "Всё хорошо / Всё окей", "Все хорошие", "Много хорошего"],
            "answer": "Всё хорошо / Всё окей"
        }
    },

    {
        "id": 34,
        "phrase": "Hang on",
        "translation": "Подожди / Одну секунду",
        "meaning": "Просьба немного подождать",
        "example": "Hang on, I'll be right back.",

        "type_1": {
            "question": "Тебе нужно секунду — ты ищешь ключи. Что скажешь другу?",
            "options": ["Hang on!", "Catch you later.", "No worries.", "All good."],
            "answer": "Hang on!"
        },
        "type_2": {
            "scene": "Сериал «Friends». Монику отвлекают во время готовки — она просит немного подождать:",
            "options": ["Hang on!", "I'm good.", "Fair enough.", "That makes sense."],
            "answer": "Hang on!"
        },
        "type_3": {
            "question": "Что значит «Hang on»?",
            "options": ["Держись за что-то", "Подожди / Одну секунду", "Повесь это", "Возьми меня"],
            "answer": "Подожди / Одну секунду"
        },
        "type_4": {
            "question": "Как перевести «Hang on»?",
            "options": ["Повесь это", "Подожди / Одну секунду", "Держись всегда", "Зависни тут"],
            "answer": "Подожди / Одну секунду"
        }
    },

    {
        "id": 35,
        "phrase": "Hold on",
        "translation": "Подожди / Стоп",
        "meaning": "Просьба остановиться или подождать",
        "example": "Hold on — did you just say you quit your job?",

        "type_1": {
            "question": "Друг рассказывает что-то важное очень быстро. Ты хочешь его притормозить. Что скажешь?",
            "options": ["Hold on!", "Hang on!", "Go for it.", "No problem."],
            "answer": "Hold on!"
        },
        "type_2": {
            "scene": "Фильм «The Avengers». Персонаж прерывает разговор, чтобы переспросить удивительный факт:",
            "options": ["Hold on!", "I'm good.", "Take care.", "All good."],
            "answer": "Hold on!"
        },
        "type_3": {
            "question": "Что значит «Hold on»?",
            "options": ["Держи крепко", "Подожди / Стоп", "Возьми это", "Не отпускай"],
            "answer": "Подожди / Стоп"
        },
        "type_4": {
            "question": "Как перевести «Hold on»?",
            "options": ["Держи это", "Подожди / Стоп", "Подними это", "Держись на чём-то"],
            "answer": "Подожди / Стоп"
        }
    },

    {
        "id": 36,
        "phrase": "Give me a sec",
        "translation": "Дай мне секунду",
        "meaning": "Просьба немного подождать",
        "example": "Are you ready? — Give me a sec, almost done.",

        "type_1": {
            "question": "Тебя торопят, но ты почти готов. Что скажешь?",
            "options": ["Give me a sec!", "I'm down.", "No worries.", "Deal."],
            "answer": "Give me a sec!"
        },
        "type_2": {
            "scene": "Сериал «Grey's Anatomy». Доктор заканчивает запись в карточке и просит секунду подождать:",
            "options": ["Give me a sec.", "I'm not sure.", "How's it going?", "Lucky you."],
            "answer": "Give me a sec."
        },
        "type_3": {
            "question": "Что значит «Give me a sec»?",
            "options": ["Дай мне секрет", "Дай мне секунду", "Дай мне силу", "Скажи мне сейчас"],
            "answer": "Дай мне секунду"
        },
        "type_4": {
            "question": "Как перевести «Give me a sec»?",
            "options": ["Дай мне второй", "Дай мне секунду", "Покажи мне секунду", "Дай секунду ему"],
            "answer": "Дай мне секунду"
        }
    },

    {
        "id": 37,
        "phrase": "Wait a minute",
        "translation": "Подожди минуту / Стоп",
        "meaning": "Остановка для осмысления или уточнения",
        "example": "Wait a minute — that doesn't add up.",

        "type_1": {
            "question": "Друг говорит что-то противоречивое. Ты хочешь остановить разговор. Что скажешь?",
            "options": ["Wait a minute!", "No problem.", "That sucks.", "I suppose."],
            "answer": "Wait a minute!"
        },
        "type_2": {
            "scene": "Фильм «Back to the Future». Доктор Браун внезапно понимает важную деталь и останавливается:",
            "options": ["Wait a minute!", "Hold on.", "Hang on.", "Give me a sec."],
            "answer": "Wait a minute!"
        },
        "type_3": {
            "question": "Что значит «Wait a minute»?",
            "options": ["Жди ровно минуту", "Подожди / Стоп (для осмысления)", "Минуту внимания", "Одна минута"],
            "answer": "Подожди / Стоп (для осмысления)"
        },
        "type_4": {
            "question": "Как перевести «Wait a minute»?",
            "options": ["Жди одну минуту", "Подожди минуту / Стоп", "Одна минута ожидания", "Минута прошла"],
            "answer": "Подожди минуту / Стоп"
        }
    },

    {
        "id": 38,
        "phrase": "Just a second",
        "translation": "Одну секунду",
        "meaning": "Просьба чуть-чуть подождать",
        "example": "Can I ask you something? — Just a second, I'm on the phone.",

        "type_1": {
            "question": "Тебе звонят, а ты занят. Что скажешь, прежде чем ответить?",
            "options": ["Just a second!", "Catch you later.", "I'm good.", "Hold on."],
            "answer": "Just a second!"
        },
        "type_2": {
            "scene": "Сериал «The Crown». Помощник просит внимания королевы — она поднимает руку и говорит:",
            "options": ["Just a second.", "I'm not gonna lie.", "That makes sense.", "I'd say."],
            "answer": "Just a second."
        },
        "type_3": {
            "question": "Что значит «Just a second»?",
            "options": ["Только второй раз", "Одну секунду / Чуть подождите", "Просто второй", "Ещё один раз"],
            "answer": "Одну секунду / Чуть подождите"
        },
        "type_4": {
            "question": "Как перевести «Just a second»?",
            "options": ["Только секундный", "Одну секунду", "Просто второй вариант", "Лишь секунду назад"],
            "answer": "Одну секунду"
        }
    },

    {
        "id": 39,
        "phrase": "I'm not gonna lie",
        "translation": "Честно говоря / Не буду врать",
        "meaning": "Вступление к честному признанию",
        "example": "I'm not gonna lie, that was really hard.",

        "type_1": {
            "question": "Ты хочешь честно признаться, что фильм тебе не понравился. Как начнёшь?",
            "options": ["I'm not gonna lie,", "I mean,", "Basically,", "You know,"],
            "answer": "I'm not gonna lie,"
        },
        "type_2": {
            "scene": "Реалити-шоу. Участник признаётся камере, что задание было намного сложнее, чем он ожидал:",
            "options": ["I'm not gonna lie,", "I guess,", "It depends,", "Sort of,"],
            "answer": "I'm not gonna lie,"
        },
        "type_3": {
            "question": "Что значит «I'm not gonna lie»?",
            "options": ["Я не умею лгать", "Честно говоря / Не буду врать", "Я никогда не лгу", "Лгать плохо"],
            "answer": "Честно говоря / Не буду врать"
        },
        "type_4": {
            "question": "Как перевести «I'm not gonna lie»?",
            "options": ["Я не буду ложиться", "Честно говоря / Не буду врать", "Я не умею лгать вообще", "Я говорю правду всегда"],
            "answer": "Честно говоря / Не буду врать"
        }
    },

    {
        "id": 40,
        "phrase": "At the end of the day",
        "translation": "В конце концов / По большому счёту",
        "meaning": "Итоговый вывод или главная мысль",
        "example": "At the end of the day, what matters is your health.",

        "type_1": {
            "question": "Ты хочешь подвести итог разговора о работе. Как начнёшь финальную мысль?",
            "options": ["At the end of the day,", "I mean,", "Basically,", "I feel like"],
            "answer": "At the end of the day,"
        },
        "type_2": {
            "scene": "Ток-шоу. Гость завершает мысль об успехе, говоря о главном, что важно в итоге:",
            "options": ["At the end of the day,", "You know what I mean,", "I'd say,", "I'm not gonna lie,"],
            "answer": "At the end of the day,"
        },
        "type_3": {
            "question": "Что значит «At the end of the day»?",
            "options": ["В конце рабочего дня", "В конце концов / По большому счёту", "Вечером всегда", "После работы"],
            "answer": "В конце концов / По большому счёту"
        },
        "type_4": {
            "question": "Как перевести «At the end of the day»?",
            "options": ["В конце дня буквально", "В конце концов / По большому счёту", "В финале дня всегда", "К концу суток"],
            "answer": "В конце концов / По большому счёту"
        }
    },

    {
        "id": 41,
        "phrase": "That's the thing",
        "translation": "Вот в чём дело / Именно в этом и проблема",
        "meaning": "Указание на суть проблемы или ключевой момент",
        "example": "I want to help, but that's the thing — I don't have time.",

        "type_1": {
            "question": "Ты хочешь объяснить другу суть проблемы. Как начнёшь?",
            "options": ["That's the thing —", "That sucks,", "I mean,", "I guess,"],
            "answer": "That's the thing —"
        },
        "type_2": {
            "scene": "Сериал «Succession». Персонаж наконец объясняет, в чём настоящая проблема ситуации:",
            "options": ["That's the thing.", "It is what it is.", "We'll see.", "I'd say."],
            "answer": "That's the thing."
        },
        "type_3": {
            "question": "Что значит «That's the thing»?",
            "options": ["Это та вещь", "Вот в чём дело / Именно в этом проблема", "Это странная штука", "Это не важно"],
            "answer": "Вот в чём дело / Именно в этом проблема"
        },
        "type_4": {
            "question": "Как перевести «That's the thing»?",
            "options": ["Это та вещь", "Вот в чём дело / Именно в этом проблема", "Это такая вещь", "Это и есть то"],
            "answer": "Вот в чём дело / Именно в этом проблема"
        }
    },

    {
        "id": 42,
        "phrase": "It is what it is",
        "translation": "Что есть, то есть / Ничего не поделаешь",
        "meaning": "Принятие ситуации, которую нельзя изменить",
        "example": "The flight was cancelled. — Well, it is what it is.",

        "type_1": {
            "question": "Ваша команда проиграла. Ты расстроен, но принимаешь это. Что скажешь?",
            "options": ["It is what it is.", "That sucks!", "No way.", "I'm not sure."],
            "answer": "It is what it is."
        },
        "type_2": {
            "scene": "Сериал «Breaking Bad». Уолтер принимает неприятный факт спокойно и философски:",
            "options": ["It is what it is.", "No big deal.", "Fair enough.", "I suppose."],
            "answer": "It is what it is."
        },
        "type_3": {
            "question": "Что значит «It is what it is»?",
            "options": ["Это точно то, что есть", "Ничего не поделаешь / Такова жизнь", "Это неправда", "Это лучшее"],
            "answer": "Ничего не поделаешь / Такова жизнь"
        },
        "type_4": {
            "question": "Как перевести «It is what it is»?",
            "options": ["Оно есть что есть", "Что есть, то есть / Ничего не поделаешь", "Это именно так", "Оно такое"],
            "answer": "Что есть, то есть / Ничего не поделаешь"
        }
    },

    {
        "id": 43,
        "phrase": "We'll see",
        "translation": "Посмотрим / Поживём — увидим",
        "meaning": "Неопределённость или осторожный ответ",
        "example": "Do you think you'll get the job? — We'll see.",

        "type_1": {
            "question": "Тебя спрашивают: «Will you come to the party?» Ты ещё не решил. Что скажешь?",
            "options": ["We'll see.", "I'm down!", "No problem.", "Sounds good."],
            "answer": "We'll see."
        },
        "type_2": {
            "scene": "Фильм «Rocky». Тренер отвечает на вопрос о шансах на победу — без лишних обещаний:",
            "options": ["We'll see.", "I'm not gonna lie.", "It depends.", "I don't think so."],
            "answer": "We'll see."
        },
        "type_3": {
            "question": "Что значит «We'll see»?",
            "options": ["Мы увидим это сейчас", "Посмотрим / Поживём — увидим", "Мы смотрели", "Давай посмотрим фильм"],
            "answer": "Посмотрим / Поживём — увидим"
        },
        "type_4": {
            "question": "Как перевести «We'll see»?",
            "options": ["Мы будем смотреть", "Посмотрим / Поживём — увидим", "Увидим скоро", "Нам покажут"],
            "answer": "Посмотрим / Поживём — увидим"
        }
    },

    {
        "id": 44,
        "phrase": "Let me know",
        "translation": "Дай мне знать / Сообщи",
        "meaning": "Просьба сообщить информацию позже",
        "example": "Let me know if you need help.",

        "type_1": {
            "question": "Друг думает, идти ли на вечеринку. Ты хочешь, чтобы он сообщил о решении. Что скажешь?",
            "options": ["Let me know!", "I'm down.", "No problem.", "Go for it."],
            "answer": "Let me know!"
        },
        "type_2": {
            "scene": "Сериал «Suits». Харви заканчивает встречу и просит клиента связаться, если что-то изменится:",
            "options": ["Let me know.", "Keep me posted.", "We'll see.", "I'm not sure."],
            "answer": "Let me know."
        },
        "type_3": {
            "question": "Что значит «Let me know»?",
            "options": ["Позволь мне знать всё", "Дай мне знать / Сообщи", "Я знаю это", "Ты знаешь меня"],
            "answer": "Дай мне знать / Сообщи"
        },
        "type_4": {
            "question": "Как перевести «Let me know»?",
            "options": ["Позволь мне знать", "Дай мне знать / Сообщи", "Дай мне всё", "Скажи это всем"],
            "answer": "Дай мне знать / Сообщи"
        }
    },

    {
        "id": 45,
        "phrase": "Keep me posted",
        "translation": "Держи меня в курсе",
        "meaning": "Просьба регулярно обновлять информацию",
        "example": "I'm going on a date tonight. — Oooh, keep me posted!",

        "type_1": {
            "question": "Друг ждёт результатов собеседования. Ты хочешь знать, как пройдёт. Что скажешь?",
            "options": ["Keep me posted!", "Let me know.", "We'll see.", "No worries."],
            "answer": "Keep me posted!"
        },
        "type_2": {
            "scene": "Сериал «The Good Place». Персонаж уходит с важного задания — друзья просят рассказывать о ходе дел:",
            "options": ["Keep me posted.", "Let me know.", "Sounds like a plan.", "Go for it."],
            "answer": "Keep me posted."
        },
        "type_3": {
            "question": "Что значит «Keep me posted»?",
            "options": ["Пиши мне посты", "Держи меня в курсе", "Отправь мне письмо", "Держи меня рядом"],
            "answer": "Держи меня в курсе"
        },
        "type_4": {
            "question": "Как перевести «Keep me posted»?",
            "options": ["Держи меня отправленным", "Держи меня в курсе", "Напиши мне пост", "Следи за мной"],
            "answer": "Держи меня в курсе"
        }
    },

    {
        "id": 46,
        "phrase": "Sounds like a plan",
        "translation": "Звучит как план / Договорились",
        "meaning": "Одобрение предложенного плана",
        "example": "Let's meet at 7, grab dinner and then go to the concert. — Sounds like a plan!",

        "type_1": {
            "question": "Друг предлагает план на выходные — пляж, барбекю, кино. Тебе всё нравится. Что скажешь?",
            "options": ["Sounds like a plan!", "I'm not sure.", "We'll see.", "I don't think so."],
            "answer": "Sounds like a plan!"
        },
        "type_2": {
            "scene": "Сериал «Community». Группа обсуждает стратегию перед экзаменом — все соглашаются с предложением Джеффа:",
            "options": ["Sounds like a plan!", "Deal.", "Sounds good.", "Works for me."],
            "answer": "Sounds like a plan!"
        },
        "type_3": {
            "question": "Что значит «Sounds like a plan»?",
            "options": ["Это похоже на карту", "Звучит как план / Договорились", "Это звук плана", "Я слышу план"],
            "answer": "Звучит как план / Договорились"
        },
        "type_4": {
            "question": "Как перевести «Sounds like a plan»?",
            "options": ["Звучит как план (буквально)", "Звучит как план / Договорились", "Слышу про план", "Похоже на что-то"],
            "answer": "Звучит как план / Договорились"
        }
    },

    {
        "id": 47,
        "phrase": "Why not",
        "translation": "Почему нет / А почему бы и нет",
        "meaning": "Лёгкое согласие без особых причин",
        "example": "Want to try sushi? — Why not!",

        "type_1": {
            "question": "Друг предлагает попробовать новый ресторан. Ты не против. Что скажешь?",
            "options": ["Why not!", "I don't think so.", "I'm not sure.", "No way."],
            "answer": "Why not!"
        },
        "type_2": {
            "scene": "Фильм «Yes Man». Главный герой соглашается на очередное неожиданное предложение лёгким ответом:",
            "options": ["Why not!", "I'm down.", "Deal.", "Fair enough."],
            "answer": "Why not!"
        },
        "type_3": {
            "question": "Что значит «Why not»?",
            "options": ["Почему нельзя?", "Почему нет / А почему бы и нет", "Зачем нет?", "Почему это не так?"],
            "answer": "Почему нет / А почему бы и нет"
        },
        "type_4": {
            "question": "Как перевести «Why not»?",
            "options": ["Почему не", "Почему нет / А почему бы и нет", "Зачем нет", "Не почему"],
            "answer": "Почему нет / А почему бы и нет"
        }
    },

    {
        "id": 48,
        "phrase": "Go for it",
        "translation": "Давай / Вперёд",
        "meaning": "Подбадривание или разрешение действовать",
        "example": "Should I ask for a raise? — Go for it!",

        "type_1": {
            "question": "Друг боится прыгнуть с тарзанки. Ты хочешь его подбодрить. Что скажешь?",
            "options": ["Go for it!", "I'm not sure.", "We'll see.", "That sucks."],
            "answer": "Go for it!"
        },
        "type_2": {
            "scene": "Сериал «New Girl». Нику нравится девушка, он колеблется — друзья подталкивают его к действию:",
            "options": ["Go for it!", "It depends.", "No big deal.", "I suppose."],
            "answer": "Go for it!"
        },
        "type_3": {
            "question": "Что значит «Go for it»?",
            "options": ["Иди туда", "Давай / Вперёд / Действуй", "Беги быстрее", "Возьми это"],
            "answer": "Давай / Вперёд / Действуй"
        },
        "type_4": {
            "question": "Как перевести «Go for it»?",
            "options": ["Иди за этим", "Давай / Вперёд / Действуй", "Идти к этому", "Пойди туда"],
            "answer": "Давай / Вперёд / Действуй"
        }
    },

    {
        "id": 49,
        "phrase": "Deal",
        "translation": "По рукам / Договорились",
        "meaning": "Подтверждение сделки или договорённости",
        "example": "I'll cook if you wash the dishes. — Deal!",

        "type_1": {
            "question": "Друг предлагает: «You drive there, I'll pay for parking.» Тебе нравится. Что скажешь?",
            "options": ["Deal!", "No way.", "I don't think so.", "I'm not sure."],
            "answer": "Deal!"
        },
        "type_2": {
            "scene": "Сериал «Shark Tank». Инвестор принимает условия предпринимателя одним словом и протягивает руку:",
            "options": ["Deal!", "Sounds good.", "Works for me.", "I'm down."],
            "answer": "Deal!"
        },
        "type_3": {
            "question": "Что значит «Deal»?",
            "options": ["Сделка (в магазине)", "По рукам / Договорились", "Раздача карт", "Большая скидка"],
            "answer": "По рукам / Договорились"
        },
        "type_4": {
            "question": "Как перевести «Deal» в ответ на предложение?",
            "options": ["Сделка", "По рукам / Договорились", "Дели это", "Торгуй"],
            "answer": "По рукам / Договорились"
        }
    },

    {
        "id": 50,
        "phrase": "No way",
        "translation": "Ни за что / Не может быть!",
        "meaning": "Категорический отказ или сильное удивление",
        "example": "Did she really say that? — No way!",

        "type_1": {
            "question": "Друг предлагает прыгнуть в холодную воду в январе. Ты точно против. Что скажешь?",
            "options": ["No way!", "I'm down.", "Why not?", "Deal."],
            "answer": "No way!"
        },
        "type_2": {
            "scene": "Сериал «Friends». Джо узнаёт невероятную новость и реагирует с искренним удивлением:",
            "options": ["No way!", "That sucks.", "I'm not gonna lie.", "Fair enough."],
            "answer": "No way!"
        },
        "type_3": {
            "question": "Что значит «No way»?",
            "options": ["Нет дороги", "Ни за что / Не может быть!", "Нет выхода", "Не сюда"],
            "answer": "Ни за что / Не может быть!"
        },
        "type_4": {
            "question": "Как перевести «No way»?",
            "options": ["Нет пути", "Ни за что / Не может быть!", "Нет способа", "Никуда не иду"],
            "answer": "Ни за что / Не может быть!"
        }
    },
]

# ============================================================
#  PHRASE OF THE DAY  —  ротация для пуш-уведомлений
#  Логика: берём (day_of_year % 50) → индекс в PHRASES
# ============================================================

PUSH_TEMPLATE = (
    "🗣 <b>Фраза дня:</b> <b>{phrase}</b>\n\n"
    "💬 Значение: {translation}\n"
    "📝 Пример: <i>{example}</i>\n\n"
    "👇 Нажми, чтобы потренироваться!"
)
