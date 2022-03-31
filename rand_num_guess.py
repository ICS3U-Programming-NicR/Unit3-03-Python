#!/usr/bin/env python3

# Created by: Nicolas Riscalas
# Created on: March 29 2022
# Game for random number


import random
import sys
import colorama
import time
from colorama import Fore, Back, Style


def get_num(max_value, random_number):

    users_num = int(input("Guess a number between 1 and {}: ".format(max_value)))
    time.sleep(1)
    check_aswr(users_num, random_number, max_value)


def try_again_fnct():
    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        sys.exit()


def check_aswr(num_user, random_num_gen, num_big):

    if num_user > random_num_gen:
        print("The secret number is lower")
        get_num(num_big, random_num_gen)
    elif num_user < random_num_gen:
        print("The secret number is higher")
        get_num(num_big, random_num_gen)
    elif num_user == random_num_gen:
        print("Good Job you guessed correct!")
        try_again_fnct()


def main():

    # input
    print(Fore.GREEN + "Enter the largest number to be generated")
    biggest_num = int(input())
    random_num = random.randint(1, biggest_num)
    get_num(biggest_num, random_num)


if __name__ == "__main__":
    main()
