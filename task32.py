# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list_1 = [random.randint(-20, 20) for i in range(random.randrange(10, 15))]
print(*list_1)

min_num = int(input("Введите минимальное число диапазона: "))
max_num = int(input("Введите максимальное число диапазона: "))

for i in range (len(list_1)):
    if min_num <= list_1[i] <= max_num:
        print(i, end=' ')

