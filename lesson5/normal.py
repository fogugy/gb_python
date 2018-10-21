# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os

ACTIONS_STR = {'help': ['0', 'help', '?'], \
               'cd': ['1', 'cd'], \
               'list': ['2', 'ls', 'list'], \
               'remove': ['3', 'rm', 'remove'], \
               'mkdir': ['4', 'mkdir']}

ACTIONS_SIGNATURE = {'cd': 'cd <path>', \
                     'remove': 'rm <filename>', \
                     'mkdir': 'mkdir <dirname>'}


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


current_path = os.path.normpath(os.getcwd())


def ls():
    print('\t'.join([name for name in os.listdir(current_path)]))


def cd(rel_path):
    global current_path
    if os.path.exists(os.path.normpath(os.path.join(current_path, rel_path))):
        current_path = os.path.normpath(os.path.join(current_path, rel_path))
    else:
        raise MyError(f'Не удалось перейти по пути "{rel_path}"')
    return current_path


def mkdir(dir_name):
    try:
        os.mkdir(os.path.join(current_path, dir_name))
    except BaseException:
        raise MyError(f'Не удалось создать "{dir_name}"')


def remove(file_name):
    try:
        for root, dirs, files in os.walk(os.path.join(current_path, file_name), topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    except BaseException:
        raise MyError(f'Не удалось удалить "{file_name}"')


def get_action(action_str):
    if action_str in ACTIONS_STR['help']:
        return print_actions
    if action_str in ACTIONS_STR['list']:
        return ls
    if action_str in ACTIONS_STR['cd']:
        return cd
    if action_str in ACTIONS_STR['remove']:
        return remove
    if action_str in ACTIONS_STR['mkdir']:
        return mkdir

    return lambda: None


def get_action_signature(key):
    exmpl = ACTIONS_SIGNATURE.get(key)
    return exmpl or '<no params>'


def print_actions():
    print('Возможные действия: ')
    actions = [(k, ACTIONS_STR[k], get_action_signature(k)) for k in ACTIONS_STR.keys()]
    for k, commands, sign in actions:
        print(k, '\t[', '/ '.join(commands), ']', '  ', sign, sep='')


def do_action(input_str):
    params = input_str.split(' ')
    action = get_action(params[0])
    try:
        action(*params[1:])
    except BaseException:
        raise


def current_path_str():
    return current_path


print_actions()

while True:
    action_str = input(f'{current_path} $: ')
    try:
        do_action(action_str)
        print('')
    except BaseException as err:
        print(*err.args, sep='\n')
