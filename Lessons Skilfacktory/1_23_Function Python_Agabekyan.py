# def say_hello():
#     print('Hello')
# def say_goodbye():
#     print('good bye')
# message = say_hello
# message()
# message = say_goodbye
# message()

# def sum(a, b):
#     return a + b
# def mult(a, b):
#     return a * b
# operation = sum
# result = operation(5, 6)
# print(result)

# operation = mult
# print(operation(5,6))

# Рекурсивная функция.
# def rec_func(x):
#     if x < 4:
#         print(x)
#         rec_func(x+1)
#         print(x)
# rec_func(1)

# # Рекурсивная функция: фактериал. (4*3*2*1)
# def facterial(x):
#     if x == 1:
#         return 1
#     return facterial(x-1)*x
# print(facterial(4))

# ДЕКОРАТОР - функция дли добовления дополнительных возможностей другой функции без изменения её ссодержимого.
# Способы декорирования: способ №1:
# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
# def my_func():
#     print('Тут основная функция')
# my = my_decor(my_func)
# my()

# Способ №2 (Более распространённый и удобный). С помощью @. Нужно будет написать имя декоратора. 
# На базе кода из варианта №1.
# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
# @my_decor     # Первое изменение. Название декоратора.
# def my_func():
#     print('Тут основная функция')
# # my = my_decor(my_func)   # Эти строки можно удалить
# # my()                     # Эти строки можно удалить
# my_func()

# Как быть, если функция должна получить данные и их обработать? (на базе кода №2)
# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
# @my_decor     # Первое изменение. Название декоратора.
# def my_func():
#     print('Тут основная функция')
# my_func()

# # Функция, которая выводит сумму чисел.
# def sum(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     print(f'sum = {res}')
# sum(1, 2, 3)
# sum (2, 4, 6, 8)

# 1. Статический вариант
# def my_func():
#     a = 1
#     b = 2
#     print(a + b)
# my_func()

# 2. Динамический вариант
# def my_func(a, b):
#     print(a + b)
# my_func(5, 10)

# 3. Возвращение результата
# def my_func(a, b):
#     result = a + b
#     return result
# c = my_func(5, 10)
# print(c)


# 15_26 Вэбинар 13.12.2023 21:44 codewars.com задачи и примеры
#staring.split(separator*, maxsplit*)
# my_str = ('Программирование в Pyton')
# print(my_str.split())

# def multiply_nums(numbers):
#     p = 1
#     for x in numbers.split(','):
#         p *= int(x)
#     return p
# print(multiply_nums('2, 3'))

# Задача. Вернуть таблицу умножения для числа, которое всегда является целым числом от 1 до 10, напр. для числа 5.
# 1 * 5 = 5
# 2 * 5 = 10 и т.д.

# def multy_table(number):
#     st = str()
#     for x in range(1, 11):
#         z = number * x
#         st += f'{x} * {number} = {z}\n'
#     return st
# print(multy_table(5)) 


# a = '2,3' # Не использовать пробел. Иначе 3 сдвинется в нижней строке.
# b = a.split(',')
# for i in b:
#     print(i)

# Задача. Изограмма - это слово, где нет повторяющихся или следующих по порядку букв. 
#Опредилить, является ли слово изограммой или нет. aba==False  abs==True

# def is_isogram(string):              # Шаг №1. Опредилить функцию.
#     string = string.lower()          # Шаг №4а Перевод букв в прописной (нижний) регистр. Встр. метод .lower()
#     for item in string:              # Шаг №3. Создание цикла.В данном случае для значений ("item") в стринг.
#         if string.count(item) > 1:   # Шаг №4. У строки есть встроенный метод .count(), 
#             return False             # который отвечает за количество элементов.
#         return True
# print(is_isogram('Abs'))              # Шаг №2. Опредилить конечную задачу функции (разбираемое слово)

# Задача. Найти наименьшее число из списка.
# def find_smallest_int(arr):
#     max = arr[0]
#     for i in range(0, len(arr)):
#         if arr[i] < max:
#             max = arr[i]
#     return max
# print(find_smallest_int([2, 345, 96, 75, 1]))

# name = 'Tom'
# def say_hi():               # Глобальная переменные.
#     print('Hello', name)
# def say_bye():
#     print('Good bye', name)
# say_hi()
# say_bye()

# def say_hi():               # Локальная переменные.
#     name = 'Tom'
#     surname = 'Johnson'
#     print('Hello', name, surname)

# def say_bye():
#     name = 'Cventin'        # Локальная переменные.
#     surname = 'Tarantino'
#     print('Good bye', name, surname)
# say_hi()
# say_bye()

# name = 'Tom'
# def say_hi():               # Глобальная переменные.
#     global name             # использование встроенного метода global
#     Surname = 'Johns'
#     name = f'{name}, Bilovich'
#     print(name)
#     print(Surname)
# say_hi()

# # nonlocal использование нелокальных переменных
# def outer():
#     x = 'Локальная переменная'
#     def inner():
#         nonlocal x
#         print('Вложенная функция', x)
#     inner()
#     print('Внешняя функция', x)
# outer()

# x = 5           # Объединение глобальных и локальных переменных.
# def foo():
#     x = 10
#     print('local "X":', x)
# foo()
# print('global "X":', x)

