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

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


from easy import *
from re import match
import os

def folder_contents():
    print(os.listdir(os.getcwd()))

def user_input():
    dir_name = input('Введите название папки:\n')
    dir_path = os.path.join(os.getcwd(), dir_name)
    return dir_name, dir_path

if __name__ == '__main__':
    pattern = '[1-5]$'
    #current_folder = os.getcwd()
    while True:

        choice = input('Выберите пункт:\n'
                       '1. Перейти в папку\n'
                       '2. Просмотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n'
                       '---------------------\n'
                       'Ваш выбор:\n')
        if not match(pattern, choice):
            print('Такого пункта меню нет')
            continue

        if choice == '1':
            dir_name, dir_path = user_input()
            if os.path.exists(dir_path):
                print(f'Вы перешли в {dir_name}')
                os.chdir(dir_path)
            else:
                print(f'Директория {dir_name} не существует')

        if choice == '2':
            folder_contents()

        if choice == '3':
            dir_name, dir_path = user_input()
            delete_directory(dir_name)

        if choice == '4':
            dir_name, dir_path = user_input()
            create_directory(dir_name)

        if choice == '5':
            break
