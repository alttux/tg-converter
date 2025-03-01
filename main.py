import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, html, F
from aiogram.filters.command import Command
from aiogram.types import  Message, FSInputFile

from env import TOKEN, INPUT_IMG, OUTPUT_IMG # Ваш Telegram token
from PIL import Image


# Включаем логирование
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


async def send_p_doc(bot: Bot, chat_id: int, file_path: str, caption: str = None):
    """
    Отправляет фото в указанный чат, используя aiogram 3.x.

    :param bot: объект бота
    :param chat_id: ID чата, куда отправлять фото
    :param file_path: Путь к файлу изображения
    :param caption: (опционально) Подпись к изображению
    """
    doc = FSInputFile(file_path)  # Создаем объект файла
    await bot.send_document(chat_id, doc, caption=caption)


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в конвертер,! Что вы хотите сделать?"
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
    img_out = Image.open(path_to_input)
    path_to_output = os.path.join(INPUT_IMG, f"{img}.jpg")
    img_out.save(path_to_output)
    await send_p_doc(
        bot, message.chat.id, path_to_output, caption="Вот ваше изображение!"
    )


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())