import random

def display_rules():
    """Prints the rules of the game."""
    print("\n--- Game Rules ---")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock\n")

def determine_winner(user, computer):
    """Determines the winner of a single round."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    """The main function to run the Rock, Paper, Scissors game."""
    total_choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    round_number = 1

    print("\nWelcome to the Rock-Paper-Scissors Game!")
    print("Type 'rules' to see how to play, or 'quit' to exit the game.\n")
    
    while True:
        print(f"\n--- Round {round_number} ---")
        print("Available choices: rock, paper, scissors")
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Scores => You: {user_score} | Computer: {computer_score}\n")
            break
        elif user_choice == "rules":
            display_rules()
            continue
        elif user_choice not in total_choices:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(total_choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Scores > You: {user_score} | Computer: {computer_score}")
        round_number += 1

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    rock_paper_scissors()