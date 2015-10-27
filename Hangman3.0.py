emptyHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
______________________|__________________"""

headHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
                      |
                      |
                      |
                      |
                      |
______________________|__________________"""
bodyHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
        |             |
        |             |
        |             |
                      |
                      |
______________________|__________________"""
leftArmHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
       /|             |
      / |             |
        |             |
                      |
                      |
                      |
______________________|__________________"""
rightArmHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
       /|\\            |
      / | \\           |
        |             |
                      |
                      |
______________________|__________________"""
leftLegHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
       /|\\            |
      / | \\           |
        |             |
       /              |
      /               |
______________________|__________________"""
rightLegHanger ="""
         _____________             
        |             |           
        |             |            
        |             |             
        |             |             
        |             |             
        o             |
       o o            |
        o             |
       /|\\            |
      / | \\           |
        |             |
       / \\            |
      /   \\           |
______________________|__________________"""

hangers = [emptyHanger, headHanger, bodyHanger,\
           leftArmHanger, rightArmHanger, leftLegHanger, rightLegHanger]
#what to add:
#spaces within words
#better hanging men

wordList = ["Cheese", "Jazz", "Zoo", "Truck", "Fireplace", "Alcohol",\
            "Trial", "Refund", "Hangman", "Train"]

from random import randrange
word = wordList[randrange(0, len(wordList))].upper()
letters = list(word)
correctGuesses = []
guessWord  = len(word)*"-"
wrongGuesses = []
a = 0
print(hangers[a])
def wasGuessed():
    print ("You already guessed that")
def guessCorrect():
    print(guessLetter + " is in the word " + str(word.count(guessLetter))\
              + " times!")
    for i in range(len(word)):
            if guessLetter == word[i]:
                guessWord[i] = guessLetter
'''def guessWholeWord():
    guessWord = "".join(guessWord)
    guessWord = word
    return guessWord
'''
'''def guessWrong():
    a += 1
    print("Sorry that isn't in the word")
    wrongGuesses.append(guessLetter)
    print(wrongGuesses) #testingPurposes
    print(hangers[a])
'''
        
    
while (guessWord != word):
    if len(wrongGuesses) == 6:
        break
    word = word.upper()
    guessWord = list(guessWord)
    guessLetter = input("Guess a letter to see if it's in the word, or guess the word: ").upper()
    if guessLetter == word:
        guessWord = "".join(guessWord)
        guessWord = word
        break
    elif guessLetter.isalpha() !=  True:
        print("Please guess a letter")
    elif len(guessLetter) > 1:
        print("Please only guess one letter")
    
    elif guessLetter in correctGuesses:
        wasGuessed()
    elif guessLetter in wrongGuesses:
        wasGuessed()
    elif guessLetter in word:
        guessCorrect()
        
    elif guessLetter not in word:
        a += 1
        print("Sorry that isn't in the word")
        wrongGuesses.append(guessLetter)
        print(wrongGuesses) #testingPurposes
        print(hangers[a])
       
    guessWord = "".join(guessWord)
    print(guessWord) #testing purposes
    
       
if guessWord.upper() == word.upper():
    print("You win! The word is {}".format(word))
else:
    print("sorry, you lose, the word was {}".format(word))         
print(hangers[a])

