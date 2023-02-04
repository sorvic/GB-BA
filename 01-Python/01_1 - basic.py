# Ctrl + / - команда по комментированию строки
# print('Hello world!')
# print - вывод в консоль
"""
Многострочный
комментарий
"""


# АРИФМЕТИЧЕСКИЕ ДЕЙСТВИЯ

# print(1 + 1)
# print(1 - 1)
# print(2 * 5)
# print(2 / 7)  # 0.2857142857142857

# Округление
# print(round(2 / 7))  # 0
# print(round(2 / 7, 5))  # 0.28571
# print(10 % 3) #1
# print(10 // 3) #3
# print(10 ** 3) #1000


# ЛОГИЧЕСКИЕ ДЕЙСТВИЯ

# print(10 > 20)
# print(10 < 20)
# print(10 == 20)
# >=, <=
# print(10 != 5)

# x = 10
# print(x + 1)


# ПЕРЕМЕННЫЕ

# snake_case - верно
# CamelStyle - не подходит

# speed = 50
# distance = 70
# time_car = 1
# %asd = 0
# car_1 = 0
# car_2 = 0
# car2 = 0
# car = 0

# name = input('Введите имя: ')
# print('Hello', name)
# x = 'Текст'
# print(x)

# Узнать тип переменной type()
# print(type(10))
# print(type('qwe'))
# print(type(5.6))
# print(type(True))
# print(type(False))

# Использование кавычек
# print("Hel'lo")
# print("Hello")
# print('Hello')
# print('Hel"lo')

# print('10' + str(10))
# print(int('10') + 10)
# a = 50
# b = 1
# c = -5
# print(a > b and c < 0)
# out = (a < b or c < 0) and b > 5
# print(out)

# УСЛОВИЯ

# room = 73
# do_clean = room // 10 > 7 or room % 10 == 3
# print(do_clean)
#
# user_pass = 'qwerty'
# admin_pass = 'admin'
#
# if input('Введите пароль: ') == user_pass:
#     print('Авторизован успешно!')
#     if input('Введите пароль админа: ') == admin_pass:
#         print('Вы модератор!')
#     else:
#         print('Не модератор!')
# else:
#     print('Ошибка!')
# print('code')


# color = 'red'
#
# if color == 'red':
#     print('красный')
# elif color == 'blue':
#     print('синий')
# elif color == 'white':
#     print('белый')
# elif color == 'black':
#     print('черный')
# else:
#     print('unk')
#
# print('end')


# СПИСКИ

# my_list = [10, 'qwe', 50.5, True]
# my_list[0] = 'zxc'
# print(my_list)
# print(my_list[-2])
# my_list.append(1000)
# print(my_list)
# my_str = 'text'
# my_str[0] = 'w'


#  ЦИКЛЫ

# my_list = [10, 'qwe', 50.5, True]
#
# indx = 0
# while indx < len(my_list):
#     indx += 1  # indx = indx + 1
#     print(my_list[indx])
#
# # for step_val in my_list:
# #     print(step_val)
#
# # for i in 'привет мир':
# #     print(i)

# for i in range(10):
#     if i == 5:
#         continue
#     if i == 8:
#         break
#     print(i)

# for i in range(1, 10, 2):
# print(i)
# 1
# 3
# 5
# 7
# 9

# names = ['Иван', 'Sergey', 'Petr']
# for i, name in enumerate(names, start=1):
#     print(i, name)


# РАБОТА СО СТРОКАМИ
# text = 'съешь еще этих мягких французских булок'
# print(len(text))  # 39
# print('еще' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('еще', 'ЕЩЕ'))  # съешь ЕЩЕ этих мягких французских булок

# for c in text:
#     print(c)


# СРЕЗЫ
text = 'съешь еще этих мягких французских булок'
print(text[0])  # с
print(text[1])  # ъ
print(text[len(text)-1])  # к
# длина всегда минус один, потому что индексы начинаются с нуля!
print(text[-5])  # б
print(text[:])  # съешь еще этих мягких французских булок
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь еще
print(text[6:-18])  # еще этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ъ


# ПОЛУЧЕНИЕ СПРАВКИ
# help(text.isdigit)
