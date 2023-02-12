"""
Дано натуральное число A > 1. Определите, каким по счету
числом Фибоначчи оно является, то есть выведите такое
число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

# 1-й способ
num_user = int(input('Введите целое положительное число: '))
fibo_num = [0, 1]
n = fibo_num[1]

while n < num_user:
    n = fibo_num[-1] + fibo_num[-2]
    fibo_num.append(n)

if num_user in fibo_num:
    print(f'{num_user} - число Фиббоначи №{fibo_num.index(num_user) + 1}')
else:
    print(f'{num_user} - не является числом Фиббоначи')


# 2-й способ (предпочтительнее, если число большое буде
num_user = int(input('Введите целое положительное число: '))
n1, n2 = 0, 1
n_num = 2

while n2 < num_user:
    n1, n2 = n2, n1 + n2
    n_num += 1

if n2 == num_user:
    print(f'{num_user} - число Фиббоначи №{n_num}')
else:
    print(f'{num_user} - не является числом Фиббоначи')
