import random

# Generate a random number within a specified range
low = 1
high = 5
random_number = random.randint(low, high)

print("Welcome to the Guess the Number Game!")
print(f"I'm thinking of a number between {low} and {high}.")

# Game loop
while True:
    # Prompt the player to guess the number
    guess = int(input("Enter your guess: "))

    # Provide feedback based on the player's guess
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
