"""
Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов.
Определите, сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells that she sells are
sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure
that the shells are sea shore shells

Output: 13
"""
input_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# Делаем из строки список
list_str = input_str.lower().split()
print(list_str)
# Делаем Множество - значения там все уникальные и считаем затем кол-во элементов
res_str = set(list_str)
print(res_str)
print(len(res_str)) #13



# -----------------------------
""" IrinaZurina code """
words = [i.strip(' ,.?!').lower() for i in input().split()]
print(len(set(words))) # 13
