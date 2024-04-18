# L = ['a', 'b', 'd']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a) - id(b))

# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
#
# print(a)

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# text = input("Введите текст:")
#
# unique = set(text)
#
# print("Количество уникальных символов: ", len(unique))

# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# debtors = {"Петров", "Антонов"}
#
# non_debtors = abons.difference(debtors)
#
# print(non_debtors)

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.intersection(b_set)
#
# print(a_and_b)

# some_var = (None)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = None # пустая строка
# b = a or 1
# print(b)

# a = ""
# b = "bar"
#
# print(1 and a or b)

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(*more_numbers, sep='; ')

# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# print(fruits[0], fruits[1], fruits[2], fruits[3], sep='; ')
# print(*fruits, sep=', ')

# def liner_solve(a, b):
#     return b / a
# print(liner_solve(0, 1))

# def linear_solve(a, b):
#     if a: # помним, что 0 интерпретируется как False, иначе True
#         return b / a
#     elif not a and not b: # Снова используем числа в логических выражениях.
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# print(int(linear_solve(2, 10)))

# # Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x % 2 == 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

# # map + filter
# some_list = [i - 10 for i in range(20)]
# def pow2(x): return x**2
# def positive(x): return x > 0
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))

# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
# #sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря
# # Чтобы отсортировать его по ключам нужно сделать так
# print(dict(sorted(d.items(), key=lambda x: x[1])))

# ИМТ (вес, рост)
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
# sorted(data, key = lambda x: x[0] / x[1]**2) # Никаких значений на выходе.????

# # ИМТ (вес, рост) найти минимальное значение ИМТ
# data = [
#    (82, 1.91),
#    (68, 1.74),
#    (90, 1.89),
#    (73, 1.79),
#    (76, 1.84)
# ]
# print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу

# Сортировка текста по длинне
# a = ["asd", "bbd", "ddfa", "mcsa"]
# print (list(map(len, a)))

# # Перевод текста в верхний регистр
# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.upper, a)))

