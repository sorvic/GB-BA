"""
По данному целому неотрицательному n вычислите значение
n!. N! = 1 * 2 * 3 * ... * N
(произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while
Input: 5
Output: 120
"""

def factorial(n):
    count = 1
    res = 1
    while count <= n:
        res *= count
        count +=1
    return res

num = int(input('Введите число: '))
print(f'Факториал числа {num}: {factorial(num)}')
