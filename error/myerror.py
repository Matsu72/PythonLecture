class MyError(Exception):

    def __str__(self):
        return "my error occurred"

response = input("y/n?")
if response != 'y' and response != 'n':
    raise MyError("Invalid response: " + response)