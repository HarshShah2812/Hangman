# %%
import random
# %%
class Hangman:
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

        while True:
            guess = input("Guess a letter")
            
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
           
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
# %%
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
