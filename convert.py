from PIL import Image

class ImageConverter:
    def __init__(self, path):
        self.path
        try:
            self.image = Image.open(path)
        except IOError:
            print("Не удалось открыть изображение")
            self.image = None

    def convert(self, format, new_path):
        if self.image is not None:
            try:
                self.image.save(new_path, format)
                print(f"Изображение сохранено в {new_path}")
            except IOError:
                print(f"Не удалось сохранить изображение в {new_path}")
        else:
            print("Конвертация не может быть выполнена, т.к. изображение не было загружено.")
