casino_age = 18
games_dict = {"1" : "ルーレット", "2" : "ブラックジャック", "3" : "ポーカー"}


age = int(input("あなたは何歳ですか？："))
if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("ゲームを選択してください")
        for num, game_name in games_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in games_dict:
            print(f"{games_dict[game]}を始めます")
            break
        else:
            print("正しい番号を入力してください")
else:
    print(f"{casino_age}歳未満の方は入場できません")