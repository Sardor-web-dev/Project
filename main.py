from os import getenv
from dotenv import load_dotenv

import asyncio
import logging
from app.utils.logger_config import setup_logger

from aiogram import Bot, Dispatcher

from app.handler.start import router as start_router
from app.handler.custom import router as custom_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN") or ""

setup_logger()
logger = logging.getLogger(__name__)

dp = Dispatcher()
dp.include_routers(start_router, custom_router)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.debug("Сообщение типа INFO")
    asyncio.run(main())