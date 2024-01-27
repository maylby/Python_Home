# Знакомство с языком Python (семинары)
# Урок 7. Функции высшего порядка
# https://gb.ru/lessons/391158/homework


''' Задача 1 '''
# https://autotest.gb.ru/problems/83?lesson_id=391158&_ga=2.55648939.1223630724.1705653773-1736153193.1704617193
'''
print_operation_table

Напишите функцию print_operation_table(operation, num_rows, num_columns), 
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: 
бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Пример
'''
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9


''' Задача 2 '''
# https://autotest.gb.ru/problems/82?lesson_id=391158&_ga=2.55648939.1223630724.1705653773-1736153193.1704617193
'''
Винни Пух

Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (число гласных букв) 
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, 
если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka 
в виде строки. В ответе напишите Парам пам-пам, 
если с ритмом все в порядке и Пам парам, если с ритмом не все в порядке.
Если фраза только одна, то ритм определить не получится 
и необходимо вывести: 
"Количество фраз должно быть больше одной!".

Пример
'''
# На входе:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# На выходе:
# Парам пам-пам


"""
Дополниетльные задания с семинара 7

Задача 51. 
Решение в группах

Напишите функцию same_by(characteristic, objects), которая 
проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается, то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая 
принимает объект и вычисляет его характеристику.
"""

# # Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values): # Что не так с записью фукции?
#  print('same')
# else: print('different')
      
# # Вывод:
# 'same'