# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class MakingToys:

    def __init__(self, name='demo_name', color='demo_color', toys_type='demo_toys_type'):
        self.name = name
        self.color = color
        self.toys_type = toys_type

    def purchase_of_raw_materials(self):
        print('Закупка сырья')

    def tailoring(self):
        print('Пошив')

    def coloring(self):
        print('Окраска')


toys = MakingToys()

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

toys_type = input()


class Animal(MakingToys):

    def __init__(self, name='demo_name', color='demo_color', toys_type='animal'):
        super().__init__(name, color, toys_type)


class CartoonCharacter(MakingToys):

    def __init__(self, name='demo_name', color='demo_color', toys_type='demo_toys_type'):
        super().__init__(name, color, toys_type)


if toys_type == 'animal':
    toys = Animal()
else:
    if toys_type == 'cartoon character':
        toys = CartoonCharacter()
    else:
        print('Завод данного вида игрушек не производит')
