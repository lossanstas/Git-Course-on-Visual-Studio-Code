# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(*more_numbers, sep='; ')

def my_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    print(f'sum: {result}')
my_sum(10, 10, 8, 8, 6, 6, 4, 4, 2, 2)
