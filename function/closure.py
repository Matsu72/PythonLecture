# Closure:クロージャー

# # 関数もオブジェクト
# def compute_square(num):
#     return num * num

# f = compute_square
# print(f(10))

# function_list = [compute_square, print]
# print(function_list[0](10))

# # 関数も引数として渡せる
# def execute_func(func, param):
#     return func(param)

# print(execute_func(compute_square, 10))


# # 関数も戻り値として返せる
# def return_func():

#     def inner_func():
#         print("This is an inner function.")
#     return inner_func

# f = return_func()
# f()


# closure : 状態をキープした関数オブジェクト
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

square = power(2)
print(square(1120))


def average():
    nums = []
    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums(10))
print(average_nums(1))