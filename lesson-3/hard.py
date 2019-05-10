# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

def attack(person1, person2):
    if person1['health'] <= person2['damage']:
        person1['health'] = 0
        print(person1['name'], ' - убит')
    else:
        person1['health'] -= person2['damage']
    return person1, person2


player = {
    'name': input('Имя игрока: '),
    'health': 100,
    'damage': 50,
}

enemy = {
    'name': input('Имя противника: '),
    'health': 100,
    'damage': 50,
}
player, enemy = attack(player, enemy)
