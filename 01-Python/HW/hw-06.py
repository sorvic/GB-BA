"""
Задача 6
Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным
номером, где сумма первых трех цифр равна сумме последних
трех. Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

# способ через перебор строки и срезы
print('1-й способ')
ticket = input('Введите номер билета: ')
sum1 = 0
sum2 = 0

for i in ticket[0:3]:
    sum1 += int(i)

for i in ticket[3:7]:
    sum2 += int(i)

if sum1 == sum2:
    print('yes')
else:
    print('no')

# способ через деление
print('2-й способ')
ticket = int(input('Введите номер билета: '))

num1 = ticket // 1000
sum1 = num1 % 10 + num1 % 100 // 10 + num1 % 1000 // 100

num2 = ticket % 1000
sum2 = num2 % 10 + num2 % 100 // 10 + num2 % 1000 // 100

if sum1 == sum2:
    print('yes')
else:
    print('no')

""" teacher's comment
Можно еще добавить условие, что номер билета 6-значный.
"""


# -----------------------------
""" IrinaZurina code """
ticket_num = int(input('Введите номер билета: '))
# Блок проверки числа на шестизначность
flag = False
while not flag:
    if len(str(ticket_num)) != 6:
        flag = False
        print('Введено неправильное число')
        ticket_num = int(input('Введите номер билета: '))
    else:
        flag = True
first_sum, second_sum = 0, 0
for _ in range(3):
    second_sum += ticket_num % 10
    ticket_num //= 10
for _ in range(3):
    first_sum += ticket_num % 10
    ticket_num //= 10

if first_sum == second_sum:
    print('Билет счастливый!')
else:
    print('Билет несчастливый...')