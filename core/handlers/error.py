from aiogram import Bot
from aiogram.types import Message


async def error_message(message: Message, bot: Bot):
    await message.answer('Неизвестная команда')