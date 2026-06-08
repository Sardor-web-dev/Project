from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("custom"))
async def command_custom_handler(message: Message) -> None:
    await message.answer("Это кастомная функция")