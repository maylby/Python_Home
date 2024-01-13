""" 
Знакомство с языком Python (семинары)
Урок 3. Списки и словари """
# https://gb.ru/lessons/391154/homework


""" Задача 1 (16) """
# https://autotest.gb.ru/problems/21?lesson_id=391154&_ga=2.8891701.1648384661.1703691758-1734585693.1703049693

""" 
Требуется вычислить, сколько раз встречается 
некоторое число k в массиве list_1.
Найдите количество и выведите его. 
"""

# # Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

''' Решение:

Вариант 1 
(решение с применением метода 'count')
'''

# list_1 = [1, 2, 3, 4, 5, 3]
# k = 3

# print('list_1 =', list_1)
# print('k =', k)
# print(list_1.count(k)) # метод 'count', встроен в функционал Pyhton 


'''
Вариант 2 (алгоритмическое решение)
'''

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# print('list_1 =', list_1)
# print('k =', k)

# count = 0
# for i in list_1:
# 	if i == k: count += 1
# print(count)



""" Задача 2 (18) """
# https://autotest.gb.ru/problems/22?lesson_id=391154&_ga=2.41926050.1648384661.1703691758-1734585693.1703049693

"""
Требуется найти в массиве list_1 
самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.
"""

# # Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5


''' Решение 
(С-04; 00:17:40 - Андрей Лопатько)
'''

# n = int(input('Input quantity number: '))
# list_1 = [] # для сохранения созданного списка (массива)
# from random import randint # без "импорта" 'randint' функция не работает 
# for i in range(n):
#     list_1.append(randint(-10, 10)) # Если в промежутке (-10, 10) 
#                                     # заменить '-10' на другое число, то результат поиска 
#                                     # ближайшего числа к заданному числу 'k' 
#                                     # выдаёт ошибочные значения
# print(f'list_1 = {list_1}')

# k = int(input('k = '))

# min1 = abs(k - list_1[0]) # Функция 'abs()' возвращает абсолютное значение заданного числа: 
#                           # - Целые числа — целочисленное абсолютное значение; 
#                           # - Числа с плавающей точкой — абсолютное значение с плавающей точкой; 
#                           # - Комплексные числа — величина числа.
# result = list_1[0]
# for i in range(1, len(list_1)):
#     if (k - list_1[i]) < min1: 
#         min1 = abs(k - list_1[i])
#         result = list_1[i]
# print(result) # Как вернуть два числа, если минимумы совпадают? 
#               # Пример:
#               # list_1 = [10, 9, 2, -10, 4]
#               # k = 3
#               # 4 <- выдача || реальный результат -> 2 и 4


"""
Вариант 2

(сравнение модуля разности между элементами списка 
и заданным числом для нахождения наименьшей разницы)
https://uchet-jkh.ru/i/napisite-programmu-dlya-poiska-elementa-v-massive-blizaisego-po-velicine-k-zadannomu-cislu/ 
"""

numbers = [2, 5, 9, 12, 17]
print(f'numbers = {numbers}')
# target = 10
target = int(input('target = '))
closest = None
closest_diff = None

for number in numbers:
	diff = abs(number - target)
	if closest_diff is None or diff < closest_diff:
		closest = number
		closest_diff = diff
print(closest)




""" Задача 3 (20) """ 
# <https://autotest.gb.ru/problems/23?lesson_id=391154&_ga=2.41176354.1648384661.1703691758-1734585693.1703049693>

"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
"""
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

"""
А русские буквы оцениваются так:
"""
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

"""
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.

ПРИМЕР 

(презентация): 
"""
# Ввод: ноутбук
# Вывод: 12

""" 
(autotest): 
"""
# k = 'ноутбук'
# 12

""" 
Алгоритм решения задачи:

Поименовать каждый список с буквами 
(l_Rus01, l_Rus02 или l_En01, l_En02 и т.д.).
Присвоить численные значения (очки) буквам каждого списка 
(l_Rus01 = 1 или l_En01 = 1 и т.д.), т.е.
(???) n[i] = 1, либо n[i] = i + 1 - i 
Задать некое слово, например "ноутбук"
и перебором вычислить сумму значений всех букв слова.
Вывести слово и результат суммирования. 


Решение:

Вариант 1 (???)
"""
# A = E = I = O = U = L = N = S = T = R = 1
# l_En1 = A, E, I, O, U, L, N, S, T, R

# print(l_En1)

# word = ('lines')
# w = word.upper()
# result = 0

# for i in l_En1: 
#     if w in l_En1:  # Как перебрать знаки "word" в "l_En1"?
#                     # И посчитать сумму значений?
#         result += i
# print(result) # выведение 'i' при каждой итерации цикла


""" 
Вариант 2 
"""
# w = input('Input word: ')
# # word = 'ноутбук' # проверить правильность написания
# word = w.upper() # Метод upper() возращает копию строки, 
#                  # в которой все буквы сконвертированы 
#                  # к большому регистру (заглавные буквы)
# dict_rus = {'АВЕИНОРСТ' : 1,
# 	        'ДКЛМПУ' : 2,
# 	        'БГЁЬЯ' : 3,
# 	        'ЙЫ' : 4,
# 	        'ЖЗХЦЧ' : 5,
# 	        'ШЭЮ' : 8,
# 	        'ФЩЪ' : 10}
# dict_en = {'AEIOULNSTR' : 1,
# 		   'DG' : 2,
# 		   'BCMP' : 3,
# 		   'FHVWY' : 4,
# 		   'K' : 5,
# 		   'JX' : 8,
# 		   'QZ' : 10}
# result = 0
# for i in word:
# 	for simbols, count in dict_rus.items() | dict_en.items(): 
# 		                            # items() - это метод словарей в Python, 
# 	                                # возвращает итерируемый объект (DictView) 
# 		                            # для получения пары "ключ-значение" словаря.
# 		if i in simbols: result += count
# print(result)