import random
wordList = ["apple", "banana", "computer", "suspicous", "arizona", "connecticut", "operation","opposition", "kryptonite"]
gameWord = wordList[random.randint(0, len(wordList)-1)] # pick sandom thing from wordList
gL = [] # letters from word list
gL.extend(gameWord)
uL = [] #uL stands for under lines

for i in range(len(gL)):
    uL.append("_")

print(uL)

userGuess = ''
userGuessedLetters = []
guesses = 6

while userGuess != gameWord and guesses > 0:
    print(gameWord) #testing remove after
    print(f"\n game word is {uL}")
    break
    inputInput = int(input("1.guess a letter/n2.guess number"))
    if userInput == 1:
        print("you choose 1") #testing
    elif userInput == 2:
        print("you choose 2") # testing
    else:
        inputInput = int(input("1.guess a letter/n2.guess number"))