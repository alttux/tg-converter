Вот полностью оформленный `README.md` в Markdown-формате для вашего проекта Telegram-бота-конвертера изображений:

---

# 🖼️ Telegram Image Converter Bot

Телеграм-бот для конвертации изображений между различными форматами с помощью [Aiogram 3](https://docs.aiogram.dev/) и [Pillow](https://pillow.readthedocs.io/).

## 🚀 Возможности

- ✅ Поддержка форматов: **BMP**, **GIF**, **JPG**, **PNG**, **WEBP**, **ICO**
- ✅ Удобные инлайн-кнопки для выбора форматов
- ✅ Асинхронная работа через `asyncio` и `aiogram`
- ✅ Хранение состояний с помощью `FSM`

---

## 📦 Установка

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/yourusername/telegram-image-converter-bot.git
cd telegram-image-converter-bot
```

2. **Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

3. **Установите зависимости:**

```bash
pip install -r requirements.txt
```

4. **Создайте файл `env.py` со следующими переменными:**

```python
# env.py
TOKEN = "ваш_токен_бота"
INPUT_IMG = "input_img"    # Папка для загрузки входных изображений
OUTPUT_IMG = "output_img"  # Папка для сохранения выходных изображений
```

> Убедитесь, что папки `input_img` и `output_img` существуют в корне проекта!

---

## ▶️ Запуск

```bash
python main.py
```

Бот начнет работать в режиме polling.

---

## 📚 Команды бота

- `/start` — Приветственное сообщение
- `/img` — Запуск режима конвертации изображений
- `/about` — Ссылки на проект и дополнительную информацию

---

## 🧠 Как это работает?

1. Пользователь вводит `/img`
2. Бот предлагает выбрать **входной** и **выходной** формат
3. Пользователь отправляет изображение
4. Бот сохраняет его и конвертирует в нужный формат
5. Конечный результат отправляется пользователю как файл

---

## 🧱 Структура проекта

```plaintext
📁 telegram-image-converter-bot/
├── main.py               # Основная логика бота
├── convert.py            # Функции конвертации и клавиатура
├── env.py                # Конфигурация с токеном и путями
├── input_img/            # Входящие изображения
├── output_img/           # Сохранённые изображения
├── requirements.txt      # Зависимости
└── README.md             # Этот файл
```

---

## 🛠 Зависимости

- `aiogram >= 3.x`
- `pillow`

Файл `requirements.txt`:

```txt
aiogram==3.3.0
pillow
```

---

## 📎 Полезные ссылки

- Telegram канал: [@st_release](https://t.me/st_release)
- GitHub проекта: [tg-converter](https://github.com/alttux/tg-converter)

---

## ⚖️ Лицензия

Проект распространяется под лицензией **MIT**. См. файл `LICENSE`.

---
