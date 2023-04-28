#数値型(Numeric Type): integer, float, complex
#整数型(integer): int -3, -2, -1, 0, 1, 2, 3
print(type(1))
print(type(-1))

#浮動小数点型(float): float 3.14, 0.0, -1.23
print(type(3.14))
print(type(0.0))
print(0.1+0.1+0.1)

#複素数型(complex): complex 1 + 2j, 1 - 2j
print(type(1 + 2j))
print(type(1 - 2j))

#数値型の演算
#四則演算
print(1 + 1.2)
print(1 - 1.2)
print(2 * 3)
print(3 / 2)
print(3 // 2)

#べき乗
print(2 ** 3)

#剰余
print(10 % 3)

#数値型の変換
#int()
print(int(3.14))
print(int(-3.14))
print(int("10"))

result = 1 + 1.2
print(f"type of result is {type(result)}")
