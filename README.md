# Hangman

## A repository containing the work I've done in order to create a Hangman game

### Milestone 1

I have used Python to build a random word generator that randomly picks a fruit from a given list, as well as to capture user input with the use of a built-in function ("input") where the player is asked to enter a single letter, also letting them know when an input is valid and when it isn't with the use of an if/else statement. I have used Python as it is easily readable, as well as having a wide array of built-in functions e.g. "random".

![image](https://user-images.githubusercontent.com/67421468/192967349-b42f6f64-57fe-4a8d-b10c-510f2a1e330e.png)

### Milestone 2

Here, I have created the functions that I will be implementing in the game. 

The first function, check_guess, checks if the guess is in the randomly generated word. I have defined this function by firstly using the variable "guess" as the parameter which will be passed into the function. Within the body of the function, I have firstly used the "lower()" method to ensure that the guess is converted to lower case; then, I have introduced an "if" statement to check if the guess is in the word; where this is the case, a statement will be printed to say that the guess is in the word; I have also created an "else" block to tell the player when the guess is not in the word.

![check_guess](https://user-images.githubusercontent.com/67421468/193422406-e724c29f-4a90-410c-b1b9-0997aaf254c0.png)

In the second function, ask_for_input, I've used a "while true" loop as it runs continuously, within which the guess is taken and checked to see if it is a single, alphabetical letter with the use of an "if" statement; if this is the case, then with the help of a "break" statement, the loop is terminated and enables you to skip to the next line of code after the loop, otherwise, an else statement is printed, telling the player that their guess is invalid and that they'll need to enter a single alphabetical character. Outside of the loop, the previously created check_guess function is then called.

![ask_for_input](https://user-images.githubusercontent.com/67421468/193422440-5babe692-bc2c-44e4-a7ef-e02b333bbc19.png)

Finally, the ask_for_input function is called.

![ask_for_input()](https://user-images.githubusercontent.com/67421468/193422460-c33ea13f-5300-478c-9bb7-9fdc298ddfbb.png)

### Milestone 3

Here, I have created a class called "Hangman", in which I have put together the code I wrote in the previous milestones, making a few tweaks to it, as well as initialising the attributes that will be assigned to the class.

To define this class, I have firstly used ´def _init_(self, word_list, num_lives = 5)' to initialise the following attributes of the class: "word" - the word to be guessed, "word_guessed" - the list of letters for the word, "num_letters" - the number of unique letters in the word that are yet to be guessed, "num_lives" - the number of lives the player has at the start, "word_list" - a list of the words that will be used for the game and "list_of_guesses" - a list of the guesses already attempted, which is set to empty initially; "word_list" and '"num_lives" = 5' have been passed as parameters, alongside "self", which allows us to refer to the attributes of the class.

![def _init_](https://user-images.githubusercontent.com/67421468/193475845-b97088df-dcc0-4061-a74f-6e3112964be3.png)

Secondly, I have created 'def check_guess(self, guess)', within which the guess is firstly converted to lower case, and then it's passed through a "if" statement that checks if the guess is in the word. If the guess passes the check, the computer will tell the player that it is a good guess; in addition, I have created a "for" loop for the sake of control flow, looping through each letter in the word; if a letter in the word corresponds to the guess, the corresponding "_" will be relaced with the guess; outside the loop, the number of unique letters in the word is reduced by 1. If the guess doesn't pass the check, the number of lives will be reduced by one and the player will be told that the letter is not in the word, as well as the number of lives they have left. Lastly, the guess is appended to the list of guesses attempted.

![def check_guess](https://user-images.githubusercontent.com/67421468/193476312-c5664566-ff8d-4d2e-aaaa-b4e086e6667a.png)

Thirdly, I have created 'def ask_for_input(self)', within which a while loop is implemented and who's condition is set to "true", ensuring that the loop runs continuously. Inside the loop, the guess is checked; if the guess doesn't contain a single, alphabetical letter, or if the guess is in in the list of letters guessed, the player will be advised accordingly; otherwise, the guess will be passed through the check_guess method and will be added to the list of guesses.

![def ask_for_input](https://user-images.githubusercontent.com/67421468/193477139-ee463cf6-a504-42ee-ae5c-a9c26bd6aad0.png)

### Playing the game

Here, I defined the game (play_game) and the logic behind it. I did this by creating the word list and assigning it to "word_list". Then, I assigned the Hangman class with the parameters to a new variable "game". With regards to the logic, I created a "while" loop, assigning the condition "True" to it; within the loop, I used an "if" statement with the condition that if the player has no lives left, the computer will tell the player that they've lost, as well as what the word was; this is followed by an "elif" statement with the condition that if the number of letters left to guess is greater than 0, then the game will continue to ask for an input; I've created an additional elif statement  

![play_game()](https://user-images.githubusercontent.com/67421468/194377061-ba341ca0-5168-45d2-a135-5b89ae3e033e.png)

