import random
wordList = ["apple", "banana", "tools", "computer", "suspicous", "arizona", "connecticut", "operation","opposition", "kryptonite"]
gameWord = wordList[random.randint(0, len(wordList)-1)]
print(gameWord)