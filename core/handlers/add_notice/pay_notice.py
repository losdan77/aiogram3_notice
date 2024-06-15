from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime

from core.utils.state_add_notice import StepsAddNotice

from core.keyboards.keyboard import main_keyboard
from core.dao.accouting_notice import AccoutingDAO


async def get_type_notice_pay(message: Message, state: FSMContext):
    type_text = f'''
                    Вы выбрали: <b>{message.text}</b>\n<i>Теперь введите название сервиса, который необходимо оплачивать:</i>
                '''
    await message.answer(type_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(type=message.text)
    await state.set_state(StepsAddNotice.GET_NAME)


async def get_name_notice(message: Message, state: FSMContext):
    name_text = f'''
                    Вы указали: <b>{message.text}</b>\n<i>Введите сумму для оплаты:</i>
                '''
    await message.answer(name_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(name=message.text)
    await state.set_state(StepsAddNotice.GET_PRICE)


async def get_price_notice(message: Message, state: FSMContext):
    name_text = f'''
                    Вы указали: <b>{message.text}</b>\n<i>Введите ежемесячную дату для оплаты в формате <u>ГГГГ-ММ-ДД</u>:</i>
                '''
    await message.answer(name_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(price=message.text)
    await state.set_state(StepsAddNotice.GET_DATE_PAY)


async def get_date_pay_notice(message: Message, state: FSMContext): #сделать валидацию
    date_text = f'''
                        Дата ежемесячной оплаты: <b>{message.text}</b>
                   '''
    await message.answer(date_text,
                         parse_mode='HTML')
    context_data = await state.get_data()

    type_notice = context_data['type']
    name = context_data['name']
    price = context_data['price']
    date_n = message.text
    date_time_obj = datetime.datetime.strptime(date_n, '%Y-%m-%d')

    await AccoutingDAO.add(id_type=2,
                      id_user=str(message.from_user.id),
                      text=name,
                      price=float(price),
                      date_notice=date_time_obj)

    result_text = f'''
                        <b>Вот что получилось:</b>\nТип уведомления: <i>{type_notice}</i>\nНазвание сервиса: <i>{name}</i>\nЦена: <i>{price}</i>\nДата напоминания: <i><u>{date_n}</u></i>
                   '''
    await message.answer(result_text, 
                         reply_markup=main_keyboard,
                         parse_mode='HTML')
    await message.answer('<b>Напоминание успешно добавлено</b>',
                         parse_mode='HTML')
    await state.clear()