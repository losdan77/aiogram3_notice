from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import datetime

from core.utils.state_add_notice import StepsAddNotice

from core.keyboards.keyboard import get_type_notice_keyboard, main_keyboard

from core.dao.accouting_notice import AccoutingDAO


async def get_type_notice_standard(message: Message, state: FSMContext):
    type_text = f'''
                    Вы выбрали: <b>{message.text}</b>\n<i>Теперь введите текст для напоминания:</i>
                '''
    await message.answer(type_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(type=message.text)
    await state.set_state(StepsAddNotice.GET_TEXT)


async def get_text_notice(message: Message, state: FSMContext):
    notice_text = f'''
                    Вы указали: <b>{message.text}</b>\n<i>Введите дату в формате <u>ГГГГ-ММ-ДД</u>:</i>
                '''
    await message.answer(notice_text,
                         reply_markup=None,
                         parse_mode='HTML')
    await state.update_data(text=message.text)
    await state.set_state(StepsAddNotice.GET_DATE_ST)


async def get_date_standard_notice(message: Message, state: FSMContext): #сделать валидацию
    date_text = f'''
                        Дата напоминания: <b>{message.text}</b>
                   '''
    await message.answer(date_text,
                         parse_mode='HTML')
    context_data = await state.get_data()

    type_notice = context_data['type']
    text = context_data['text']
    date_n = message.text
    date_time_obj = datetime.datetime.strptime(date_n, '%Y-%m-%d')

    await AccoutingDAO.add(id_type=3,
                      id_user=str(message.from_user.id),
                      text=text,
                      date_notice=date_time_obj)

    result_text = f'''
                        <b>Вот что получилось:</b>\nТип уведомления: <i>{type_notice}</i>\nТекст: <i>{text}</i>\nДата напоминания: <i><u>{date_n}</u></i>
                   '''
    await message.answer(result_text, 
                         reply_markup=main_keyboard,
                         parse_mode='HTML')
    await message.answer('<b>Напоминание успешно добавлено</b>',
                         parse_mode='HTML')
    await state.clear()