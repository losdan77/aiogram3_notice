from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Напоминания'
        ),
        KeyboardButton(
            text='Дни рождения'
        ),
        KeyboardButton(
            text='Оплаты'
        ),
    ],
    [
        KeyboardButton(
            text='Вывести все события'
        ),
        KeyboardButton(
            text='Удалить событие'
        ),
    ],
    [
        KeyboardButton(
            text='Добавить напоминание'
        ),
    ],
], resize_keyboard=True,
    one_time_keyboard=False,
    )

get_type_notice_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='День рождения'
        ),
    ],
    [
        KeyboardButton(
            text='Оплата'
        ),
    ],
    [
        KeyboardButton(
            text='Напоминание'
        ),
    ],
], one_time_keyboard=True,
    )