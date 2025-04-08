import os
from PIL import Image
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from env import OUTPUT_IMG, OUTPUT_DOC, INPUT_DOC

# Список поддерживаемых форматов
SUPPORTED_FORMATS_IMG = ['BMP', 'GIF', 'JPG', 'PNG', 'WEBP', 'ICO']

def formats_kb_img():
    """
    Создает инлайн-клавиатуру с поддерживаемыми форматами.
    """
    inline_kb_list = [
        [InlineKeyboardButton(text=format, callback_data=format.lower())] for format in SUPPORTED_FORMATS_IMG
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


async def convert_image(input_file: str, output_format: str) -> str:
    """
    Конвертирует изображение в указанный формат.

    :param input_file: Путь к входному изображению
    :param output_format: Формат выходного изображения
    :return: Путь к выходному изображению
    """
    # Открываем входное изображение
    with Image.open(input_file) as img:
        # Определяем путь для сохранения выходного изображения
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_path = os.path.join(OUTPUT_IMG, f"{base_name}.{output_format}")

        # Сохраняем изображение в новом формате
        img.save(output_path)

    return output_path

def convert_pdf_doc(input_path: str, output_path: str, input_file: str, output_file: str, formats: list) -> str:
    # Specify the PDF file location
    pdf_file = rf"{input_path}/{input_file}.pdf"

    # Specify the output DOCX file location
    docx_file = rf"{output_path}/{output_file}.docx"

    # Convert the PDF file to a DOCX file
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

    return docx_file