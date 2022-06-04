import random

while True:

    user_action = input("Enter a choice rock, paper, scissors): ")
    #user_action = int(user_input)

    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#Determine a winner

    if user_action == computer_action:
        print(f"both players selected {user_action}. It's a tie!!! ")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win! ")
        else:
            print("paper covers rock! You lose! ")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win! ")
        else:
            print("Scissors cuts paper! You lose. ")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break