from aiogram import Bot
from aiogram.types import Message, BotCommand, BotCommandScopeDefault, FSInputFile
from aiogram.enums import parse_mode

from core.dao.type_notice import TypeDAO

import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = os.getenv('ADMIN_ID')

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start',
                   description='Начало работы'),
        BotCommand(command='help',
                   description='Помощь с ботом'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, 'Бот запущен!',
                           parse_mode='HTML')


async def stop_bot(bot: Bot):
    users_info = FSInputFile(path=r'./users.txt')
    await bot.send_document(ADMIN_ID, document=users_info)
    await bot.send_message(ADMIN_ID, 'Бот остановлен!')


async def import_type_notice(message: Message, bot: Bot):
    if int(message.from_user.id) == int(ADMIN_ID):
        try:
            await TypeDAO.add(id=1, name='День рождения')
            await TypeDAO.add(id=2, name='Оплата')
            await TypeDAO.add(id=3, name='Напоминание')
            await bot.send_message(ADMIN_ID, 'Типы напоминаний успешно вставленны!')
        except:
            await bot.send_message(ADMIN_ID, 'Типы напоминаний не удалось вставить!')
    else:
        await message.answer('Ты не босс!')

