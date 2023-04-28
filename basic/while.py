# while ループ
# while 条件式:
#   条件式が真の場合に実行する文

# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# breakとcontinue
# while True:
#     like = input("好きなフルーツを入力してください：")
#     if like == "exit":
#         break
#     else:
#         print(f"{like}は好きです")
#         continue



casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
:"""

while True:
    age = input("あなたは何歳ですか？：")
    if age.isdigit():
        age = int(age)
        if age >= casino_age:
            print("どうぞお入りください")
            game = input(game_text)
            if game.isdigit():
                game = int(game)
                if game == 1:
                    print("ルーレットを選択しました")
                    break
                elif game == 2:
                    print("ブラックジャックを選択しました")
                    break
                elif game == 3:
                    print("ポーカーを選択しました")
                    break
                else:
                    print("1~3の番号を入力してください")
                    continue
            else:
                print("数字を入力してください")
                continue
        else:
            print(f"あなたは{casino_age}歳未満なので入場できません")
            break
    else:
        print("数字を入力してください")
        continue