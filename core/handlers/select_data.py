from aiogram import Bot
from aiogram.types import Message

from core.dao.accouting_notice import AccoutingDAO

async def select_all(message: Message, bot: Bot):
    user_id = str(message.from_user.id)
    result = await AccoutingDAO.select_by_id(user_id)

    await message.answer('<b>Дни рождения:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==1:
            select_all_text = f'#{line["id"]}\n<u>{line["date_birthday"]}</u> день рождения у:\n<i>{line["text"]}</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')

    await message.answer('<b>Оплата:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==2:
            select_all_text = f'#{line["id"]}\n<u>{line["date_notice"]}</u> необходимо оплатить:\n<i>{line["text"]}</i> - <i>{line["price"]}руб.</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')

    await message.answer('<b>Напоминания:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==3:
            select_all_text = f'#{line["id"]}\n<u>{line["date_notice"]}</u> необходимо сделать:\n<i>{line["text"]}</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')


async def select_birthday(message: Message, bot: Bot):
    user_id = str(message.from_user.id)
    result = await AccoutingDAO.select_by_id_type(user_id, 1)
    
    await message.answer('<b>Дни рождения:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==1:
            select_all_text = f'#{line["id"]}\n<u>{line["date_birthday"]}</u> день рождения у:\n<i>{line["text"]}</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')


async def select_pay(message: Message, bot: Bot):
    user_id = str(message.from_user.id)
    result = await AccoutingDAO.select_by_id_type(user_id, 2)

    await message.answer('<b>Оплата:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==2:
            select_all_text = f'#{line["id"]}\n<u>{line["date_notice"]}</u> необходимо оплатить:\n<i>{line["text"]}</i> - <i>{line["price"]}руб.</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')


async def select_notice(message: Message, bot: Bot):
    user_id = str(message.from_user.id)
    result = await AccoutingDAO.select_by_id_type(user_id, 3)

    await message.answer('<b>Напоминания:</b>', parse_mode='HTML')
    for line in result:
        if line['id_type']==3:
            select_all_text = f'#{line["id"]}\n<u>{line["date_notice"]}</u> необходимо сделать:\n<i>{line["text"]}</i>'
            await message.answer(str(select_all_text), parse_mode='HTML')

        