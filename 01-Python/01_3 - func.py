# user1 = ['Иван', 30]
# user2 = ['Alex', 35]

# user3 = {'name': 'Ivan', 'age': 30}
# user3['phone'] = ('+7', 898908989008)
# user3['name'] = 'qwe'
# print(user3['address'])
# print(user3.get('name'))


# print(user3.setdefault('address', 'Russia'))
# print(user3.setdefault('name', 'Russia'))

# print(user3)

# user3 = {'name': 'Ivan', 'age': 30}
# add_info = {'address': 'Russia', 'phone': [5665, 45454]}
# user3.update(add_info)
# # print(user3['phone'][1])

# # print(user3.popitem())
# # print(user3)

# print(user3.pop('qwe', 1))
# print(user3)

# for key in user3:
#     print(key)
# for value in user3.values():
#     print(value)

# for key, value in user3.items():
#     print(key, value)


# ФУНКЦИИ

# def say_hello(name):
#     print(f'hello {name}!')
#
#
# say_hello('ivan')
# say_hello()


# def average(numbers):
#     """
#     Наша функция
#     :param numbers: list of numbers
#     :return:
#     """
#     my_sum = sum(numbers)
#     count = len(numbers)
#     return my_sum / count


# avg_number = average([1, 2, 3, 4, 5])
# print(avg_number)

# my_func = average
# print(average)
# print(my_func)
# print(my_func([1, 2, 3, 4, 5]))

# x = 100

# def my_test():
#     x = 10

# my_test()
#
# print(x)


# x = 100

# def my_test():
#     global x
#     x = 10


# my_test()
# print(x)

# x = 1007


# def my_func(x):
#     x += 1
#     return x


# x = my_func(x)
# x = my_func(x)
# x = my_func(x)
# print(x)


# def my_f(name, surname='Guest'):
#     print(name, surname)

# my_f('Ivan')
# my_f('Ivan', 'Ivanov')


# def my_f(name, surname, *args):
#     print(name, surname, args)


# my_f('Ivan', 'Ivanov', 890909, 'Russia')
# my_f('Ivan', 'Ivanov', 890909)
# my_f('Ivan', 'Ivanov')


# def my_f(name, surname, age):
#     print(name, surname, age)


# my_f('Ivan', age=90, surname='Ivanov')


# def my_f(name, **person_info):
#     print(name, person_info)

# my_f('Ivan', age=90, surname='Ivanov', address='qwe')


from random import choice, seed

# print(random.random())
# print(random.randint(0, 9))
# print(random.randrange(0, 9, 3))
# print(random.randrange(0, 9, 3))
# print(random.randrange(0, 9, 3))
# print(random.randrange(0, 9, 3))
# print(random.randrange(0, 9, 3))

# my_list = ['red', 'green', 'blue']
# seed(0)
# print(choice(my_list))


# names = ['Вячеслав', 'Anton', 'Andrey']
# ages = [50, 40, 10]


# for name, age in zip(names, ages):
#     print(name, age)


data = [10, 20, 30, -10, -20, -30]


# def my_calc(x):
#     return x ** 3 + 2 / 15


# def g_zero(x):
#     return x > 0


# new = []
# for val in data:
#     new.append(my_calc(val))
# print(new)

# result = list(map(lambda x: x ** 3 + 2 / 15, data))
# print(result)

# result = list(filter(lambda x: x > 0, data))
# print(result)
# my_f = lambda x: x ** 3 + 2 / 15
# print(my_f(5))
