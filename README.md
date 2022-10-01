# Hangman

## A repository containing the work I've done in order to create a Hangman game

### Milestone 1

I have used Python to build a random word generator that randomly picks a fruit from a given list, as well as to capture user input with the use of a built-in function ("input") where the player is asked to enter a single letter, also letting them know when an input is valid and when it isn't with the use of an if/else statement. I have used Python as it is easily readable, as well as having a wide array of built-in functions e.g. "random".

![image](https://user-images.githubusercontent.com/67421468/192967349-b42f6f64-57fe-4a8d-b10c-510f2a1e330e.png)

### Milestone 2

Here, I have created the functions that I will be implementing in the game. 

The first function, check_guess, checks if the guess is in the randomly generated word. I have defined this function by firstly using the variable "guess" as the parameter which will be passed into the function. Within the body of the function, I have firstly used the "lower()" method to ensure that the guess is converted to lower case; then, I have introduced an "if" statement to check if the guess is in the word; where this is the case, a statement will be printed to say that the guess is in the word; I have also created an "else" block to tell the reader when the guess is not in the word.

![check_guess](https://user-images.githubusercontent.com/67421468/193422406-e724c29f-4a90-410c-b1b9-0997aaf254c0.png)

In the second function, ask_for_input, a "while true" loop is used as it runs endlessly, within which the guess is taken and checked to see if it is a single, alphabetical letter with the use of an "if" statement; if this is the case, then with the help of a "break" statement, the loop is terminated and enables you to skip to the next line of code after the loop, otherwise, an else statement is printed, telling the player that their guess is invalid and that they'll need to enter a single alphabetical character. Outside of the loop, the previously created check_guess function is then called.

![ask_for_input](https://user-images.githubusercontent.com/67421468/193422440-5babe692-bc2c-44e4-a7ef-e02b333bbc19.png)

Finally, the ask_for_input function is called.

![ask_for_input()](https://user-images.githubusercontent.com/67421468/193422460-c33ea13f-5300-478c-9bb7-9fdc298ddfbb.png)
