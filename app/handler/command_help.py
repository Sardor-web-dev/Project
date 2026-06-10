from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

HELP_TEXT = """
Справка по боту

Команды:
/start — Запустить бота
/menu — Открыть главное меню
/help — Помощь по пользованию ботом

Кнопки меню:
🛍 Товары — Просмотр каталога товаров
💳 Дисконтная карта — Ваша персональная скидочная карта
❓ Помощь — Помощь


Если возникли проблемы свяжитесь с нашим админом @fksociety1
"""


@router.message(F.text == "❓ Помощь")
async def button_help_handler(message: Message) -> None:
    await message.answer(HELP_TEXT)

@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(HELP_TEXT)






