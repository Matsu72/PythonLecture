#　リスト内法表記 (List Comprehension)
# 　リスト内法表記は、リストを生成するための簡潔な方法です。

# 例えば、0から9までの整数のリストを作る場合、次のように書くことができます。
square_list = [i ** 2 for i in range(10)]
print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# このように、リスト内法表記は、for文を使ってリストを生成する方法です。
# この例では、range(10)で0から9までの整数を生成し、それぞれの整数を2乗しています。

even_square_list = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_square_list)