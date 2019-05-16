# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

import re

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 1000000.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 2000000.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 3000000.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == '1':
        print(check_account(person))
    elif choice == '2':
        pattern_count = '(([0].{0,1}[0-9]+)|([1-9]{1,}[0-9]{0,}\.{0,1}[0-9]{0,}))'
        while True:
            count = input('Сумма к снятию:\n')

            if re.match(pattern_count, count) \
                    and len(re.match(pattern_count, count).group(0)) == len(count):
                print(withdraw_money(person, float(count)))
                break
            else:
                print('Некорректная сумма снятия')


def verification():
    pattern_split = '[1-9][0-9]{15}\s[0-9]{4}'

    attempts = 5
    for i in range(attempts):
        user_date = input('Введите номер карты и пин код через пробел:\n')
        if not (re.match(pattern_split, user_date)
                and len(re.match(pattern_split, user_date).group(0)) == len(user_date)):
            print('Вы ввели не коректные данные, осталось {} попытки ввода'.format(attempts - i - 1))
            continue
        else:
            card_number, pin_code = user_date.split()
            person = get_person_by_card(int(card_number))
            if not person:
                print('Номер карты введен неверно, осталось {} попытки ввода'.format(attempts - i - 1))
                continue
            else:
                if not is_pin_valid(person, int(pin_code)):
                    print('Пин код введен неверно, осталось {} попытки ввода'.format(attempts - i - 1))
                    continue
                else:
                    return person
    return False


def start():
    person = verification()
    pattern_choice = '[1-3]{1}'
    if person:
        while True:

            choice = input('Выберите пункт:\n'
                           '1. Проверить баланс\n'
                           '2. Снять деньги\n'
                           '3. Выход\n'
                           '---------------------\n'
                           'Ваш выбор:\n')
            if not (re.match(pattern_choice, choice) and len(re.match(pattern_choice, choice).group(0)) == len(
                    choice)):
                print('Такого пункта меню нет')
                continue

            if choice == '3':
                break
            process_user_choice(choice, person)
    else:
        print('Вы истратили все попытки ввода')


start()
