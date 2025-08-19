import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it. Good luck!\n")

    # Pick random number
    secret_number = random.randint(1, 100)
    attempts = 7

    # Game loop
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it right in {attempt} tries!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try again.\n")
        else:
            print("📈 Too high! Try again.\n")

    # Runs only if no correct guess was made (loop finished without 'break')
    else:
        print(f"😢 Sorry, you ran out of attempts. The number was {secret_number}.")

# Run the game
number_guessing_game()
