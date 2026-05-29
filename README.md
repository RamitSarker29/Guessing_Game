# Number Guessing Game

A simple Python console game where the player tries to guess a randomly generated number within a chosen range.

## Features

* User chooses the upper limit of the range
* Random number generation using Python's `random` module
* Input validation
* Hints provided after each guess

  * "Higher..." if the guess is too low
  * "Lower..." if the guess is too high
* Keeps running until the correct number is guessed

## How It Works

1. Enter the upper limit.
2. The program generates a random number between 1 and the chosen limit.
3. Enter your guess.
4. The program provides hints until you guess correctly.
5. Win the game by finding the correct number.

## Example

```text
Enter your limit: 100
Enter your number: 50
Higher...

Enter your number: 75
Lower...

Enter your number: 63
Congratulations!!!!
You've Won
```

## Technologies Used

* Python
* Random Module

## Concepts Learned

* Loops (`while`)
* Conditional Statements (`if-elif-else`)
* User Input
* Random Number Generation
* Input Validation
* Basic Game Logic

## How to Run

```bash
python guessing_game.py
```

## Future Improvements

* Count number of attempts
* Difficulty levels (Easy, Medium, Hard)
* High score tracking
* Multiplayer mode

## Author

Ramit Sarker
