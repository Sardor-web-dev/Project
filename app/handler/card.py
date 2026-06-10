import io
import barcode
from barcode.writer import ImageWriter

from aiogram import Router, F
from aiogram.types import Message, BufferedInputFile

router = Router()


@router.message(F.text == "💳 Дисконтная карта")
async def button_discount_card_handler(message: Message) -> None:
    user_id = str(message.from_user.id)

    Code128 = barcode.get_barcode_class("code128")
    barcode_instance = Code128(user_id, writer=ImageWriter())

    buffer = io.BytesIO()
    barcode_instance.write(buffer)
    buffer.seek(0)

    photo = BufferedInputFile(buffer.read(), filename="discount_card.png")
    await message.answer_photo(photo, caption="Баланс: 100.000")
