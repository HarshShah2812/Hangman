# %%
import random
# %%
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks to see if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        The ist of words to be used in the game
    num_lives: int
        The number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the list of words
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        E.g. if the word is 'banana', the word_guessed list would be ['_', '_', '_', '_', '_', '_']
        If the player guesses 'b', the list would be ['b', '_', '_', '_', '_', '_']
    num_letters: int
        The number of unique letters in the word that are yet to be guessed yet
    num_lives: int
        The number of lives the player has
    word_list: list
        A list of the words used to play the game
    list_of_guesses: list
        A list of the letters that have already been tried
    
    Methods:
    -------
    check_guess(guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = len(self.word) * ['_'] # A list of the letters of the word
        self.num_letters = len(set(self.word)) # The number of unique letters in the word that have not been guessed yet
        self.num_lives = num_lives # The number of lives the player has at the start of the game.
        self.word_list = word_list
        self.list_of_guesses = [] # A list of the guesses that have already been tried
    
        print(f"The chosen word has {len(self.word)} letters")
        print(self.word_guessed)
    
    def check_guess(self, guess):
        '''
        Checks if the guess is in the word.
        If it's, it replaces the '_' in the word_guessed list with the guess.
        If it's not, it reduces the number of lives by 1.
        
        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        guess = guess.lower()
        if guess in list(self.word):
            print(f"Good guess! {guess} is in the word.")
            for i in range(0, len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        
        else:
            self.num_lives -= 1
            print(self.word_guessed) 
            
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
               
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character and is a letter
        If it passes both of these checks, it calls the check_guess method.
        '''
        
        guess = input("Guess a letter")
            
        if len(guess) != 1 or guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
                
           
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
                
            
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
                
# %%
'''
Creates a new object of the Hangman class, in order to then
be able to call the ask_for_input() method
'''
h = Hangman(["banana", "orange", "apple", "kiwi", "melon"])
h.ask_for_input()

# %%
def play_game():
    word_list = ["banana", "orange", "apple", "kiwi", "melon"]
    game = Hangman(word_list, num_lives = 5)

    while True:
        
        if game.num_lives == 0:
            print("You lost")
            print(f"The word was '{game.word}'")
            break
        
        elif game.num_letters > 0:
            game.ask_for_input()
            
        
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations! You have won the game.")
            print(f"The word is '{game.word}'")
            break
# %%
play_game()

# %%
