from aiogram.fsm.state import StatesGroup, State


class StepsAddNotice(StatesGroup):
    GET_TYPE = State()
    GET_FIO = State()
    GET_NAME = State()
    GET_TEXT = State()
    GET_PRICE = State()
    GET_DATE_B = State()
    GET_DATE_PAY = State()
    GET_DATE_ST = State()


class StepsDeleteNotice(StatesGroup):
    GET_ID = State()
