# decorator 関数に機能を付属する

def greeeting(func):
    def inner(*args, **kwargs):
        print('Hello {}'.format(*args, **kwargs))
        func(*args, **kwargs)
        print('Nice to meet you!')
    return inner

@greeeting
def say_name(name):
    print('I am {}'.format(name))

# # say_name('Taro')
# say_name = greeeting(say_name)
# say_name('Taro')

# defの上の@はデコレーターと呼ばれる
# デコレーターは関数に機能を付属する
# 例えば、関数の実行前後に処理を追加する

@greeeting
def say_name_and_origin(name, origin):
    print('I am {} from {}'.format(name, origin))
say_name_and_origin('Taro', 'Japan')