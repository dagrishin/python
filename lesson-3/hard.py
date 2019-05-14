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


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.


def damage_with_armor(person1, person2):
    return person2['damage'] / person1['armor']


def attack(person1, person2):
    if person1['health'] <= damage_with_armor(person1, person2):
        person1['health'] = 0
    else:
        person1['health'] -= damage_with_armor(person1, person2)
    return person1, person2


player = {
    'name': input('Имя игрока: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2,
}

enemy = {
    'name': input('Имя противника: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2,
}

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt

with open('{}.txt'.format(player['name']), 'w') as file:
    for key, value in player.items():
        file.write(key + ' : ' + str(value) + '\n')

with open('{}.txt'.format(enemy['name']), 'w') as file:
    for key, value in enemy.items():
        file.write(key + ' : ' + str(value) + '\n')



# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,

def creat_dict(file1, file2):
    player1 = {}
    player2 = {}
    with open(file1, 'r') as file:
        for line in file:
            if line.strip().split(' : ')[0] == 'name':
                player1[line.strip().split(' : ')[0]] = line.strip().split(' : ')[1]
            else:
                player1[line.strip().split(' : ')[0]] = float(line.strip().split(' : ')[1])

    with open(file2, 'r') as file:
        for line in file:
            if line.strip().split(' : ')[0] == 'name':
                player2[line.strip().split(' : ')[0]] = line.strip().split(' : ')[1]
            else:
                player2[line.strip().split(' : ')[0]] = float(line.strip().split(' : ')[1])

    return player1, player2

player, enemy = creat_dict('{}.txt'.format(player['name']), '{}.txt'.format(enemy['name']))

# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


while True:
    player, enemy = attack(player, enemy)
    if player['health'] == 0:
        print(enemy['name'], ' - wins!!!', enemy['health'], ' - количество оставшихся единиц здоровья')
        break
    enemy, player = attack(enemy, player)
    if enemy['health'] == 0:
        print(player['name'], ' - wins!!!', player['health'], ' - количество оставшихся единиц здоровья')
        break
