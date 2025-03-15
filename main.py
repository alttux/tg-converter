import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from env import TOKEN, INPUT_IMG
from convert import convert_image, formats_kb_img

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем хранилище состояний в памяти
storage = MemoryStorage()

# Объект бота
bot = Bot(token=TOKEN)

# Диспетчер
dp = Dispatcher(storage=storage)

'''КЛАССЫ ДЛЯ ОПРЕДЕЛЕНИЯ СОСТОЯНИЯ'''

class ConversionStatesImg(StatesGroup):
    waiting_for_input_format = State()
    waiting_for_output_format = State()
    waiting_for_image = State()

'''
ХЕНДЛЕРЫ
'''

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в конвертер! введите команду /img для работы")

# Хэндлер на команду /img
@dp.message(Command("img"))
async def cmd_img(message: Message, state: FSMContext):
    await message.answer("Конвертер изображений. Выберете входной формат:", reply_markup=formats_kb_img())
    await state.set_state(ConversionStatesImg.waiting_for_input_format)

'''
ИЗОБРАЖЕНИЯ
'''

# Хэндлер для выбора формата входного изображения
@dp.callback_query(ConversionStatesImg.waiting_for_input_format)
async def input_format_chosen_img(callback: CallbackQuery, state: FSMContext):
    await state.update_data(input_format=callback.data)
    await callback.message.edit_text("Выберите формат выходного файла:", reply_markup=formats_kb_img())
    await state.set_state(ConversionStatesImg.waiting_for_output_format)

# Хэндлер для выбора формата выходного изображения
@dp.callback_query(ConversionStatesImg.waiting_for_output_format)
async def output_format_chosen_img(callback: CallbackQuery, state: FSMContext):
    await state.update_data(output_format=callback.data)
    await callback.message.edit_text("Пожалуйста, отправьте изображение для конвертации.")
    await state.set_state(ConversionStatesImg.waiting_for_image)

# Хэндлер для получения изображения
@dp.message(ConversionStatesImg.waiting_for_image, F.photo)
async def img_received(message: Message, state: FSMContext):
    user_data = await state.get_data()
    input_format = user_data['input_format']
    output_format = user_data['output_format']
    img = message.photo[-1].file_id
    path_to_input = f"{INPUT_IMG}/{img}.{input_format}"
    await bot.download(message.photo[-1], destination=path_to_input)
    path_to_output = await convert_image(path_to_input, output_format)
    await message.answer_document(types.FSInputFile(path_to_output), caption="Вот ваше конвертированное изображение!")
    await state.clear()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
