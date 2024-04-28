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

def my_func(a, b):
   result = a + b
   return result
c = my_func(5, 10)
print(c)

# def get_mul_func(m):
#     nonlocal_m = m
#     def local_mul(n):
#         return n * nonlocal_m
#     return local_mul

# two_mul =  get_mul_func(2) # возвращаем функцию, которая будет умножать числа на 2
# two_mul(5)  # 5 * 2 НЕ РАБОТАЕТ ЭТОТ КОД