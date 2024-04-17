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

# Рекурсивная функция: фактериал. (4*3*2*1)
def facterial(x):
    if x == 1:
        return 1
    return facterial(x-1)*x
print(facterial(4))

45:00



