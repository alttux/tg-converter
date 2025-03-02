import asyncio
import logging
import os
from PIL import Image
from aiogram import Bot, Dispatcher, types, html, F
from aiogram.filters.command import Command
from aiogram.types import  Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from env import TOKEN, INPUT_IMG, OUTPUT_IMG # Ваш Telegram token
from convert import send_p_doc, converter



# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


def formats_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="AVIF")],
        [InlineKeyboardButton(text="BMP")],
        [InlineKeyboardButton(text="GIF")],
        [InlineKeyboardButton(text="JPG")],
        [InlineKeyboardButton(text="PNG")],
        [InlineKeyboardButton(text="WEBP")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в конвертер! Отправьте изображение, чтобы начать"
    )

@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    img = message.photo[-1].file_id
    path_to_input = os.path.join(INPUT_IMG, f"{img}.png")
    print(path_to_input)
    await bot.download(
        message.photo[-1],
        destination=path_to_input
    )
    img_format = 'jpg'
    await converter(
        message, bot, path_to_input, img_format, INPUT_IMG, img
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())