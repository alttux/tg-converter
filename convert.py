import os
from PIL import Image
from aiogram import Bot
from aiogram.types import  Message, FSInputFile

async def send_p_doc(bot: Bot, chat_id: int, file_path: str, caption: str = None):
    """
    Отправляет фото в указанный чат.

    :param bot: объект бота
    :param chat_id: ID чата, куда отправлять фото
    :param file_path: Путь к файлу изображения
    :param caption: (опционально) Подпись к изображению
    """
    doc = FSInputFile(file_path)  # Создаем объект файла
    await bot.send_document(chat_id, doc, caption=caption)

async def converter(message: Message, bot: Bot, img_path: str, img_format: str, input_img: str, img, send_func = send_p_doc):
    """
    Конвертирует фото.

    :param message: объект сообщения 
    :param bot: объект бота
    :param img_path: путь до конвертируемого изображения
    :param img_format: формат выходного узображения 
    :param input_img:  путь до директории с конвертируемым изображением
    :param img:  имя изображения
    :param send_func: (по умолчанию: send_p_doc) функция для конвертиации изображения  
    """
    img_out = Image.open(img_path)
    path_to_output = os.path.join(input_img, f"{img}.{img_format}")
    img_out.save(path_to_output)
    await send_func(
        bot, message.chat.id, path_to_output, caption="Вот ваше изображение!"
    )