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

    choice = show_menu() # обращение к функции show_menu() /см. ниже/
                         # получение данных (выбора (?) /Сердюк/)
    phone_book = read_txt('phonebook.txt')

    while (choice != 8): # изменил 7 на 8
                         # добавить пункт 7 (Закончить работу)
                         # выфяснить, что должно быть в пункте 7?
        if choice == 1:
            print_result(phone_book) # tkinter - библиотека (скачать)
                                     # Доп. инфа для любопытных от Сердюка
                                     # визуальная часть программы
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
    choice = int(input()) # 'choice' - переменная, принимающая 
                          # значение введённое пользователем и
                          # переводящая его в цифру (в какую?)
                          # В цифру порядкового номера данного списка?  
    return choice


""" 
Таблица данных (пример)

Таблица в программе (?) должна представлять из себя список кортежей:
[(фамилия, Иванов), (имя, Иван), (телефон, 111), (описание, друг)]
"""

# Иванов, Иван, 111, описание Иванова

# Петров,	Петр,	222,	описание Петрова

# Васичкина, Василиса, 333, описание Васичкиной

# Питонов, Антон, 777, умеет в Питон



''' Функция read_txt'''

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', "Имя", "Телефон", "Описание"] # шапка таблицы данных

    with open(filename, 'r', encoding = 'utf-8') as phb: # 'with' - контекстное меню
            # 'filename' - это 'phonebook.txt' (?)       # 'open' можно прописать без 'with', но
            # нет записи: filename = 'phonebook.txt'     # тогда оператор закрывают командой.
            # 'r' - режим чтения                         # контестное меню закрытия не требует
            # 'encoding' - кодировка                     # 'open' закрывается при выходе из цикла 
            # 'utf-8' - указание кодировки               # в Pyhton цикл определяют отступы,
            # при использовании кирилицы,                # пока мы внутри отступа, мы в цикле
            # обязательно указывать кодировку            # выход левее его границы - выход из цикла
            # 'as phb' - открываем переменную,           
            # где записан наш файл .txt
            # имя переменной произвольное 
            # (phb, x, file_1 и пр.)

        for line in phb: # 'line' - строка таблицы, где записаны данные, которые мы перебираем

            record = dict(zip(fields, line.split(','))) # создаём словари, которые составят
                    # 'zip()' - функция высшего порядка # список для телефонной книги, т.е.
                    # 'split' делит 'fields' (таблицу)  # телефонная книга - список из словарей
                    # на отдельные строки (line)
                    # строк любое количество
            
            dict(( (фамилия, Иванов), (имя, Точка), (номер, 8928) )) # <- словари: (ключ, значение)
                                                                     # одна строка - 1 человек
                                                                     # в строке несколько словарей

        phone_book.append(record) # запись данных отдельного человека (строки, словаря) в список
    return phone_book # возврат списка



''' Функция write_txt'''

def write_txt(filename, phone_book): # функция имеет два значения (имя файла и данные)
                                     # 'filename' - этой переменной нигде нет
    with open(filename, 'w', encoding = 'utf-8') as phout:  # filename, на семинаре, обозначен, как
                                                            # 'phonebook.txt', но в коде переменная
                                                            # filename нигде не принимает строку
                                                            # в виде: filename = 'phonebook.txt'
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values(): # 'v' - значение, которое ищем в наших словарях
                                             # Код не понимает, что значит 'values',
                                             # не подсвечивает переменную
                s += v + ','
            phout.write(f'{s[:-1]}\n')  # phout.write - построчная запись
                                        # s[] - срез строки, найденой в результате перебора
                                        # [:-1] - строка без последнего элемента, без запятой
                                        # '\n' - переход на другую строку



work_with_phonebook()
