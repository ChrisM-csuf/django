import random

hangmanPics = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    o   |
        |
        |
       ===''', '''
    +---+
    o   |
    |   |
        |
       ===''', '''
     +---+
     o   |
    /|   |
         |
        ===''', '''
     +---+
     o   |
    /|\  |
         |
        ===''', '''
     +---+
     o   |
    /|\  |
    /    |
        ===''', '''
     +---+
     o   |
    /|\  |
    / \  |
        ===''', '''
      +---+
     [o   |
     /|\  |
     / \  |
         ===''', '''
      +---+
     [o]  |
     /|\  |
     / \  |
         ===''']
words = {'Animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
         'Fruits': 'apple orange mango tangerine grape lemon lime pear watermelon cherry banana strawberry'.split(),
         'Shapes': 'triangle rhombus square rectangle trapezoid parallelagram circle pentagon hexagon'.split(),
         'Colors': 'red orange yellow green blue purple indigo violet'.split()}

def randomWord(words):
    wordKey = random.choice(list(words.keys()))
    wordIndex = random.randint(0, len(words[wordKey])-1)
    return [words[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print('Wrong letters:')
    for i in range(len(missedLetters)):
        print(missedLetters[i])

    print(hangmanPics[len(missedLetters)])
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please only guess one letter')
        elif guess in alreadyGuessed:
            print('You have already guess that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def hangman():
    print(' H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord, secretSet = randomWord(words)
    gameIsDone = False

    difficulty = 'x'
    while difficulty not in 'EMH':
        print('Enter Difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
    if difficulty == 'M':
        del hangmanPics[8]
        del hangmanPics[7]
    elif difficulty == 'H':
        del hangmanPics[8]
        del hangmanPics[7]
        del hangmanPics[5]
        del hangmanPics[3]

    while True:
        print('The secret word is in this set: ' + secretSet)
        displayBoard(missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You win!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(hangmanPics) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' +
                      str(len(missedLetters)) + ' missed guesses and ' +
                      str(len(correctLetters)) + ' correct guesses, the word was "' +
                      secretWord + '"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = randomWord(words)
            else:
                break