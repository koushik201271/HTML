import random

def generate_number(limit):

    return random.randint(1, limit)

def get_player_input(limit):
    
    while True:
        try:
            return int(input(f"Enter your guess (1-{limit}): "))
        except ValueError:
            print("Invalid input. Please provide a valid number.")

def play_round(limit):
    
    target = generate_number(limit)
    attempts = 0

    while True:
        guess = get_player_input(limit)
        attempts += 1

        if guess < target:
            print("Too low. Recalibrating expectations...")
        elif guess > target:
            print("Too high. Consider adjusting your approach...")
        else:
            print(f"Excellent! You reached the target in {attempts} attempts.")
            return attempts

def choose_difficulty():
   
    print("\nSelect Difficulty Level:")
    print("1. Easy   (1-10)")
    print("2. Medium (1-20)")
    print("3. Hard   (1-50)")
    print("4. Custom (You decide the range)")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 20
        elif choice == "3":
            return 50
        elif choice == "4":
            while True:
                try:
                    custom = int(input("Enter a custom range limit (minimum 10): "))
                    if custom >= 10:
                        return custom
                    else:
                        print("Range must be at least 10.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("Invalid selection. Please choose a valid option.")

def ask_replay():
    return input("\nWould you like to play another round? (y/n): ").lower() == "y"

def guess_the_number():
    print("\nWelcome to the Guess-the-Number Experience!")

    score = 0
    total_attempts = 0
    rounds_played = 0

    limit = choose_difficulty()

    while True:
        print(f"\n--- New Round (Range: 1-{limit}) ---")
        
        attempts = play_round(limit)

        score += 1
        total_attempts += attempts
        rounds_played += 1

        print(f"Round Score: {score}")

        if not ask_replay():
            break

    print("\n--- Session Summary ---")
    print(f"Total Rounds Played: {rounds_played}")
    print(f"Total Attempts: {total_attempts}")
    
    if rounds_played > 0:
        print(f"Average Attempts per Round: {total_attempts / rounds_played:.2f}")
    
    print("Thank you for playing. Session terminated.\n")

guess_the_number()