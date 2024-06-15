from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.utils.state_add_notice import StepsAddNotice

from core.keyboards.keyboard import get_type_notice_keyboard, main_keyboard


async def start_add_notice(message: Message, state: FSMContext):
    start_text = f'''
                    <b>{message.from_user.first_name}</b>, начинаем добавлять уведомление.\n<i>Выберите тип уведомления</i>:
                  '''
    await message.answer(start_text,
                         reply_markup=get_type_notice_keyboard,
                         parse_mode='HTML')
    await state.set_state(StepsAddNotice.GET_TYPE)