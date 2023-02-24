# СПИСОК (list) - упорядоченная изменяемая коллекция объектов
# КОРТЕЖ (set) - упорядоченная неизменяемая коллекция объектов
# СЛОВАРЬ (dict) - неупорядоченное множество пар ключ/значение
# МНОЖЕСТВО (tuple) - неупорядоченный набор неповторяющихся объектов

# СПИСОК (list)
# - быстро проверить присутствие элемента в списке можно с помощью оператора in
# - рост списков может происходить в рещултате использования
# методов append, extend, insert
# - сокращение списков может происходить в результате вызова методов remove, pop
# - списки поддерживают срезы (начало, конец, шаг)

# Если список создается и заполняется объектами непосредственно
# в коде - такой список называется литеральным.
# Он создается и заполняется за один прием.

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]


# Выводим гласные буквы из заданного слова
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word = 'Металлургия'
for letter in word:
    if letter in vowels:
        print(letter)

# Выводим гласные буквы из заданного слова, без повторов
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word = 'Высокопревосходительство'
found = []
for letter in word:
    if letter in vowels: # определяем присутствие объекта в коллекции
        if letter not in found: # определяем отсутствие объекта в коллекции
            found.append(letter) # добавляем объект в список
for vowel in found:
    print(vowel)

len(found) # опредеяем кол-во объектов в списке

# Выводим гласные буквы из заданного слова, без повторов
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# Попросим ввести слово
word = input('(Введите слово для поиска гласных)\nProvide a word to search for vowels: ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

# append() -  добавляем объект в список
nums = [1, 2, 3, 4]
nums.append(2)
nums
nums.append([]) # может добавлять пустой список
nums

# remove() - Удаляет первое вхождение указзаного в скобках значения из списка
nums.remove(2)
nums
nums.remove([])
nums

# pop() - удаляет из списка и возвращает объект по индексу
# Если не указать инденкс - то будет удален и возвращен последний объект в списке
nums.pop()
nums
nums.pop(2)
nums

# extend() - принимает список и добавляет его в существующий список
nums.extend([7, 8, 9])
nums

# insert( , ) - вставляет объект в список перед индексом, указанным в первом аргументе
nums.insert(1, 5)
nums

help(list) # Документация по Списку
help(list.append) # Документация по Методу Списка - append()


phrase = "Don't panic!"
# преабразуем фразу в список, который состоит из букв и символов фразы
plist = list(phrase)
print(phrase)
print(plist)


# ---
# Трансформируем обратно в строку
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

# трансформируем "Don't panic!" в строку "on tap"
# этот цикл извлекает 4 объекта из plist, удаляя из строки "nic!"
for i in range(4):
    plist.pop()
# удаляем первую букву
plist.pop(0)
# удаляем по значению - апостроф
plist.remove("'")
# извлекаем по очереди 2 крайних символа и снова вставляем в plist
# таким образом мы поменяли местами 2 крайних символа
plist.extend([plist.pop(), plist.pop()])
# снова извлекаем plist.pop(3)- а затем вставляем пробел перед элементом с индексом 2
plist.insert(2, plist.pop(3))

new_phrase2 = ''.join(plist)
print(plist)
print(new_phrase2)


# ---
# Копирование объектов и ссылки на объекты
first = [1, 2, 3, 4, 5]
first
second = first
second
# добавим во второй список еще один элемент
second.append(6)
second
first
# first тоже ПОМЕНЯЛСЯ, ПОТОМУ ЧТО оператор присваивания не копирует объект,
# а записывает ссылку на сам объект. Поэтому при изменении одного объекта -
# меняется и другой объект

# чтобы скопировать используем метод copy
third = second.copy()
third
third.append(7)
third
second


# ---
# Python позволяет обращаться к элементам списка как с начало (положительный индекс)
# так и с конца (отрицательный индекс)
saying = "Don't panic!"
letters = list(saying)
letters
letters[0] # = D
letters[3] # = '
letters[6] # = p
letters[-1] # = !
letters[-3] # = i

# в списках можно использовать [начало:конец:шаг]
letters[0:10:3] # каждая 3 буква до (но не включая) индекса 10
letters[3:] # пропустить первые 3 буквы и вернуть остальные
letters[:10] # все буквы до (но не включая) индекса 10
letters[::2] # каждая вторая буква
letters[-4:-1] # можно использовать отрицательные индексы
letters[::-1] # отрицательный индекс шага - перевернет строку

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
booklist
# превращаем список в строку с помощью ''join()
''.join(booklist[0:3])
''.join(booklist[-6:])

backwards = booklist[::-1]
''.join(backwards)

every_other = booklist[::2]
''.join(every_other)

# таким образом можно использовать СРЕЗы списка
''.join(booklist[4:14])
''.join(booklist[13:3:-1])

# преобразуем программу panic.py с помощью СРЕЗов
phrase = "Don't panic!"
# преабразуем фразу в список, который состоит из букв и символов фразы
plist = list(phrase)
print(phrase)
print(plist)

# трансформируем "Don't panic!" в строку "on tap"
# берем срез с нужными буквами
plist[1:3] # = [o, n]
plist[5] # = пробел
plist[4] # = [t]
plist[-5:-7:-1] # = [a, p]
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[-5], plist[-6]])
print(new_phrase)


# ---
# цикл for знает все о списках - где начало, длину и конец
paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print('\t', char) # \t - добавляет табулацию перед выводом

# цикл может работать со срезами
paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char) # \t - добавляет табулацию перед выводом
print()
for char in letters[-7:]:
    print('\t'*2, char) # оператор умножения определяет сколько символов табуляции нужно поставить
print()
for char in letters[12:20]:
    print('\t'*3, char)
print()

