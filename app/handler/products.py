from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.keyboards.reply import categories_keyboard, products_keyboard, menu_keyboard
from app.utils.db import get_products, add_to_cart

router = Router()

CATEGORIES = {
    "📱 Телефоны": "phones",
    "🛋 Мебель": "furniture",
    "👗 Мода": "fashion",
}


class ProductBrowse(StatesGroup):
    choosing_category = State()
    choosing_product = State()


@router.message(F.text == "🛍 Товары")
async def button_products_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductBrowse.choosing_category)
    await message.answer("Выберите категорию:", reply_markup=categories_keyboard())


@router.message(ProductBrowse.choosing_category, F.text == "⬅️ Главное меню")
async def back_to_menu_from_categories(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Главное меню:", reply_markup=menu_keyboard())


@router.message(ProductBrowse.choosing_category, F.text.in_(CATEGORIES.keys()))
async def choose_category(message: Message, state: FSMContext) -> None:
    category_key = CATEGORIES[message.text]
    products = get_products(category_key)

    await state.update_data(category=category_key)
    await state.set_state(ProductBrowse.choosing_product)

    product_names = [p["name"] for p in products]
    await message.answer(
        f"Товары в категории {message.text}:",
        reply_markup=products_keyboard(product_names)
    )


@router.message(ProductBrowse.choosing_product, F.text == "⬅️ К категориям")
async def back_to_categories(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductBrowse.choosing_category)
    await message.answer("Выберите категорию:", reply_markup=categories_keyboard())


@router.message(ProductBrowse.choosing_product)
async def choose_product(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    products = get_products(data.get("category", ""))

    product = next((p for p in products if p["name"] == message.text), None)
    if not product:
        await message.answer("Товар не найден. Выберите из списка.")
        return

    add_to_cart(message.from_user.id, product)
    await message.answer(
        f"✅ Добавлено в корзину!\n\n"
        f"📦 {product['name']}\n"
        f"💰 ${product['price']}"
    )
