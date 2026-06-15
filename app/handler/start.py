from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from app.keyboards.reply import menu_keyboard
from app.utils.db import save_user

router = Router()


class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Registration.waiting_for_name)
    await message.answer(
        "Добро пожаловать в наш онлайн-магазин!\n\nКак вас зовут?",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Registration.waiting_for_name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Registration.waiting_for_phone)
    await message.answer(f"Приятно познакомиться, {message.text}!\n\nВведите ваш номер телефона:")


@router.message(Registration.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    name = data["name"]
    phone = message.text

    save_user(message.from_user.id, name, phone)
    await state.clear()

    await message.answer(
        f"✅ Регистрация завершена!\n\nИмя: {name}\nТелефон: {phone}\n\nДобро пожаловать!",
        reply_markup=menu_keyboard()
    )
