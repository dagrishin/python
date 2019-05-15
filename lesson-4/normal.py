# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

pattern_initials = '[А-Я][а-я]+|[A-Z][a-z]+'
pattern_email = '[a-z_0-9]+@[a-z0-9]+\.ru|com|org'

print('Введите имя, фамилию, email. Имя и фамилия должны иметь заглавные первые буквы. \nemail - не должен иметь заглавных букв и должен быть в формате: \nтекст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, \nпотом текст, допускаются цифры, точка, ru или org или com.')
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
email = input('Введите свой email: ')

bol = True
while bol:
    if re.match(pattern_initials, name) and len(re.match(pattern_initials, name).group(0)) == len(name):
        bol_name = False

    else:
        print('Неверно указано имя')
        name = input('Введите свое имя: ')
        bol_name = True
    if re.match(pattern_initials, surname) and len(re.match(pattern_initials, surname).group(0)) == len(surname):
        bol_surname = False
    else:
        print('Неверно указана фамилия')
        surname = input('Введите свою фамилию: ')
        bol_surname = True
    if re.match(pattern_email, email) and len(re.match(pattern_email, email).group(0)) == len(email):
        bol_email = False
    else:
        print('Неверно указан email')
        email = input('Введите свой email: ')
        bol_email = True
    bol = bol_name or bol_surname or bol_email

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

pattern = '\.{2,}'

result = re.findall(pattern, some_str)

if len(result) == 0:
    print('Более одной точки подряд не встретилось ни разу')
else:
    print('Более одной точки подряд встретилось {} раз'.format(len(result)))
