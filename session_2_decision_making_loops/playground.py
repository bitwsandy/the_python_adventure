import random

# Rock / Paper / Scissor

user_name = input("Enter your name : ")

while True :
    user_choice = input("Enter your choice [Rock, Paper, Scissor] : ")
    if user_choice in ['Rock', 'Paper', 'Scissor'] :
        break
    else :
        print("Invalid choice, Choices [Rock, Paper, Scissor]")

print(f"The Choice of {user_name} : {user_choice}")


computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
print(f"The Choice of Computer : {computer_choice}")


if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Paper' and computer_choice == 'Rock') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper'):
    print(f"{user_name} win!")
else:
    print("Computer wins!")
