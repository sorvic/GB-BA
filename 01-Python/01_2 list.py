# var = 5
# print(type)

# print(type(var) == int)
# print(isinstance(var, float))
# print(dir(var))


# СПИСКИ - list
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
# my_list.insert(1, 'Dmitriy') # Добавление (позиция, значение)
# cutted = my_list.pop # Удаление крайнего индекса
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
# print(my_list[len(my_list)-2:])
# print(my_list[::2])
# print(my_list[::-1])
# print(my_list[::-2])


# a = ['декабрь', 'январь', 'февраль']
# # a.sort()
# print(sorted(a))
# print(a)


# КОРТЕЖ - tuple
# Неизменяемые списки
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

# t = ()
# print(type(t))
#
# t = (1) # <class 'int'>
# print(type(t))
#
# t = (1,) # <class 'tuple'>
# print(type(t))
#
# t = (1, 5, 3)
# print(type(t))
#
# v = [1, 8, 9]
# print(v)
# print(type(v))
#
# v = tuple(v) # преобразование в Кортеж
# print(v)
# print(type(v))
#
# # можно записывать сразу несколько значений
# a, b = 1, 2
# a = b = 1
#
# # Распаковка кортежа
# a,b,c = v
# print(a, b, c)

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

# name = 'Ivan'
# year = 2020
# money = 20.41123213
#
# print('Пользователь:', name, 'Год:', year, 'Счет:', money)
#
# # out = 'Пользователь: %s Год: %d Счет: %f' % (name, year, money)
# # out = 'Пользователь: {:^20} Год: {} Счет: {:.3f}'.format(name, year, money)
# out = f'Пользователь: {name} Год: {year} Счет: {money:.3f}'
# print(out)


# СЛОВАРИ - dictionary
# Неупорядоченные коллекции произвольных объектов с доступом по ключу
# d = {}
# d = dict()
#
# d['q'] = 'qwerty'
# print(d)
#
# d['w'] = 'werty'
# print(d)
# # вывод значения по ключу
# print(d['q'])

dictionary = {}
dictionary = {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
    print(item)

for (k,v) in dictionary.items():
    print(k, v)


# МНОЖЕСТВА - set
# Уникальные элементы, не обязательно упорядоченные
colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red') # ничего не добавилось, потому что неуникальное значение
print(colors)
colors.add('grey') # добавляем
print(colors)
colors.remove('red') # удаляем значение (если такого значения нет - то выдает ошибку_
print(colors)
colors.discard('red') # проверяет и если значение есть - то удаляет, а если нет - не выдает ошибку
print(colors)
colors.clear() #
print(colors)

# Операции со множестовом
a = {1, 2, 3 ,5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # {1, 2, 3, 5, 8}
u = a.union(b) # {1, 2, 3, 5, 8, 13, 21} - объединение
i = a.intersection(b) # {8, 2, 5} - пересечение
di = a.difference(b) # {1, 3} - разность
dr = b.difference(a) # {13, 21}
q=a.union(b).difference((a.intersection(b))) # {1, 21, 3, 13}

bf = frozenset(a)
print(bf) # frozenset({1, 2, 3, 5, 8}) - замороженное множество, не меняется!

# list comprehension - генаратор списка
# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable (if conditional)]

# Создаем список от 1 до 100
# Старый способ
list_1 = []
for i in range(1, 100):
    list_1.append(i)
print(list_1)

# Новый способ - list comprehension
list_1 = [i for i in range(1, 100)]
print(list_1)

# Только четные - list comprehension
list_1 = [i for i in range(1, 100) if i % 2 == 0]
print(list_1)

# создаем пару каждому числу (кортежи) - list comprehension
list_1 = [(i, i) for i in range(1, 100) if i % 2 == 0]
print(list_1)

# можно прибавлять, вычитать, делить и умножать
list_1 = [i * 2 for i in range(1, 100) if i % 2 == 0]
print(list_1)
