import random

choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)

 
while True:
    user_choice = None
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    while user_choice not in choice:
        user_choice = input("What would you like to play? ").lower()
    print("The computer has chosen " + computer_choice)
    if computer_choice == user_choice:
        print("You both chose the same thing! It's a draw")
    elif user_choice == "rock":
        if computer_choice =="scissors":
            print("You win! Rock beats scissors")
        elif computer_choice == "paper":
            print("You lost, paper beats rock")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win! Paper beats rock")
        elif computer_choice == "scissors":
            print("You lost, scissors beats paper")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lost, rock beats scissors")
        elif computer_choice == "paper":
            print("You win! Scissors beats paper")
    next_round = input("Would you like to play again? (Y/N)").capitalize()
    if next_round != "Y":
        break

print("Bye, hope you play again soon!")





    
