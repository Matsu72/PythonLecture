def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")

print_name_local()

age = 20
def print_age():
    # age = 12
    print(f"I'm {age} years old")

print_age()
print(age)

# 関数ではローカル変数を使うことができないときは、グローバル変数を使う