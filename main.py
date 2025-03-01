import asyncio
import logging
from PIL import Image
from io import BytesIO
from aiogram import Bot, Dispatcher, types, html, F
from aiogram.filters.command import Command
from aiogram.types import InputFile, Message

from env import TOKEN, INPUT_IMG# Ваш Telegram token

# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Добро пожальвать в конвертер, {html.bold(html.quote(message.from_user.full_name))}! Что вы хотите сделать?",
        parse_mode=html
    )

@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    img_name = f"{message.photo[-1].file_id}"
    await bot.download(
        message.photo[-1],
        destination=f"{INPUT_IMG}/{img_name}.png"
    )
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())