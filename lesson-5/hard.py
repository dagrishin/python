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
    print("ping - тестовый ключ")
    print('cp < file_name > - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not parameter:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), parameter)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(parameter))
    except FileExistsError:
        print('директория {} уже существует'.format(parameter))


def ping():
    print("pong")

def copy_file():
    dir_path = os.path.join(os.getcwd(), parameter)
    if os.path.exists(dir_path):
        shutil.copyfile(parameter, 'copy_{}'.format(os.path.split(parameter)[1]))
    else:
        print(f'Файла {parameter} в даной директории не существут')

def delete_file():
    dir_path = os.path.join(os.getcwd(), parameter)
    if os.path.exists(dir_path):
        confirm = input('Точно удалить файл y/n: ')
        if confirm == 'y':
            try:
                os.remove(dir_path)
                print(f'Файл {parameter} удален')
            except OSError:
                print(f'Удаление невозможно, {parameter} - у вас нет прав на удаление файла')
        else:
            print('Вы не подтвердили удаление')
    else:
        print(f'Файла {parameter} не существует')

def go_to_directory():
    if '/' in parameter:
        dir_path = parameter
    else:
        dir_path = os.path.join(os.getcwd(), parameter)
    if os.path.exists(dir_path):
        print(f'Вы перешли в {parameter}')
        os.chdir(dir_path)
        os.system(f'cd {dir}')
    else:
        print('Данной папки не существуе')

def full_path():
    print(os.getcwd(), os.listdir())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "cd": go_to_directory,
    "ls": full_path
}

try:
    parameter = sys.argv[2]
except IndexError:
    parameter = None

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
