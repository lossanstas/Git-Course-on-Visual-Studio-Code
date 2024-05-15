# *args/**kwargs (Вместо "args" или "kwargs" можно использовать любые буквосочетания или слова)
# *args распаковка по позиции (списки, строки)
# **kwargs распаковка по имени (только словари)

# def fun(*abc):
#     print(abc[2])
# fun('Pithon', 'C++', 'Jumla')

# def func(*args):
#     result = 0
#     for item in args:
#         result += item
#     return result
# num = (1, 2, 3, 4, 5)
# print(func(*num))


# def fun(**dict):
#     print(dict)   #  Запаковка в словарь
# fun(name='Tom', surname='Cruse')




# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(*more_numbers, sep='; ')

# def my_sum(*numbers):
#     result = 0
#     for i in numbers:
#         result += i
#     print(f'sum: {result}')
# my_sum(10, 10, 8, 8, 6, 6, 4, 4, 2, 2)

