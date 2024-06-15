from aiogram import Bot, Dispatcher, F

from core.handlers.base import start_bot, stop_bot, import_type_notice
from core.handlers.start import get_start
from core.handlers.help import get_help
from core.handlers.error import error_message
from core.handlers.select_data import select_all, select_birthday, select_pay, select_notice
from core.handlers.add_notice.base import start_add_notice
from core.handlers.add_notice.birthday_notice import get_type_notice_birthaday, get_fio_notice, get_date_birthday
from core.handlers.add_notice.pay_notice import get_type_notice_pay, get_name_notice, get_price_notice, get_date_pay_notice
from core.handlers.add_notice.standard_notice import get_type_notice_standard, get_text_notice, get_date_standard_notice
from core.handlers.delete_data import start_delete_by_id, delete_by_id
from core.handlers.notice import check_standard_notice, check_birthday_notice, check_pay_notice

from core.utils.state_add_notice import StepsAddNotice, StepsDeleteNotice

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')


async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()


    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(check_standard_notice,
                      trigger='cron',
                      hour=7,
                      minute=0,
                      kwargs={'bot': bot})
    scheduler.add_job(check_birthday_notice,
                      trigger='cron',
                      hour=7,
                      minute=30,
                      kwargs={'bot': bot})
    scheduler.add_job(check_pay_notice,
                      trigger='cron',
                      hour=8,
                      minute=0,
                      kwargs={'bot': bot})
    scheduler.start()
    # dp.message.register(check_standard_notice,
    #                     F.text == '/test1')
    # dp.message.register(check_birthday_notice,
    #                     F.text == '/test2')
    # dp.message.register(check_pay_notice,
    #                     F.text == '/test3')

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start,
                        F.text == '/start')
    dp.message.register(get_help,
                        F.text == '/help')
    dp.message.register(import_type_notice,
                        F.text == '/import_los')
    
    dp.message.register(select_all,
                        F.text == 'Вывести все события')
    dp.message.register(select_birthday,
                        F.text == 'Дни рождения')
    dp.message.register(select_pay,
                        F.text == 'Оплаты')
    dp.message.register(select_notice,
                        F.text == 'Напоминания')
    
    dp.message.register(start_delete_by_id,
                        F.text == 'Удалить событие')
    dp.message.register(delete_by_id,
                        StepsDeleteNotice.GET_ID)
    
    dp.message.register(start_add_notice,
                        F.text == 'Добавить напоминание')

    dp.message.register(get_type_notice_birthaday,
                        F.text=='День рождения',
                        StepsAddNotice.GET_TYPE)
    dp.message.register(get_type_notice_pay,
                        F.text=='Оплата',
                        StepsAddNotice.GET_TYPE)
    dp.message.register(get_type_notice_standard,
                        F.text=='Напоминание',
                        StepsAddNotice.GET_TYPE)
    
    dp.message.register(get_fio_notice,
                        StepsAddNotice.GET_FIO)
    dp.message.register(get_date_birthday,
                        StepsAddNotice.GET_DATE_B)

    dp.message.register(get_name_notice,
                        StepsAddNotice.GET_NAME)
    dp.message.register(get_price_notice,
                        StepsAddNotice.GET_PRICE)
    dp.message.register(get_date_pay_notice,
                        StepsAddNotice.GET_DATE_PAY)

    dp.message.register(get_text_notice,
                        StepsAddNotice.GET_TEXT)
    dp.message.register(get_date_standard_notice,
                        StepsAddNotice.GET_DATE_ST)

    dp.message.register(error_message)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())