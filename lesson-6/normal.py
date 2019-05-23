# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name='test', health=100, damage=50, armor=1.2):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _damage_with_armor(self, person2):
        return person2.damage / self.armor

    def attack(self, person2):
        if self.health <= self._damage_with_armor(person2):
            self.health = 0
        else:
            self.health -= self._damage_with_armor(person2)


class Player(Person):
    # 'name': input('Имя игрока: '),
    # 'health': 100,
    # 'damage': 50,
    # 'armor': 1.2,
    def __init__(self):
        super().__init__(name=input('Имя игрока: '))


class Enemy(Person):
    # 'name': input('Имя противника: '),
    # 'health': 100,
    # 'damage': 50,
    # 'armor': 1.2,
    def __init__(self):
        super().__init__(name=input('Имя противника: '))


player = Player()
enemy = Enemy()

while True:
    player.attack(enemy)
    if player.health == 0:
        print(enemy.name, ' - wins!!!', enemy.health, ' - количество оставшихся единиц здоровья')
        break
    enemy.attack(player)
    if enemy.health == 0:
        print(player.name, ' - wins!!!', player.health, ' - количество оставшихся единиц здоровья')
        break
