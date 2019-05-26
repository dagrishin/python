"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
from re import match


class NextKeg:

    def __init__(self):
        self._next_keg = []
        self.total_kegs = 90
        self.count_kegs = self.total_kegs

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_kegs > 0:
            while True:
                random_keg = random.randint(1, self.total_kegs)
                if random_keg not in self._next_keg:
                    self._next_keg.append(random_keg)
                    self.count_kegs -= 1
                    return random_keg
        else:
            raise StopIteration


class CreateCard:

    def __init__(self):
        self.card = [
            [],
            [],
            []
        ]
        self.numbers_card = 15

        for i in range(3):
            for j in range(9):
                self.card[i].append('  ')

        for i in range(3):
            line_cell_number = []
            for j in range(5):
                while True:
                    n = random.randint(0, 8)
                    if n not in line_cell_number:
                        line_cell_number.append(n)
                        while True:
                            keg_number = random.randint(1, 90)
                            if keg_number not in self.card[0] \
                                    and keg_number not in self.card[1] \
                                    and keg_number not in self.card[2]:
                                self.card[i][n] = keg_number
                                break
                        break

    def display_card(self):
        print('---'*9)
        for i in range(3):
            s = ''
            for j in range(9):
                if self.card[i][j] != '  ' and self.card[i][j] != '--' and self.card[i][j] // 10 == 0:
                    s += ' ' + str(self.card[i][j]) + '|'
                else:
                    s += str(self.card[i][j]) + '|'
            print(s)
        print('---' * 9)

    def delete_number_keg(self, keg):
        for i in range(3):
            for j in range(9):
                if self.card[i][j] == keg:
                    self.card[i][j] = '--'
                    self.numbers_card -= 1
                    return True


class Loto:

    def __init__(self):
        self._player1 = CreateCard()
        self._player2 = CreateCard()

    def _input_choice(self):
        pattern = '[1-2]$'
        choice = input('Выберите пункт:\n'
                       '1. Зачеркнуть\n'
                       '2. Продолжить\n'
                       '---------------------\n'
                       'Ваш выбор:\n')
        if not match(pattern, choice):
            print('Такого пункта меню нет')
            print('Вы проиграли')
            return -1
        else:
            return choice
    def games(self):

        kegs = NextKeg()

        for keg in kegs:
            print('Карточка компьютера')
            self._player1.display_card()

            print('Твоя карточка')
            self._player2.display_card()

            print('Из мешка достали:', keg, 'Осталось бочонков:', kegs.count_kegs)
            self._player1.delete_number_keg(keg)

            choice = self._input_choice()

            b = self._player2.delete_number_keg(keg)
            if choice == '1':
                if b != True:
                    print('Вы проиграли, у вас нет данного боченка')
                    self._player2.numbers_card = -1
            if choice == '2':
                if b == True:
                    print('Вы проиграли, у вас есть данный боченка')
                    self._player2.numbers_card = -1

            if self._player1.numbers_card == 0 or self._player2.numbers_card <= 0:
                break

        if self._player1.numbers_card == 0 or self._player2.numbers_card == -1:
            print('Компьютер бобедил')
        else:
            print('Вы победили')

        input('Нажмите ENTER')








game = Loto()

game.games()