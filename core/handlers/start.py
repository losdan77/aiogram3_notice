from aiogram import Bot
from aiogram.types import Message

from core.keyboards.keyboard import main_keyboard


def get_users_list():
    with open('users.txt', 'r') as f:
        return f.readlines()


def new_user(uid):
    if str(uid) + '\n' not in get_users_list():
        with open('users.txt', 'a') as f:
            f.write(str(uid) + '\n')


async def get_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    new_user(user_id)

    username = message.from_user.first_name
    hello_text = f'''
                    Привет, <b>{username}</b> Я бот в котором ты можешь настроить напоминания\
 о <u>днях рождения</u>, <u>оплате сервисов</u> и <u>простые напоминания</u>,\
 которые будут приходить тебе <u>каждое утро</u>, за <i>3 дня</i> и <i>день</i> до события,\
 а так же <i>в день</i> события.
                '''
    await message.answer(hello_text,
                         reply_markup=main_keyboard,
                         parse_mode='HTML')