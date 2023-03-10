"""Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
"""


# вариант с генератором списка и построчным выводом матрицы
def print_operation_table(operation, num_rows=6, num_columns=6):
    # генерируем двумерную матрицу
    matrix = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    # построчно распечатываем матрицу
    for x in range(num_rows):
        temp = []
        for y in range(num_columns):
            temp.append(str(matrix[x][y]).ljust(3))
        print(*temp)


# вариант с поэлементным выводом матрицы
def print_operation_table1(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()


print_operation_table(lambda x, y: x * y)
print()
print_operation_table1(lambda x, y: x * y)
