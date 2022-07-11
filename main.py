import random
import time

from colorama import init, Back
from ascii_art import *

rock = rock_raw.split('\n')
paper = paper_raw.split('\n')
scissors = scissors_raw.split('\n')
hand = (rock, paper, scissors)
choice_handler = {
    'rock': rock,
    'paper': paper,
    'scissors': scissors
}


def playerChoice():
    choice = input("Rock, paper, or scissors?\n").lower().strip()
    if choice == 'exit':
        exit()
    player_choice = choice_handler.get(choice)
    return player_choice


def botChoice():
    bot_choice = random.choice(list(choice_handler.values()))
    return bot_choice


def display(player_choice, bot_choice):
    for n in range(1, 31):
        print(f'{player_choice[n]}   VS   {bot_choice[n]}')


def winnerDefine(player_choice, bot_choice):
    player = hand.index(player_choice)
    bot = hand.index(bot_choice)
    if player == bot:
        print(f'{Back.YELLOW}{draw}{Back.RESET}')
        return
    game_index = f'{player}{bot}'
    match game_index:
        case '01' | '10':
            winner = 1
        case '02' | '20':
            winner = 0
        case '12' | '21':
            winner = 2
    if player is winner:
        print(f'{Back.GREEN}{win}{Back.RESET}')
    else:
        print(f'{Back.RED}{lose}{Back.RESET}')


if __name__ == '__main__':
    init()
    while True:
        player_choice = playerChoice()
        if player_choice is None:
            print('looks like you made a mistake\n')
            continue
        bot_choice = botChoice()
        display(player_choice, bot_choice)
        time.sleep(2)
        winnerDefine(player_choice, bot_choice)
