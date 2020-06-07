
import helper
from random_word import RandomWords
# get a random word
choosed = []
wrongs = 7
hangedPortion = []
# scetch the hang man
hanged = ["-----------", "|         |", "|         O",
          "|        /|\ ", "|         |", "|       _/ \_", "|          "]
notHanged = ["  O", " /|\ ", "  |", "_/ \_"]
hangedgrad = hanged[::-1]
word = (RandomWords().get_random_word()).lower()
tempGuess = list("_"*len(word))
while ('-' in word) or (' ' in word):
    word = (RandomWords().get_random_word()).lower()


def status(x):
    print('{} characters left to guess and you got {} shots'.format(
        tempGuess.count('_'), wrongs))
    helper.newLine()
    print("Your guess: " + (" ".join(tempGuess)))
    helper.newLine(x)


helper.clear()
status(2)
while (wrongs > 0):
    helper.newLine(2)
    char = input("Guess a charachter: ")
    if char in choosed:
        helper.clear()
        status(1)
        print("You had this char before")
        for item in hangedPortion:
            if(len(item) > 0):
                print(item)
    else:
        choosed.append(char)
        if(char in word):
            indexList = helper.find(word, char)
            for i in indexList:
                tempGuess[i] = char
            helper.newLine()
            if ('_' not in tempGuess):
                helper.clear('You won!!!')
                print('The word was '+word)
                helper.newLine()
                helper.draw(notHanged)
                helper.newLine()
                break
            else:
                helper.clear()
                status(2)
                for item in hangedPortion:
                    if(len(item) > 0):
                        print(item)
        else:
            wrongs -= 1
            helper.clear()
            status(1)
            print('Wrong. You are left {} shots.'.format(wrongs))
            if(len(hangedgrad) > 1):
                hangedPortion.append(hangedgrad.pop())
                for item in hangedPortion:
                    if(len(item) > 0):
                        print(item)
            else:
                helper.clear('You lost!!!')
                print('The word was '+word)
                helper.newLine(5)
                hangedPortion.append(hangedgrad.pop())
                helper.draw(hangedPortion)
