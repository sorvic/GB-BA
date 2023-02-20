"""
Требуется вывести все целые степени двойки
(т.е. числа вида 2**k), не превосходящие числа N.

Пример:
10 -> 1 2 4 8
"""
num = int(input('Введите целое число: '))

for i in range(num):
    num_ext = 2 ** i
    if num_ext > num:
        break
    else:
        print(num_ext)
