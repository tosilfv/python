from wonderwords import RandomWord

##### DECLARATIONS #####
game_finished, guessed_letter, lose_life, wrong_guesses,\
    lives_left, guessed_letters, letter_indeces = False, '', '', 0, 6, [], []
title = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

##### RANDOM WORD #####
r = RandomWord()
# generate and save a random word
rword = r.word()
# convert random word into a list
rword_list = list(rword)
# save random word length
rword_length = len(rword)

##### BLANKS #####
# create initial random word string filled with blanks
blanks = "_" * rword_length
# create initial random word list filled with blanks
blanks_list = list(blanks)
# create looped random word string filled with blanks
blanks_string = ''.join(blanks_list)

##### PRINT STATUS #####
def already_guessed():
    print(f"You've already guessed {guessed_letter}\n{blanks_string}")

def endscreen():
    print(f"***********************IT WAS {rword}! YOU LOSE**********************")

def game_won():
    print(f"{blanks_string}\nYou win.")

def guessed_word():
    # show word status
    print(f"Word to guess: {blanks_string}")

def hangman_and_lives():
    # show status of hangman
    print(f'''{hangman[wrong_guesses]}\n****************************{lives_left}/6 LIVES LEFT****************************''')

def lost_life():
    print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")

##### GAME #####
print(title)
while not game_finished:
    guessed_word()
    # prompt the user to guess again
    guessed_letter = input("Guess a letter: ")

    # save guessed letter to guessed letters list
    if guessed_letter not in guessed_letters:
        guessed_letters.append(guessed_letter)
    else:
        already_guessed()
        hangman_and_lives()
        continue

    # handle guess
    if guessed_letter in rword_list:
        # save found letter indeces
        letter_indeces = [index for index, letter in enumerate(rword_list) if letter == guessed_letter]
        # replace found letter in blanks list letter indeces
        for index in letter_indeces:
            blanks_list[index] = guessed_letter
        # create blanks string again with guessed letter
        blanks_string = ''.join(blanks_list)
    else:
        lost_life()
        # increment wrong guesses counter to be used in status of hangman
        wrong_guesses += 1
        lives_left -= 1
    
    # win game
    if '_' not in blanks_list:
        game_won()
        game_finished = True
        continue

    # end game
    if wrong_guesses == 6:
        endscreen()
        game_finished = True
        continue

    hangman_and_lives()
