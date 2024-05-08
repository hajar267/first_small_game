# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hfiqar <hfiqar@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/08 15:29:31 by hfiqar            #+#    #+#              #
#    Updated: 2024/05/08 15:53:46 by hfiqar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import random

# def user_guess():
#     while True :
#         user = input("     chose one of those\n1:paper\n2:rock\n3:scissors\n     and Let me beat you !").lower
#         if user in {"paper" , "rock" , "scissors"} :
#             return user
#         else:
#             print("invalid input !!!")
#             user = input("     chose one of those\n1:paper\n2:rock\n3:scissors\n     and Let me beat you !").lower

# import random

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
#         if user_choice in ['rock', 'paper', 'scissors']:
#             return user_choice
#         else:
#             print("Invalid choice. Please enter rock, paper, or scissors.")

# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     print("Welcome to Rock-Paper-Scissors Game!")
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#         print(f"You chose: {user_choice}")
#         print(f"Computer chose: {computer_choice}")
#         print(determine_winner(user_choice, computer_choice))
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             print("Thank you for playing!")
#             break

# play_game()


import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")