from aiogram.fsm.state import StatesGroup, State


class FormStatesGroup(StatesGroup):
    fill_name = State()
    fill_age = State()
    upload_photo = State()