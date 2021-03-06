# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <dir_name> - клонирование директории")
    print("rm <dir_name> - удаление директории")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    try:
        new_dir_name = f'{dir_name}_copy' if not dir_name_dest else dir_name
        if not os.path.exists(dir_name):
            return
        shutil.copytree(dir_name_dest or os.getcwd(), new_dir_name)
        print('директория {} скопирована'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(new_dir_name))


def rm():
    try:
        shutil.rmtree(dir_name)
        print('директория {} удалена'.format(dir_name))
    except FileExistsError as err:
        print(err.args)


def cd():
    os.chdir(dir_name)
    print(os.getcwd())


def ls():
    print('\t'.join([name for name in os.listdir(dir_name)]))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    dir_name_dest = sys.argv[3]
except IndexError:
    dir_name_dest = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
