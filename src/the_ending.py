#!/usr/bin/python3
import sys
from clear_screen import clear_screen
from sleep_print import sleep_print
from villain import *


def the_ending_choice() -> None:
    """
    This function run the hero's final decision during the ending
    :return: None
    """
    print()
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print("*" * 60)
    print(f"{hero.name}, choose your action: (S) Stay or (L) Leave.".center(55))
    print("*" * 60)
    user_input = input("Enter your choice here: ").capitalize()
    try:
        if user_input == "S":
            print()
            sleep_print()
            print("\"I will stay here to protect all of you.\"".center(55))
            print()
            sleep_print()
            print("\"What if you turn evil?\"".center(55))
            print()
            sleep_print()
            print("\"I won't. I'm strong enough to fight it from overtaking me.\"".center(55))
            print()
            sleep_print()
            print("\"We shall see.\"".center(55))
            sleep_print()
            sys.exit()
        elif user_input == "L":
            print()
            sleep_print()
            print("\"I will leave. I don't want to turn evil.\"".center(55))
            print()
            sleep_print()
            print("\"Do you think that will happen?\"".center(55))
            print()
            sleep_print()
            print("\"It could. I rather not take that risk.\"".center(55))
            print()
            sleep_print()
            print("The residents nod.".center(55))
            print()
            sleep_print()
            print(f"{hero.name} disappears in a flash of lightning and a clap of thunder.".center(55))
            sleep_print()
            sys.exit()
        else:
            print()
            print("*" * 60)
            print("!! Incorrect input !!".center(55))
            print("*" * 60)
            sleep_print()
            clear_screen()
            the_ending_choice()
    except ValueError:
        print()
        print("*" * 60)
        print("!! Please enter either S or L !!".center(55))
        print("*" * 60)
        print()
        sleep_print()
        clear_screen()
        the_ending_choice()


def the_ending() -> None:
    """
    This function displays the ending of the game.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print(f"{main_villain.name} collapses onto the ground and blood gushes out of his body.".center(55))
    print()
    sleep_print()
    print(f"{hero.name} stands over the {main_villain.name}.".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"Go ahead and kill me.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"Who are you?\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I forgot my name. It's been so long since anyone used it.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I was sent by The Great Power long ago.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I was good. I was pure.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"What happened? Why did you become evil?\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"Corruption.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"I don't understand.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I don't either. I started having bad thoughts.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I thought about killing the people.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"I thought about destroying the land.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"Eventually, I succumbed to my thoughts.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"It will happen to you if you stay here.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"I won't. I'm strong.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"So was I. Leave here. Go back to The Great Power.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"These residents need me!\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"They will survive without you. They did without me.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"I'm not like you.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: \"You will become like me. Learn from my mistake.\"".center(55))
    print()
    sleep_print()
    print(f"{hero.name}: \"You're trying to manipulate me. It won't work.\"".center(55))
    print()
    sleep_print()
    print(f"{main_villain.name}: sighs and closes his eyes.".center(55))
    print()
    sleep_print()
    print("His body erupts into flames. The fire burns fast.".center(55))
    print()
    sleep_print()
    print("Smoke rises from the scattered ashes.".center(55))
    print()
    sleep_print()
    print(f"The residents walk over to {hero.name}. One of them steps forward.".center(55))
    print()
    sleep_print()
    print("\"So will you stay with us, or will you leave?\"".center(55))
    the_ending_choice()