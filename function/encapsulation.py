# カプセル化：外からアクセスできないようにする
def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"You are too young to enter the casino. You must be at least {min_age} years old.")
        return

    def inner_casino_entrance():
        print("Welcome to the casino!")

    return inner_casino_entrance()

casino_entrance(28)