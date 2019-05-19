import os
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_directory(name):
    dir_path = os.path.join(os.getcwd(), name)

    if os.path.exists(dir_path):
        print(f'Директория {name} уже существует')
    else:
        os.mkdir(dir_path)
        print(f'Директория {name} создана')

def delete_directory(name):
    dir_path = os.path.join(os.getcwd(), name)
    if os.path.exists(dir_path):
        try:
            os.rmdir(dir_path)
            print(f'Директория {name} удалена')
        except OSError:
            print(f'Удаление невозможно, {name} - папка не пуста')
    else:
        print(f'Директория {name} не существует')


if __name__ == '__main__':
    current_folder = os.getcwd()
    for i in range(1, 10):
        create_directory(f'dir_{i}')

    for i in range(1, 10):
        delete_directory(f'dir_{i}')
#
#
# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.
# for i in os.listdir(path=os.getcwd()):
#     if os.path.isdir(os.path.join(os.getcwd(), i)):
print(tuple(i for i in os.listdir(path=os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), i))))

# # Задача-3:
# # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copyfile(__file__, 'copy_{}'.format(os.path.split(__file__)[1]))
