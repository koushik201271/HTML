import random
import json
import os

class Flashcard:
    def __init__(self, question, answer):
        # Fixed: assign the stripped string back to self.question
        self.question = question.strip()
        self.answer = answer.strip()

    def to_dict(self):
        return {"question": self.question, "answer": self.answer}
    
    @staticmethod
    def from_dict(data):
        return Flashcard(data["question"], data["answer"])

class FlashcardDeck:
    def __init__(self, filename="data.json"): # Changed extension to .json for clarity
        self.filename = filename
        self.cards = []
        self.load()

    def default_cards(self):
        return [
            Flashcard("What is Python?", "A programming language"),


            Flashcard("What is a variable?", "A container for storing data"),


            Flashcard("What is a list?", "A collection of items"),


            Flashcard("What is a tuple?", "An immutable collection"),


            Flashcard("What is a dictionary?", "Key-value pair data structure"),


            Flashcard("What is a loop?", "Used to repeat code"),



            Flashcard("What is if statement?", "Used for decision making"),


            Flashcard("What is a function?", "Reusable block of code"),


            Flashcard("What is an integer?", "Whole number"),


            Flashcard("What is a float?", "Decimal number"),


            Flashcard("What is a string?", "Text data"),


            Flashcard("What is boolean?", "True or False"),


            Flashcard("What does len() do?", "Returns length"),


            Flashcard("What is input()?", "Takes user input"),


            Flashcard("What is print()?", "Displays output"),


            Flashcard("What is indexing?", "Accessing elements by position"),


            Flashcard("What is slicing?", "Extracting part of data"),


            Flashcard("What is None?", "Represents no value"),


            Flashcard("What is a module?", "A file containing Python code"),


            Flashcard("What is import?", "Used to include modules")

            
        ]
  
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f) # Fixed: load the json data first
                    self.cards = [Flashcard.from_dict(d) for d in data] # Fixed: use () instead of {}
            except (json.JSONDecodeError, KeyError):
                self.cards = self.default_cards()
        else:
            self.cards = self.default_cards()
            self.save()

    def save(self):
        # Fixed: indentation and used () for json.dump
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.cards], f, indent=4)

    def add_card(self, question, answer):
        # Fixed: typo 'qustion' and syntax ()
        self.cards.append(Flashcard(question, answer))
        self.save()

    def remove_card(self, index): # Renamed for consistency with main()
        if 0 <= index < len(self.cards):
            # Fixed: typo 'seld'
            del self.cards[index]
            self.save()
            return True
        return False
    
    def edit_card(self, index, new_q=None, new_a=None):
        if 0 <= index < len(self.cards):
            if new_q:
                self.cards[index].question = new_q
            if new_a:
                self.cards[index].answer = new_a
            self.save()

    def shuffle(self):
        random.shuffle(self.cards)

    def quiz(self, reverse=False):
        if not self.cards:
            print("No cards available to quiz!")
            return

        score = 0
        wrong = []

        for card in self.cards:
            q, a = (card.answer, card.question) if reverse else (card.question, card.answer)
            
            print(f"\nQuestion: {q}")
            user = input("Your answer: ").strip()

            if user.lower() == a.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {a}")
                wrong.append(card)

        print(f"\nScore: {score}/{len(self.cards)}")

        if wrong:
            print("\nIncorrect answers:")
            for c in wrong:
                print(f"- {c.question} = {c.answer}")

    def list_cards(self):
        if not self.cards:
            print("The deck is empty.")
        for i, card in enumerate(self.cards, 1):
            print(f"{i}. {card.question} | {card.answer}")

def main():
    deck = FlashcardDeck()

    while True:
        print("\n===== Flashcard Menu =====")
        print("1. Add flashcard")
        print("2. View all flashcards")
        print("3. Edit flashcard")
        print("4. Delete flashcard")
        print("5. Quiz (normal)")
        print("6. Quiz (reverse)")
        print("7. Shuffle cards")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            q = input("Enter question: ")
            a = input("Enter answer: ")
            deck.add_card(q, a)

        elif choice == "2":
            deck.list_cards()

        elif choice == "3":
            deck.list_cards()
            try:
                idx = int(input("Enter card number to edit: ")) - 1
                nq = input("New question (blank to skip): ")
                na = input("New answer (blank to skip): ")
                deck.edit_card(idx, nq if nq else None, na if na else None)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            deck.list_cards()
            try:
                idx = int(input("Enter card number to delete: ")) - 1
                if not deck.remove_card(idx):
                    print("Invalid card number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            deck.shuffle()
            deck.quiz()

        elif choice == "6":
            deck.shuffle()
            deck.quiz(reverse=True)

        elif choice == "7":
            deck.shuffle()
            print("Deck shuffled.")

        elif choice == "8":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()