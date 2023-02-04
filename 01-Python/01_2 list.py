# var = 5
# print(type)

# print(type(var) == int)
# print(isinstance(var, float))
# print(dir(var))


# СПИСКИ

# пронумерованная, изменяемая коллекция значений
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# numbers = list(range(1, 6))  # генерим список с помощью range
# print(numbers)

# numbers[0] = 12  # замена значений
# print(numbers)

# обход списка
# for i in numbers:
#     i *= 2  # i = i * 2
#     print(i)  # 24, 4, 6, 8, 10
# print(numbers)  # [12, 2, 3, 4, 5]

# my_list = ['Ivan', 'Andrey', 'Boris', 'qwe', 'Ivan', 'a']
# my_list.append('Dmitriy') # Добавление в конец списка
# cutted = my_list.pop(0) # Удаление по Индексу
# print(my_list, cutted)
# my_list.remove('Ivan') # Удаление по значению
# print(my_list)

# print(my_list.count('a'))
# print(my_list.index('Iva'))
# print('Iva' in my_list)
# print('Ivan' in my_list)
# my_list.insert(-1, 'ASD')
# my_list.insert(0, 'ASD')
# print(my_list)

# a = [10]
# b = a.copy()
# b.append(20)
# print(id(a))
# print(id(b))
# # print(id(a) == id(b))
# print(a is b)
# print(a)
# print(b)

# my_list = [1, 2, 3, 4, 5]
# print(id(my_list))
# # my_list.reverse()
# print(list(reversed(my_list)))
# print(id(reversed(my_list)))
# print(my_list)


# СРЕЗЫ
# my_list = ['Ivan', 'Andrey', 'Boris', 'qwe', 'Ivan', 'a']  # [start:stop:step]
# print(my_list[1:4:2])
# print(my_list[1:4])
# print(my_list[:4])
# print(my_list[1:])
# print(my_list[::2])
# print(my_list[::-1])
# print(my_list[::-2])


# a = ['декабрь', 'январь', 'февраль']
# # a.sort()
# print(sorted(a))
# print(a)


# tuple
# a = ['декабрь', 'январь', 'февраль']
# b = ('декабрь', 'январь', 'февраль')
# import sys
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# name = 'AnaStaSiya PetrOvna coM'
# name2 = '50'
# data = '10,20,30,60,40,80,90,7,10'
# prices = ('10', '20', '30', '60', '40', '80', '90', '7', '10')
# print(name.count('a'))
# print(name.split(','))
# a = '; '.join(prices)
# print(a)

# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.istitle())
# print(name2.isdigit())
# letter = 'я'
# print(chr(ord(letter) - 32))


# a, b, c, *qwe = data.split(',')
# print(a, b, c, qwe)

name = 'Ivan'
year = 2020
money = 20.41123213

print('Пользователь:', name, 'Год:', year, 'Счет:', money)

# out = 'Пользователь: %s Год: %d Счет: %f' % (name, year, money)
# out = 'Пользователь: {:^20} Год: {} Счет: {:.3f}'.format(name, year, money)
out = f'Пользователь: {name} Год: {year} Счет: {money:.3f}'
print(out)
