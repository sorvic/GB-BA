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
# способ с разбора
num1 = int(input('Введите трехзначное число: '))
if 99 < num1 < 1000:
    print(num1 // 100 + num1 // 10 % 10 + num1 % 10)
else:
    print('Вы ввели не 3-хзначное число')



# -----------------------------
""" IrinaZurina code """
user_num = int(input('Введите трехзначное число: '))
# Блок проверки числа на трехзначность
flag = False
while not flag:
    if user_num < 100 or user_num > 999:
        flag = False
        print('Введено неправильное число')
        user_num = int(input('Введите трехзначное число: '))
    else:
        flag = True

# Блок нахождения суммы цифр числа
sum_of_digits = 0
while user_num > 0:
    sum_of_digits += user_num % 10
    user_num //= 10
print(sum_of_digits)
