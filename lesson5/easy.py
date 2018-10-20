# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import path
import os

dir_names = [f'dir{x}' for x in range(1, 9)]


def mk_dirs():
    for dir_name in dir_names:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


def rm_dirs():
    for dir_name in dir_names:
        if os.path.exists(dir_name):
            os.removedirs(dir_name)
