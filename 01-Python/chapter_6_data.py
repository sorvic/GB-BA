# В Python есть встроенные инструменты, позволяющие
# открыть, обработать и закрыть текстовый файл

# Функция open() - открывает файл
# - добавление в конце арибута 'a' - append
# позволяет дописывать данные в конец файла
# - 'w' - открыть файл для записи, если есть данные - то удаляются
# - 'x' - открыть новый файл для записи.
# Вызов завершается неудачей, если такой файл уже существует
# - 'r' - открыть файл для чтения (режим по умолчанию, можно упускать данный атрибут)
# - Есои мы открываем не текстовый файл, а например картинки иили mp3,
# то нужно открывать в двоичном виде - для этого в конце добавляем 'b'
# - 'wb' - открыть файл для записи двоичных данных
# - 'x+b' - если добавляем плюс во второй аргумент,
# то файл будет открыт в режиме для чтения и записи
todos = open('todos.txt', 'a')

# Если файла нет - то создает его

# Выведим print - но указываем аргумент 'file'
# - идентифицирующий файловый поток для записи
print('Вынести мусор', file=todos)
print('Покормить кошку', file=todos)
print('Покормить кошку', file=todos)

# закрываем файл, если не закрыть - то можно потерять все данные
todos.close()

# открываем файл, теперь уже в режиме только для чтения
tasks = open('todos.txt')
# читаем наш файл прстрочно - цикл сам заершиться как строчки закончатся
for chore in tasks:
    print(chore)
# у нас выводит пустую строку, потому что print по умолчанию добавляет
# перенос строки
# И наша строка в файле тоже заканчивается переносмо строки -
# получается 2 переноса = 2 строки
# Чтобы этого избежать пишем "print(chore, end='')"

# WITH
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
# в данном случае не надо закрывать файл,
# with управляет контекстом и сама закрывает файл

# Экранирование - escaping
# Функция escape(), заимствованная из JinJa2, экранирует переданный ей
# текст, если в нем есть спец символы html
from flask import escape
# вывод обычного текста
escape('This is a Request')
# вывод текста со спец симвалами html
escape('This is a <Request>')
# ВЫВОД: Markup('This is a &lt;Request&gt;')

# Объединение значений
names = ['Terry', 'John', 'Michael', 'Graham', 'Eric']
name = '|'.join(names)
name

# строку можно превратить в список с помощью метода split()
individuals = name.split('|')
individuals

# Если есть необходимость сгенерить разметку HTML - вспоминайте про JinJa2
# Механизм шаблонов разработан специально для создания HTML
# В теги {% и %} могут содержать любые инструкции, в том числе и цикл for
# смотри viewlog.html
# Обзор табличных тегов:
# <table> - таблица
# <th> - строка дынных в таблице
# <tr> - заголовок колонки в таблице
# <td> - ячейка таблицы