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


# 15_26 Вэбинар 13.12.2023 21:44