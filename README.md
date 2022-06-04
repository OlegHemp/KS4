feat(myfun.py): создан метод класса read_project() для считываем названия директорий из папки folder_project,
    а также файлов из каждой директории и возвращает их в виде словаря sp
    :return sp: Dict[str, List[str]]

feat(myfun.py): Создан класс StructPrj, который хранит файловую структуру проектов

feat(StructPrj): В конструктор класса добавлена по сути константа folder_project в которой храниться абсолютный путь к папке с проектами.

feat: Создан метод creat_project(self, folder), который создаёт директорию проекта, добавляет проект в словарь self.struct_prg, проверяет на дубликат директорию
        :param folder:
        :return:
feat:   Создаём  в методе creat_file пустой xml файл, если файл существует, то не перезаписываем его.
        Заносим имя в словарь struct_prg 
        :param prj: 
        :param file_name: 
        :return: 