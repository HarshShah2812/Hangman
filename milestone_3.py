# %%
import random
# %%
class Hangman():
    def _init_(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for l in word:
                if self.word[l] == guess:
                    self.word_guessed[l] = guess
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} left")
        
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while(True):
            guess = input("Guess a letter")
            
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
    ask_for_input()