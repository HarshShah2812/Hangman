# %%
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess!{guess} is in the word.")
    else:
        print (f"Sorry, {guess} is not in the word. Try again.")
# %%
def ask_for_input():
    while(True):
        guess = input("Guess a letter ")
        if len(guess) == 1:
            break
        else: 
            print("Invalid letter, please enter a single alphabetical character.")
    check_guess(guess)
# %%
h = Hangman(["Banana", "Orange", "Apple", "Kiwi", "Melon"])
h.ask_for_input()
