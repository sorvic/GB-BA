"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное
число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X

Пример:
5
1 2 3 4 5
6

-> 5
"""
list_1 = [1, 2, 3, 6, 7, 4, 9, 4, 1]
x = int(input('Введите искомое число: '))
res = 0

for i in set(list_1):
    if (i != x and i < x) or i == x:
        res = i

print(res)

""" teacher's comment
если list_1 = [3, 7, 9]
Введите искомое число: 6
3
или 7 всё-таки ближе?
Посмотри разбор домашних задач в записи 4-го семинара
"""
from random import randint
n = int(input('Введите кол-во элементов: '))
list_2 = [randint(1, n) for i in range(n)]
print(list_2)
# numbers = {1, 2, 3, 5, 9, 12}
numbers = set(list_2)
# num = 7
num = int(input('Введите искомое число: '))
dif = 0
# чтобы не бегать по условиям - добавим сразу проервку,
# что если число больше max - берем сразу max
# что если число меньше min - берем сразу min
if num > max(numbers):
    print(max(numbers))
elif num < min(numbers):
    print(min(numbers))
else:
    while True:
        if num - dif in numbers and num + dif in numbers and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in numbers:
            print(num - dif)
            break
        elif num + dif in numbers:
            print(num + dif)
            break
        else:
            dif += 1

# -----------------------------
""" IrinaZurina code """
from random import randint

size = int(input('Введите размер списка: '))
numbers = tuple(randint(1, size) for _ in range(size))
print(*numbers)
num_X = int(input('Введите искомое число: '))
mod = 0
flag = False
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num_X - mod or i == num_X + mod:
            print(i)
            flag = True
            break
    if flag:
        break
    mod += 1
