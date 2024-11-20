import random
wordList = ["apple", "banana", "computer", "suspicous", "arizona", "connecticut", "operation","opposition", "kryptonite"]
gameWord = wordList[random.randint(0, len(wordList)-1)] #prints random thing from wordList
gL = [] # letters from word list
gL.extend(gameWord)
uL = [] #uL stands for under lines

for i in range(len(gL)):
    uL.append("_")

print(uL)