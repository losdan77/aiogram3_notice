from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime

from core.utils.state_add_notice import StepsAddNotice

from core.keyboards.keyboard import main_keyboard

from core.dao.accouting_notice import AccoutingDAO


async def get_type_notice_birthaday(message: Message, state: FSMContext):
    type_text = f'''
                    Вы выбрали: <b>{message.text}</b>\n<i>Теперь введите ФИО:</i>
                '''
    await message.answer(type_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(type=message.text)
    await state.set_state(StepsAddNotice.GET_FIO)


async def get_fio_notice(message: Message, state: FSMContext):
    fio_text = f'''
                    Вы указали: <b>{message.text}</b>\n<i>Введите дату рождения в формате <u>ГГГГ-ММ-ДД</u>:</i>
                '''
    await message.answer(fio_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(fio=message.text)
    await state.set_state(StepsAddNotice.GET_DATE_B)


async def get_date_birthday(message: Message, state: FSMContext): #сделать валидацию
    date_b_text = f'''
                        Дата рождения: <b>{message.text}</b>
                   '''
    await message.answer(date_b_text, 
                         parse_mode='HTML')
    context_data = await state.get_data()

    type_notice = context_data['type']
    fio = context_data['fio']
    date_b = message.text
    date_time_obj = datetime.datetime.strptime(date_b, '%Y-%m-%d')

    await AccoutingDAO.add(id_type=1,
                      id_user=str(message.from_user.id),
                      text=fio,
                      date_birthday=date_time_obj)

    result_text = f'''
                        <b>Вот что получилось:</b>\nТип уведомления: <i>{type_notice}</i>\nФИО: <i>{fio}</i>\nДата рождения: <i><u>{date_b}</u></i>
                   '''
    await message.answer(result_text, 
                         reply_markup=main_keyboard,
                         parse_mode='HTML')
    await message.answer('<b>Напоминание успешно добавлено</b>',
                         parse_mode='HTML')
    await state.clear()