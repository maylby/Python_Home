# Знакомство с языком Python (семинары)
# Урок 8. Работа с файлами
# https://gb.ru/lessons/391159/homework

'''

Задача №49. 
Решение в группах

Создать телефонный справочник с
возможностью импорта и экспорта данных в формате .txt. 
Данные, которые должны находиться в файле:
Фамилия, имя, отчество, номер телефона. 

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик 
для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной.
'''

# Иванов, Иван, 111, описание Иванова
# Петров,	Петр,	222,	описание Петрова
# Васичкина, Василиса, 333, описание Васичкиной
# Питонов, Антон, 777, умеет в Питон

"""
ДЗ по задаче из 01(С-08)

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных.
"""

'''
Функция записи, хранения и поиска данных телефоных номеров
work_with_phonebook '''

def work_with_phonebook():

    choice = show_menu() 
    
    phone_book = read_txt('phonebook.txt')

    while (choice != 8): 

        if choice == 1:
            print_result(phone_book) 

        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))

        elif choice == 4:
            last_name = input('lastname ') 
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            new_number = input('new number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            print(work_with_phonebook()) # прямой возврат в меню работы с телефонной книгой
                                         # или данное действие нужно совершать через функцию?
            print(print_menu(work_with_phonebook())) 
                                                     
        
        choice = show_menu()



''' Функция show_menu '''

def show_menu():
    print("\nВыберите наобходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти обонента по фамилии\n"
          "3. найти обонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input()) 
    return choice


""" 
Таблица данных (пример)

Таблица в программе (?) должна представлять из себя список кортежей:
[(фамилия, Иванов), (имя, Иван), (телефон, 111), (описание, друг)]

P.S.
Таблица хранения данных телефонной книги 
размещается в отдельный текстовый файл 'phonebook.txt',
где будет хранится список номеров и данные пользователей
"""

# Иванов, Иван, 111, описание Иванова

# Петров,	Петр,	222,	описание Петрова

# Васичкина, Василиса, 333, описание Васичкиной

# Питонов, Антон, 777, умеет в Питон



''' Функция read_txt'''

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', "Имя", "Телефон", "Описание"] # шапка таблицы данных

    with open(filename, 'r', encoding = 'utf-8') as phb: 

        for line in phb: # 'line' - строка таблицы, перебираемую в данных
            record = dict(zip(fields, line.split(','))) # список словарей для телефонной книги
            dict(( (фамилия, Иванов), (имя, Точка), (номер, 8928) )) # <- словари: (ключ, значение)
                                                                     # 1 строка - 1 человек
        phone_book.append(record) # список данных человека (словари)
    return phone_book # возврат списка



''' Функция write_txt'''

def write_txt(filename, phone_book): 
    
    with open(filename, 'w', encoding = 'utf-8') as phout:  
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values(): 
                s += v + ','
            phout.write(f'{s[:-1]}\n')  


work_with_phonebook()
