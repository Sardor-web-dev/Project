from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def menu_builder(params: list[str] | None) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    if params:
        for opt in params:
            builder.button(text=opt)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def menu_keyboard() -> ReplyKeyboardMarkup:
    return menu_builder(["🛍 Товары", "💳 Дисконтная карта", "🛒 Корзина", "❓ Помощь"])


def categories_keyboard() -> ReplyKeyboardMarkup:
    return menu_builder(["📱 Телефоны", "🛋 Мебель", "👗 Мода", "⬅️ Главное меню"])


def products_keyboard(product_names: list[str]) -> ReplyKeyboardMarkup:
    return menu_builder(product_names + ["⬅️ К категориям"])

