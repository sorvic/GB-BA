"""
Напишите программу, которая принимает на вход строку, и отслеживает,
сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
"""
input_str = 'a a a b c a a d c d d'
list_1 = input_str.split()
print(list_1)
dict_1 = {}
res = ''

for i in list_1:
    if dict_1.get(i) != None:
        dict_1[i] += 1
        res += f'{i}_{dict_1[i]} '
    else:
        dict_1[i] = 0
        res += f'{i} '

print(dict_1)
print(res)

# 2-ой способ
input_str_2 = 'a a a b c a a d c d d'
input_lst = input_str_2.split()
print(input_lst)
res_2 = []

for i in range(len(input_lst)):
    x = input_lst[:i]
    print(f'{x = }')
    if x.count(input_lst[i]) == 0:
        res_2.append(input_lst[i])
    else:
        res_2.append(f'{input_lst[i]}_{x.count(input_lst[i])}')
print(res_2)

# соединяем наш список в строку через пробел
out_str = ' '.join(res_2)
print(out_str)



# -----------------------------
""" IrinaZurina code """
line = [i for i in input().split()]
letters, new_line = {}, []
for letter in set(line):
    letters.setdefault(letter, 0)
for s in line:
    if letters[s] == 0:
        new_line.append(s)
        letters[s] += 1
    else:
        new_line.append(f'{s}_{letters[s]}')
        letters[s] += 1
print(*new_line)
