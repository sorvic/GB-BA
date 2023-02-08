"""
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов
сделал каждый ребенок, если известно, что Петя и Сережа
сделали одинаковое количество журавликов, а Катя сделала
в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""
sum = int(input('Введите общее кол-во журавликов: '))

"""
x+x*2=s
x=s-x/2
умножаем все члены уровнения на 2
2x=2s-x
2x+x=2s
3x=2s
x=2s/3
x/2 - наше искомое (сумма Пети и Сережи)
"""
petr = int(((2 * sum) / 3 / 2) / 2)
serg = petr
kat = serg * 4
print(f'Ученики сделали журавликов:\nПетр - {petr}\nКатя - {kat}\nСергей - {serg}')

"""
Можно еще добавить условие, что введены неверные данные
- попробуй 5 журавликов.
"""