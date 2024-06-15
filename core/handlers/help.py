from aiogram import Bot
from aiogram.types import Message


async def get_help(message: Message, bot: Bot):
    username = message.from_user.first_name
    help_text = f'''
                    Доброго времени суток, <b>{username}</b>,\
 убидительная просьба <u>использовать кнопки</u> приведенные в боте,\
 а так же <u>следовать рекомендациям бота</u> по заполнению форм.
                '''
    await message.answer(help_text,
                         parse_mode='HTML')