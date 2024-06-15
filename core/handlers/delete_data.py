from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.dao.accouting_notice import AccoutingDAO
from core.utils.state_add_notice import StepsDeleteNotice
from core.keyboards.keyboard import main_keyboard


async def start_delete_by_id(message: Message, state: FSMContext):
    await message.answer('Введите <b>номер напоминания</b>, которое необходимо удалить:',
                         parse_mode='HTML')
    await state.set_state(StepsDeleteNotice.GET_ID)


async def delete_by_id(message: Message, state: FSMContext):
    user_id = message.from_user.id
    id = message.text
    result_delete = await AccoutingDAO.delete_by_id(user_id, int(id))

    if result_delete:
        await message.answer(f'<b>Удалено</b>', reply_markup=main_keyboard,
                             parse_mode='HTML')
    else:
        await message.answer(f'<b>Произошла ошибка при удалении</b>', reply_markup=main_keyboard,
                             parse_mode='HTML')

    await state.clear()
