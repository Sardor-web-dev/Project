from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.reply import menu_keyboard

router = Router()

@router.message(Command("menu"))
async def command_menu_handler(message: Message) -> None:
    await message.answer("Выберите раздел:", reply_markup=menu_keyboard())
