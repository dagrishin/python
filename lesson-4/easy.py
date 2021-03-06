# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_1 = [1, 2, 4, 0]

list_2 = [i*i for i in list_1]

print(list_2)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_1 = ['Абиу', 'Абрикос', 'Авокадо', 'Алиберция', 'Алыча', 'Амбарелла']
list_2 = ['Абиу', 'Айва', 'Алыча', 'Амбарелла', 'Ананас']

list_3 = [fruit for fruit in list_1 if fruit in list_2]

print(list_3)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

n = random.randint(5, 17)

list = [random.randint(-500, 500) for _ in range(n)]
print(list)

result = [i for i in list if i % 3 == 0 and i > 0 and i % 4 != 0]
print(result)
