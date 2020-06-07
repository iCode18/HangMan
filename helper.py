import os


def newLine(x=1):
    print('\n' * x)


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def clear(*message):
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Welcome to HangMan Game")
    if(len(message) > 0):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        print(message[0])


def draw(shape):
    for item in shape:
        if(len(item) > 0):
            print(item)
    newLine()
