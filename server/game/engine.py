"""Object for tracking game status"""
from random import shuffle
from os.path import exists
from os import makedirs
#import pandas as pd
from datetime import datetime


def get_stats():
    stats = []

    if not exists("data") :
        makedirs("data")
        reset_setup()

    with open("data/stats.txt","r") as stats_file:
        for line in stats_file:
            stats.append(line.strip())

    number_of_players = int(stats[0])
    start_time        = stats[1]
    round             = int(stats[2])

    return number_of_players, start_time, round

def load_words(words_path='palavras.csv'):
    raw_words = []

    with open(words_path,"r") as words_file:
        for line in words_file:
            raw_words.append(line.strip())

    return raw_words

def startup(numberofplayers):

    words = load_words(words_path='palavras.csv')
    shuffle(words)

    number_of_players, start_time, round = get_stats()

    number_of_players = numberofplayers
    start_time        = datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    round             = round+1

    player_words = []

    for player_number in range(0,number_of_players):
        player_words.append(words[int((player_number)/2)])

    shuffle(player_words)

    ret = {"words":words, "number_of_players":number_of_players, "start_time":start_time,"player_words":player_words, "round":round}

    return ret

def blank_setup():

    words = [""] * 10

    number_of_players = 10
    start_time        = datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    round             = 0

    player_words = []

    for player_number in range(0,number_of_players):
        player_words.append(words[int((player_number)/2)])

    shuffle(player_words)

    ret = {"words":words, "number_of_players":10, "start_time":start_time,"player_words":player_words, "round":round}

    return ret

def save_setup(setup):

    number_of_players   = setup['number_of_players']
    start_time          = setup['start_time']
    player_words        = setup['player_words']
    round               = str(setup['round'])

    stats_raw = [str(number_of_players),start_time, round]

    with open('data/stats.txt', mode='w+', encoding='utf-8') as stats:
        stats.write('\n'.join(stats_raw))

    for player_number in range(0,len(player_words)):
        player_word = player_words[player_number]
        with open("data/player" + str(player_number+1) + ".txt", mode='wt', encoding='utf-8') as stats:
            stats.write(player_word)
        print("Writing :::: data/player" + str(player_number+1) + ".txt")

    return

def reset_setup():

    setup = blank_setup()

    start_time  = setup['start_time']
    round       = setup['round']

    save_setup(setup)

def get_player_word(player_number):

    print("Reading :::: data/player" + str(player_number) + ".txt")

    player_file = "data/player" + str(player_number) + ".txt"

    raw = []

    with open(player_file,"r") as player_file:
        for line in player_file:
            raw.append(line.strip())

    player_word = raw[0]

    return player_word

def get_word_message(player_number):

    return "That's your word, player #{player_number}.".format(**{"player_number":player_number})


def get_round_message(round):

    return "By the way, this is round {round}.".format(**{"round":round})
