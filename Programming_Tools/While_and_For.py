# # Нарезка
# name = "snow storm"
# print(name[6:8])  # "to"

# # Целочисленное деление
# x = 4.5
# y = 2
# print(x // y)   # 2.0

# # Применение ключевого значения "elif"
# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)


# x = 23
# num = 0
# if x > 10 or 11:
#     print(num)

# # # Написать цикл, который будет складывать натуральные числа, пока их сумма не превысит 500.
# S = 0 # переменная-счётчик для суммы чисел
# n = 1 # число, с которого начинаем считать
# while S < 500:
#     S += n # увеличиваем сумму, равносильно S = S + n
#     n += 1 # т.к. сумма ещё не достигла нужного значения, то увеличиваем переменную счётчик
#     print("Ещё считаю...")
# print("Сумма равна: ", S)
# print("Количество чисел: ", n-1)