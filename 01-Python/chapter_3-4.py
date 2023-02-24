# СПИСОК (list) - упорядоченная изменяемая коллекция объектов
# КОРТЕЖ (set) - упорядоченная неизменяемая коллекция объектов
# СЛОВАРЬ (dict) - неупорядоченное множество пар ключ/значение
# МНОЖЕСТВО (tuple) - неупорядоченный набор неповторяющихся объектов

# Словарь в словаре
# Если нам, например, надо сохранить список людей
people = {}
people['Ford'] = {
    'Name': 'Ford Prefect',
    'Gender': 'Male',
    'Occupation': 'Researcher',
    'Home Planet': 'Betelgeuse Seven'
}

people['Arthur'] = {
    'Name': 'Arthur Dent',
    'Gender': 'Male',
    'Occupation': 'Sanwich-Maker',
    'Home Planet': 'Earth'
}

people['Tricia'] = {
    'Name': 'Tricia McMillan',
    'Gender': 'Female',
    'Occupation': 'Mathematician',
    'Home Planet': 'Earth'
}

people['Robot'] = {
    'Name': 'Marvin',
    'Gender': 'Unknown',
    'Occupation': 'Paranoid Android',
    'Home Planet': 'Unknown'
}

people

# Красивый вовод сложных структур данных
# pprint (pretty print - красивый вывод)
import pprint
pprint.pprint(people)

# Использование двойных квадратных скобок для доступа к данным в сложной структуре
people['Arthur']['Occupation']