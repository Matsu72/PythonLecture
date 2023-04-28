# 再帰関数（recursive function）:関数内で自分自身を呼び出す関数
# 再帰関数は、関数内で自分自身を呼び出す関数です。

# 階乗を求める関数
# def factorial(n):
#     if n == 1:
#         return 1
#     # print(n)
#     return n * factorial(n - 1)

# print(factorial(5)) # 120


# フィボナッチ数列を求める関数
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     # print(n)
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6)) # 55


# フィボナッチ数列を求める関数 再帰関数を使わない
def fibonacci(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
