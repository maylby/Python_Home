# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# https://gb.ru/lessons/391161/homework

"""
Задача 44: 

В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
"""

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()