# def say_hello():
#     print('Hello')
# def say_goodbye():
#     print('good bye')
# message = say_hello
# message()
# message = say_goodbye
# message()

def sum(a, b):
    return a + b
def mult(a, b):
    return a * b
operation = sum
result = operation(5, 6)
print(result)

operation = mult
print(operation(5,6))