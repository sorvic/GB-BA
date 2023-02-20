# Модуль os функция getcwd()
from os import getcwd
where_am_i = getcwd() # показывает путь, где мы сейчас находимся

# Атрибут модуля
import sys
sys.platform # позволяет узнать платформу на которой запущен код
sys.version # позволяет узнать версию python

import os
os.getcwd() # Функция - показывает путь, где мы сейчас находимся
os.environ # Атрибут - доступ (показывает) к системным переменным окружения
os.getenv('HOME') # Атрибут - доступ (показывает) конкретный атрибут из системных переменных окружения

import datetime
datetime.date.today() # Модуль-атрибут-функция - показывает тек. дату
datetime.date.today().day # Модуль-атрибутМодуля-функция-атрибутФуекции
datetime.date.today().month
datetime.date.today().year
datetime.date.isoformat(datetime.date.today()) # текущая дата в виде строки

import time
time.strftime('%I:%M') # узнаем время в заданном формате
time.strftime('%A %p') # узнаем день недели с помощью заданных спецификаторов

import html
# экранирование угловых скобок в html коде
html.escape("This is <script>script</script>")
# позовляет вернуть экранированный код в оригинальный
html.unescape("This is &lt;script&gt")


# ---
# в Python есть собственный субоператор in - позволяет проверить, находится ли что-то внутри другого
# range - аргумент, определяющий число итераций
for num in range(5):
    print('Head First Rocks!')
# цикл for подкходит когда известно число итерация
# while - когда нам не известно число итераций


# ---
# Функции для коммандной строки
# dir() - показывает все атрибуты объекта, включая модули
import random
dir(random)
# выводим справку по функции randint()
help(random.randint)


# ---
# range(start, stop, step) - возвращает последовательность чтсел от start до stop с шагом step
range(5) # range(0, 5)
list(range(5)) # [0, 1, 2, 3, 4]
list(range(5, 10)) # [5, 6, 7, 8, 9]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
list(range(10, 0, -2))
list(range(10, 0, 2))
list(range(99, 0, -1))