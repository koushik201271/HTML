import random

def guess_the_number():
    score = 0
    print("Welcome to 'Guess the Number'!")
    print("Guess a number between 1 and 100. Let's begin!\n")

    while True:
        number_to_guess = random.randint(1,100)
         attempts = 0

         while True:
            try:
                guess = int(input("Enter your guess(1,100): "))
                attempts = attempts + 1

                  if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess: 
                    print("Too high! Try again.")
                else:
                    print(f"Correct! You guessed it in {attempts}attempts.")
                    score = score + 1
                    print(f"Your current score: {score}\n")
                    break
                except ValueError:
                    print("Please enter a vaild number betwenn 1 and 100.")


guess_the_number()