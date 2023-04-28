# Type annotation
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

print(add_nums(1, 2))

# 動的型付け言語
# 型を指定しなくても、実行時に型を判断してくれる
# 動的型付け言語の欠点
# 型が不明なため、実行時にエラーが発生する可能性がある
# 型が不明なため、IDEの補完機能が使えない
# 型が不明なため、コードの可読性が低くなる
# 型が不明なため、バグが発生しやすい
# 型が不明なため、テストコードの作成が困難になる
# 型が不明なため、コードの保守性が低くなる

one = 1
two = 2
print(add_nums(one, two))