from aiogram import Router, F
from aiogram.types import Message

from app.utils.db import get_cart

router = Router()


@router.message(F.text == "🛒 Корзина")
async def button_cart_handler(message: Message) -> None:
    items = get_cart(message.from_user.id)

    if not items:
        await message.answer("🛒 Ваша корзина пуста.")
        return

    total = sum(item["price"] for item in items)

    lines = ["🛒 Ваша корзина:\n"]
    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item['name']} — ${item['price']}")
    lines.append(f"\n💰 Итого: ${total}")

    await message.answer("\n".join(lines))
