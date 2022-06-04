import os
from typing import Dict, List


class StructPrg:
    def __init__(self):
        self.folder_project = os.getcwd() + '\\project'
        self.struct_prg = self.read_project()

    def read_project(self):
        """
        Считываем названия директорий из папки self.folder_project,
        а также файлов из каждой директории и выдаём их в виде словаря sp
        :return sp: Dict[str, List[str]]
        """
        files = os.listdir(self.folder_project)
        sp: Dict[str, List[str]] = {}
        for dir_name in files:
            file = os.listdir(f"{self.folder_project}\\{dir_name}")
            sp[dir_name] = file
        return sp

    def creat_project(self, folder):
        """
        Создаёт директорию проекта, добавляет проект в словарь self.struct_prg, проверяет на дубликат директорию
        :param folder:
        :return:
        """
        try:
            os.mkdir(f"{self.folder_project}\\{folder}")
        except FileExistsError as e:
            print(e)
        else:
            self.struct_prg[folder] = []

    def creat_file(self, prj, file_name):
        """
        Создаём пустой xml файл, если файл существует, то не перезаписываем его.
        Заносим имя в словарь struct_prg
        :param prj:
        :param file_name:
        :return:
        """
        try:
            f = open(f"{self.folder_project}\\{prj}\\{file_name}.xml", 'x')
        except FileExistsError as e:
            print(e)
        else:
            f.close()
            self.struct_prg[prj].append(file_name + ".xml")


def del_file(fp, prj):
    pass


def del_project(fp, prj):
    pass
