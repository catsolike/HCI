class File:
    def __init__(self, name, in_trash=False, is_deleted=False):
        self.name = name
        self.in_trash = in_trash
        self.is_deleted = is_deleted

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            return print(f"ErrorReadFileDeleted({self.name}")
        if self.in_trash:
            return print(f"ErrorReadFileTrashed({self.name}")
        
        print(f"Прочитали всё содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            return print(f"ErrorWriteFileDeleted({self.name}")
        if self.in_trash:
            return print(f"ErrorWriteFileTrashed({self.name}")

        print(f"Записали значение {content} в файл {self.name}")


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            return print("В корзину можно добавлять только файл")
        
        file.in_trash = True
        Trash.content.append(file)


    @staticmethod
    def clear():
        print("Очищаем корзину")

        for file in Trash.content:
            file.remove()

        Trash.content.clear()
        print("Корзина пуста")


    @staticmethod
    def restore():
        print("Восстанавливаем файлы из корзины")

        for file in Trash.content:
            file.restore_from_trash()

        Trash.content.clear()
        print("Корзина пуста")


trash = Trash()
trash.add(File('File1'))
trash.add(File('SuicideFile.exe'))
trash.add(File('DeathFile.exe'))
trash.clear()


trash.add(File('File666'))
trash.add(File('SatanaVsAliens'))
trash.add(File('GodOfWar.exe'))
trash.add(File('Fast&Furios.exe'))
trash.add(878)
trash.add("frostborne")
trash.restore()