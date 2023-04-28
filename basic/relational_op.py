# 比較演算子 >, <, >=, <=, ==, !=
print(5 > 3)  # True
print(2.0 < 1)  # False
print(5 >= 5)  # True
print(5 <= 4)  # False
print(5 == 3)  # False
print(5 != 3)  # True

# 比較演算子は数値型以外にも使える
print("abc" == "abc")  # True
print("abc" == "ABC")  # False
print("abc" != "ABC")  # True
print(1 == 1.0)  # True
print(1 == "1")  # False
print("1" == "1")  # True

# == と is の違い
# == は値が等しいかどうかを比較する
# is はオブジェクトが等しいかどうかを比較する
# 例えば、以下のような場合
a = 1
b = 1.0
print(a == b)  # True
print(a is b)  # False

# 以下のような場合
a = 1
b = 1
print(a == b)  # True
print(a is b)  # True

# 以下のような場合
a = "abc"
b = "a1c"
print(a == b)  # True
print(a is b)  # True
