import os
import shutil
import time

from env import INPUT_IMG, OUTPUT_IMG

def clean_folder(folder_path):
    """Очищает указанную папку"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Удаляет файлы и ссылки
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Удаляет папки с содержимым
        except Exception as e:
            print(f"Ошибка при удалении {file_path}: {e}")

    print(f"Папка {folder_path} очищена")

if __name__ == "__main__":
    folders = [INPUT_IMG, OUTPUT_IMG]


    while True:
        for folder in folders:
            clean_folder(folder)
        time.sleep(5)
