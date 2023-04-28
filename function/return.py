# def print_dict(dict):
#     for key, value in dict.items():
#         print(key, value)


# def main():
#     dict = {
#         'apple': 100,
#         'orange': 200,
#         'banana': 300,
#     }
#     print_dict(dict)

# if __name__ == '__main__':
#     main()


def get_first_last_word(text):
    words = text.split()
    return words[0], words[-1]

text = 'Hello World is my favorite word'
first, last = get_first_last_word(text)
print(first, last)