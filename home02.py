# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)
# https://gb.ru/lessons/391153/homework


''' Разбор ДЗ на семинаре '''
# https://gb.ru/lessons/391153

''' Задание '''

# 01:35:00
''' Задача 10: 

На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.''' 

# Каждую итерацию цикла "while" нужно вводить очередной "count"
# Обозначение: решка - n0, орёл - n1
# Сравнить количество 0 (решка) и 1 (орёл), 
# Если count0 < count1, то считаем count0, 
# если count0 > count1, то считаем count1,
# Т.е., "count" <= 1/2 "n" (число монет)

# 5 -> 1 0 1 1 0
# 2

''' Варианты 1 (for) '''

# coins = [0, 1, 0, 1, 1, 0] # [] # вводимый список
# # coins = list() 
# # coins = list(input()) # проверить правильность формы записи
# # coins = list('input coins = ', ) # можно ли так записать?
# print(list(coins)) # вывод на экран введённых данных

# n0 = 0
# n1 = 0

# for i in coins:
# 	if coins[i] == 0: n0 += 1
# 	else: n1 += 1
# if n0 <= n1: print(n0)
# else: print(n1)


''' Варианты 2 (while) '''
# код не работает, на выходе выдаёт 0, разобраться

# coins = [0, 1, 0, 1, 1, 0]
# print(list(coins))
# # coins = list() 
# n = len(coins) 
# a = 0
# b = 0

# while n > 0:
# 	if coins == 0: a += 1
# 	if coins == 1: b += 1
# 	n -= 1 
# if a < b: print(a)
# else: print(b)


''' Вариант 3.1 '''
# # 01_(C-03) 00:14:30
# # Решение с семинарского занятия (Алёна Хахина)

# coins = [0, 1, 0, 1, 1, 0]
# print(f'coins = {coins}')
# # coins = []
# print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))


''' Вариант 3.2 '''
# # Изменен мной

# coins = [0, 1, 0, 1, 1, 0]
# print(f'coins = {coins}')

# if coins.count(0) < coins.count(1): print(coins.count(0))
# else: print(coins.count(1))



''' Вариант 4.1 '''
# # 01_(C-03) 00:26:30 (Александар Верзун)

# coins = [0, 1, 0, 1, 0, 0]
# print(f'coins = {coins}')

# res = [coins.count(0), coins.count(1)]
# print(min(res))



''' Вариант 4.2 '''
# # 01_(C-03) 00:27:40 (Александар Верзун)

# coins = [0, 1, 0, 1, 0, 0]
# print(coins)
# a = 0
# b = 0

# for i in coins:
# 	if i == 0: a += 1
# 	else: b += 1
# if a < b: print(a)
# else: print(b)



''' Задача 12: 

Петя и Катя – брат и сестра. 
Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. 
Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.'''

# # 4 4 -> 2 2
# # 5 6 -> 2 3

''' Вариант 1 '''

# s = int(input('Input S: ', ))
# p = int(input('Input P: ', ))
# # summa = 20
# # product = 100
# # s = int(summa)
# # p = int(product)

# # s = a + b 
# # b = s - a
# for a in range(s):
#     if p == a * (s - a):
#         b = s - a
# print(a, b)

''' Вариант 2 '''
# Код не работает, разобраться

# s = int(input('Input S: ', ))
# p = int(input('Input P: ', ))

# # x + y = s
# x = 0
# y = s - x
# if x + y == s and x * (s - x) == p: print(x, y)
# else: x += 1 


''' Вариант 3 '''
# # 01_(C-03) 00:16:30
# # Решение с семинарского занятия (Алёна Хахина)
# # "print" выдаёт ошибку

# s = int(input('Input summa S: \n')) # "\n" с переносом значения на новую строку
# p = int(input('Input product P: \n')) # "\n" с переносом значения на новую строку
# for x in range(s):
# 	for y in range(p):
# 		if s == x + y and p == x * y:
# print(f'first number = {x}, second number = {y}')
# print(x, y)


""" Вариант 4 """
# 01_(C-03) 00:23:55
# Эталонное решение задачи из автотеста

s = int(input('Input summa S: \n')) # Добавил ввод данных 
p = int(input('Input product P: \n'))

solutions = []
for i in range(1, 1001):
	for j in range(1, 1001):
		if s == i + j and p == i * j:
			solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
	print(solution[0], solution[1])


''' Задача 14:

Требуется вывести все целые степени двойки 
(т.е. числа вида 2k ), не превосходящие числа N.'''

# Вывести все целые степени числа 2, 
# (2^0, ... 2^k), где 2^k <= N 

# 10 -> 1 2 4 8


# 01:45:00

'''Задача №15. 
Общее обсуждение

Иван Васильевич пришел на рынок и решил купить два арбуза: 
один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
Но, вот, незадача, арбузов слишком много, и он не знает, 
как же выбрать самый легкий и самый тяжелый арбуз? 
Помогите ему! 
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза '''

# Input: 5 -> 5 1 6 5 9
# Output: 1 9
