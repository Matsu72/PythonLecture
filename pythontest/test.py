# assert文：条件式がFalseの場合に例外を発生させる
# assert 条件式, メッセージ
# 条件式がFalseの場合にメッセージを表示して例外を発生させる
# 条件式がTrueの場合は何もしない
# メッセージは省略可能

# a = 1
# b = 2
# assert a == b, 'aとbが等しくありません'

def power(base, exp):
    return base ** exp

assert power(2, 3) == 8, '2の3乗は8ではありません'