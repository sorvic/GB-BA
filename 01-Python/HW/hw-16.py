"""
Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное
число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
3

-> 1
"""
num = int(input('Введите размер массива: '))
x = int(input('Введите искомое число: '))
result = 0
list_1 = [i for i in range(1, num+1)]
print(list_1)

for i in list_1:
    if i == x:
        result += 1

print(result)

# 2-ой способ быстрый, через count + рандомный список
from random import randint
size = int(input('Введите размер списка: '))
list_2 = [randint(1, size) for _ in range(size)]
print(*list_2)
print(list_2.count(int(input('Введите искомое число: '))))

