# Знакомство с языком Python (семинары)
# Урок 4. Словари, множества и профилирование
# https://gb.ru/lessons/391155/homework


"""
Задача 1 (26)
Возведение в степень

Напишите функцию f, которая на вход принимает два числа a и b, 
и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.

Пример:
"""
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

"""
Решение

Вариант 1
"""
a = int(input('Input base: '))
b = int(input('Input exp: '))

def power(a, b):
    if b == 0: return 1
    return (a * power(a, b - 1))

print(f'{a} ** {b} = {power(a, b)}')


"""
Вариант 2
"""
def power(base, exp):
    if (exp == 1): return (base)
    if (exp != 1): return (base * power(base, exp - 1))

base = int(input("Число: "))
exp = int(input("Степень: "))

print(f'{base} в степени {exp} -> {power(base, exp)}')


"""
Задача 2 (28)
Рекурсивная сумма

Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.

Пример:
"""
# sum(2, 2)
# 4

"""
Решение
"""
a = int(input('Input A: '))
b = int(input('Input B: '))

def sum(a, b):
    if b == 0 and a > b: return a
    return (sum(a, b - 1) + 1)

print(f'sum: {sum(a, b)}')