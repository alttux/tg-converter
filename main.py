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
from convert import convert_image, formats_kb

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем хранилище состояний в памяти
storage = MemoryStorage()

# Объект бота
bot = Bot(token=TOKEN)

# Диспетчер
dp = Dispatcher(storage=storage)

# Определяем состояния
class ConversionStates(StatesGroup):
    waiting_for_input_format = State()
    waiting_for_output_format = State()
    waiting_for_image = State()

# Хэндлер на команду /img
@dp.message(Command("img"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Добро пожаловать в конвертер! Пожалуйста, выберите формат входного файла:", reply_markup=formats_kb())
    await state.set_state(ConversionStates.waiting_for_input_format)

# Хэндлер для выбора формата входного файла
@dp.callback_query(ConversionStates.waiting_for_input_format)
async def input_format_chosen(callback: CallbackQuery, state: FSMContext):
    await state.update_data(input_format=callback.data)
    await callback.message.edit_text("Выберите формат выходного файла:", reply_markup=formats_kb())
    await state.set_state(ConversionStates.waiting_for_output_format)

# Хэндлер для выбора формата выходного файла
@dp.callback_query(ConversionStates.waiting_for_output_format)
async def output_format_chosen(callback: CallbackQuery, state: FSMContext):
    await state.update_data(output_format=callback.data)
    await callback.message.edit_text("Пожалуйста, отправьте изображение для конвертации.")
    await state.set_state(ConversionStates.waiting_for_image)

# Хэндлер для получения изображения
@dp.message(ConversionStates.waiting_for_image, F.photo)
async def image_received(message: Message, state: FSMContext):
    user_data = await state.get_data()
    input_format = user_data['input_format']
    output_format = user_data['output_format']

    # Скачиваем изображение
    img = message.photo[-1].file_id
    path_to_input = f"{INPUT_IMG}/{img}.{input_format}"
    await bot.download(message.photo[-1], destination=path_to_input)

    # Конвертируем изображение
    path_to_output = await convert_image(path_to_input, output_format)

    # Отправляем пользователю конвертированное изображение
    await message.answer_document(types.FSInputFile(path_to_output), caption="Вот ваше конвертированное изображение!")

    # Сбрасываем состояние
    await state.clear()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
