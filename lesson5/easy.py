# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_names = [f'dir{x}' for x in range(1, 9)]


def mk_dirs():
    for dir_name in dir_names:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)


def rm_dirs():
    for dir_name in dir_names:
        if os.path.exists(dir_name):
            os.rmdir(dir_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def ls():
    cwd = os.getcwd()
    print([name for name in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, name))])
