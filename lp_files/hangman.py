import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
========= ''', '''

  +---+
  |   |
  O   |
      |
      |
      |
========= ''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
========= ''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========= ''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''', '''

  +---+
  |   |
 (O   |
 /|\  |
 / \  |
      |
========= ''', '''

  +---+
  |   |
 (O)  |
 /|\  |
 / \  |
      |
========= ''']

#old word list
#words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
words={'Colors':'red blue green purple yellow white gray black brown teal pink'.split(),
'Shapes':'square circle triangle rectangle rhombus ellipse trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'watermelon orange peach grape cantaloupe banana mango lime lemon apple pear strawberry'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

#old function definition for the old word list
#def getRandomWord(wordlist):
    #this function returns a random string from the list of passed strings
#    wordIndex = random.randint(0, len(wordlist) - 1)
#    return wordlist[wordIndex]

def getRandomWord(wordDict):
#This function returns a random string from the passed dictionary of lists of strings, and the key also
#First, randomly select a key from the dictionary
    wordKey = random.choice(list(wordDict.keys()))
#Second, randomly select a string from the key in the dictionary list
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return[wordDict[wordKey][wordIndex], wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
#Prints the board based off any missed letters
    print(HANGMANPICS[len(missedLetters)])
    print()

#This gives a section to display any letters that were guessed but not correct
    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

#Makes blank lines for each letter in the secret word
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
#Replace blanks created above with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
#Show the secret word with spaces in between
        print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed):
#Returns the letter the player entered. This function makes sure the player enterned a single letter and not something else.
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess is alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
#This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

# LHP: I have no idea what "while True" is supposed to represent, or how I wrote this to loop properly based off of what I know...but the below code works.
# LHP: Stepping through this code would help to understand it.
while True:
    print('The secret word is in the catagory: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

#Let the player guess the word
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

#Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes, the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

#Check to see if the player guessed to many times and lost
        if len(missedLetters) == len(HANGMANPICS) -1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses! \nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses. The word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break
