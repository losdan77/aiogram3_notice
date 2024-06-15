from aiogram import Bot
from aiogram.types import Message
from datetime import datetime, timezone, timedelta

from core.dao.accouting_notice import AccoutingDAO

import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = os.getenv('ADMIN_ID')

async def get_list_user_id():
    list_user_id = []
    dict_user_id = await AccoutingDAO.select_all_id_user()
    for values in dict_user_id:
        list_user_id.append(values['id_user'])
    list_user_id = set(list_user_id)
    return list_user_id

async def check_standard_notice(bot: Bot):
    list_user_id = await get_list_user_id()
    today = datetime.now(timezone.utc).date()
    tommorow = datetime.now(timezone.utc).date() + timedelta(days=1)
    for_3_days = datetime.now(timezone.utc).date() + timedelta(days=3)
    for user_id in list_user_id:

        list_today_notice = await AccoutingDAO.select_by_id_date_standard_notice(user_id, today)
        if list_today_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания сегодня:</b>',
                               parse_mode='HTML')
            for today_notice in list_today_notice:
                await bot.send_message(str(user_id), str(today_notice['text']))
                await AccoutingDAO.delete_by_id(str(user_id), int(today_notice['id']))

        list_tommorow_notice = await AccoutingDAO.select_by_id_date_standard_notice(user_id, tommorow)
        if list_tommorow_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания завтра:</b>',
                               parse_mode='HTML')
            for tommorow_notice in list_tommorow_notice:
                await bot.send_message(str(user_id), str(tommorow_notice['text']))

        list_for_3_days_notice = await AccoutingDAO.select_by_id_date_standard_notice(user_id, for_3_days)
        if list_for_3_days_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания через 3 дня:</b>',
                               parse_mode='HTML')
            for for_3_days_notice in list_for_3_days_notice:
                await bot.send_message(str(user_id), str(for_3_days_notice['text']))


async def check_birthday_notice(bot: Bot):
    list_user_id = await get_list_user_id()
    today = str(datetime.now(timezone.utc).date())[-5:]
    tommorow = str(datetime.now(timezone.utc).date() + timedelta(days=1))[-5:]
    for_3_days = str(datetime.now(timezone.utc).date() + timedelta(days=3))[-5:]
    for user_id in list_user_id:

        list_today_notice = await AccoutingDAO.select_by_id_date_birthday_notice(user_id, today)
        if list_today_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Дни рождения сегодня:</b>',
                               parse_mode='HTML')
            for today_notice in list_today_notice:
                age = int(str(datetime.now(timezone.utc).date())[:4]) - int(str(today_notice['date_birthday'])[:4])
                await bot.send_message(str(user_id), f'{str(today_notice["text"])} - {age}')

        list_tommorow_notice = await AccoutingDAO.select_by_id_date_birthday_notice(user_id, tommorow)
        if list_tommorow_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Дни рождения завтра:</b>',
                               parse_mode='HTML')
            for tommorow_notice in list_tommorow_notice:
                age = int(str(datetime.now(timezone.utc).date())[:4]) - int(str(tommorow_notice['date_birthday'])[:4])
                await bot.send_message(str(user_id), f'{str(tommorow_notice["text"])} - {age}')

        list_for_3_days_notice = await AccoutingDAO.select_by_id_date_birthday_notice(user_id, for_3_days)
        if list_for_3_days_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Дни рождения через 3 дня:</b>',
                               parse_mode='HTML')
            for for_3_days_notice in list_for_3_days_notice:
                age = int(str(datetime.now(timezone.utc).date())[:4]) - int(str(for_3_days_notice['date_birthday'])[:4])
                await bot.send_message(str(user_id), f'{str(for_3_days_notice["text"])} - {age}')


async def check_pay_notice(bot: Bot):
    list_user_id = await get_list_user_id()
    today = str(datetime.now(timezone.utc).date())[-2:]
    tommorow = str(datetime.now(timezone.utc).date() + timedelta(days=1))[-2:]
    for_3_days = str(datetime.now(timezone.utc).date() + timedelta(days=3))[-2:]
    for user_id in list_user_id:

        list_today_notice = await AccoutingDAO.select_by_id_date_pay_notice(user_id, today)
        if list_today_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания сегодня:</b>',
                               parse_mode='HTML')
            for today_notice in list_today_notice:
                await bot.send_message(str(user_id), f'{str(today_notice["text"])} - {today_notice["price"]}руб.')

        list_tommorow_notice = await AccoutingDAO.select_by_id_date_pay_notice(user_id, tommorow)
        if list_tommorow_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания завтра:</b>',
                               parse_mode='HTML')
            for tommorow_notice in list_tommorow_notice:
                await bot.send_message(str(user_id), f'{str(tommorow_notice["text"])} - {tommorow_notice["price"]}руб.')

        list_for_3_days_notice = await AccoutingDAO.select_by_id_date_pay_notice(user_id, for_3_days)
        if list_for_3_days_notice==[]:
            pass
        else:
            await bot.send_message(str(user_id), 
                               '<b>Напоминания через 3 дня:</b>',
                               parse_mode='HTML')
            for for_3_days_notice in list_for_3_days_notice:
                await bot.send_message(str(user_id), f'{str(tommorow_notice["text"])} - {for_3_days_notice["price"]}руб.')