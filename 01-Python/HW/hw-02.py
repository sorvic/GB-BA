"""
Найдите сумму цифр трехзначного числа
123 -> 6
100 -> 1
"""

# способ через перебор строки
print('1-й способ')
num = input('Введите трехзначное число: ')
sum = 0

for i in num:
    sum += int(i)

print(sum)

# способ через деление
print('2-й способ')
num = int(input('Введите трехзначное число: '))
n = 0
sum = num % 10 + num % 100 // 10 + num % 1000 // 100
print(sum)

""" teacher's comment
старайся не использовать имена встроенных функций для
именования своих переменных (sum)

Можно добавить проверку, что число 3-значное.
"""