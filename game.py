# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hfiqar <hfiqar@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/08 15:29:31 by hfiqar            #+#    #+#              #
#    Updated: 2024/05/08 18:12:06 by hfiqar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def user_guess():
    while True :
        user_choice = (input("     chose one of those\n1:paper\n2:rock\n3:scissors\n     and Let me beat you !")).lower()
        if (user_choice == "paper" or user_choice == "rock" or user_choice == "scissors") :
            return user_choice
        else:
            print("invalid input !!!")
            


def computer_guess():
   return(random.choice(["paper", "rock", "scissors"]))

def comparaison(computer_guess, user_guess):
    again = "yes"
    while again == "yes" :
            if (computer_guess == user_guess):
                print("==")
            elif(computer_guess == "paper" and user_guess == "rock"):
                print("computer wins")
            elif(computer_guess == "paper" and user_guess == "scissors"):
                print("you win")
            elif(computer_guess == "rock" and user_guess == "paper"):
                print("you win")
            elif(computer_guess == "rock" and user_guess == "scissors"):
                print("computer wins")
            elif(computer_guess == "scissors" and user_guess == "rock"):
                print("you win")
            elif(computer_guess == "scissors" and user_guess == "paper"):
                print("computer wins")
            again = input("if you wanna play again type (yes/no)").lower()

if __name__ == "__main__":
    user_choice = user_guess()
    computer_choice = computer_guess()
    comparaison(computer_choice, user_choice)


