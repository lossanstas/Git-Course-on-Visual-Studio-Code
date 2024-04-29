#def pow_func(base):
#    print(base **  2)
#pow_func(3)

#def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*"  * i)
#reverse_stair(4)

#def my_func():
#    a = 5
#    b = 10
#    print(a + b)
#my_func()

#def my_func(a, b):
#    print(a + b)
#my_func(5, 10)

# def my_func(a, b):
#    result = a + b
#    return result
# c = my_func(5, 10)
# print(c)

# def get_mul_func(m):
#     nonlocal_m = m
#     def local_mul(n):
#         return n * nonlocal_m
#     return local_mul

# two_mul =  get_mul_func(2) # возвращаем функцию, которая будет умножать числа на 2
# two_mul(5)  # 5 * 2 НЕ РАБОТАЕТ ЭТОТ КОД

# Задача: найти площадь и периметр прямоугольного треугольника.
# S=(катет1 * катет2)/2
# P=a+b+c
# import math  # Встроенная библиотека. math  и другие
# a = float(input('длинна катета а: '))
# b = float(input('длинна катета b: '))
# c = math.sqrt(a**2 + b**2)
# S = a*b/2
# P = a+b+c
# print((f'Длинна гипотинузы: {c} см.'))
# print(f'Площадь прямоугольного треугольника: {S} кв.см.')
# print(f'Периметр треугольника: {P} см.')

# import random # Встроенная библиотека. random - генерация случайного. randint - случайная цифра в диапазоне.
# a = int(input('Нижняя граница: '))
# b = int(input('Верхняя граница: '))
# n = random.randint(a, b) 
# print(n)

# Задача. Вывести сумму цифр случайного трёхзначного числа.
# import random
# n = random.randint(100, 120)
# print('Случайное число:', n)
# a = n % 100           # остаток от деления х.? ? - значение после запятой.
# print('Первая цифра:', a)
# b = n % 100 / 10      # остаток отделения х.!? !?/10. ! - среднее число.
# print('Вторая цифра:', b, '=', int(b))
# c = n // 100          # // - целочисленное деление х.!? х - первое число.
# print('Третья цифра:', c)
# res = int(a + b + c)
# print('Сумма цифр: ', res) 

# Задача. Вычислить массу тела. Формула: m=V*p
# V - объём, р - плотность.
# flag = input('Что искать? m - масса, V - объём, p - плотность.')
# result = 0
# if flag == 'm':
#     V = float(input('Объём '))
#     p = float(input('Плотность '))
#     result = (f'Масса: {p * V} кг.')
# elif flag == 'p':
#     m = float(input('Масса '))
#     V = float(input('Объём '))
#     result = (f'Плотность: {m / V} кг./м.куб.')
# elif flag == 'V':
#     m = float(input('Масса '))
#     p = float(input('Плотность '))
#     result = (f'Объём: {m / p} м.куб.')
# print(result)

