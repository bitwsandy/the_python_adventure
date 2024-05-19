
import random

print("Let's play Rock, Paper, Scissors!")

# Get user's choice
while True:
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
    if user_choice in ['rock', 'paper', 'scissors']:
        break
    else:
        print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")

# # Get computer's choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print("You chose:", user_choice)
print("Computer chose:", computer_choice)
#
# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
