# # lamda関数

# def square(x):
#     return x * x
# print(square(10))

# # lamda関数を使うと
# square2 = lambda x: x * x
# print(square2(10))

# def power(exponent):
#     def inner_power(base):
#         return base ** exponent
#     return inner_power
# third_power = power(3)
# print(third_power(2)) # 8

# # lamda関数を使うと
# def power(exponent):
#     return lambda base: base ** exponent


numbers = [4, 35, 7, 9, 10, 2, 1, 3, 8, 6]


    
# for num in numbers:
#     print(filter_func(num))

filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))
