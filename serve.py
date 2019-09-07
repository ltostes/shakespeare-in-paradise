# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:56:00 2018

@author: lucas.tostes
"""

from flask import Flask
from flask import render_template
from random import shuffle
from os.path import exists
from os import makedirs
#import pandas as pd
from datetime import datetime

app = Flask(__name__)

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

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "You are playing Shakeaspeare in Paradise!"

    number_of_players, start_time, round = get_stats()

    return render_template('index.html', message=message, number_of_players=number_of_players,start_time=start_time, round = round)

# a route where we will display a welcome message via an HTML template
@app.route("/player/<int:player_number>")
def player(player_number):

    player_background_colors    = ['#8749b3',' #ff4d4d', '#ffa600', '#ff4400', '#1732ff', '#eb1f10', '#452302', '#098a00', '#adadad', '#000000', '#ffffff']
    player_text_colors          = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#000000']

    # Purple, Pink, Yellow, Orange, Blue, Red, Brown, Green, Gray, Black, White

    number_of_players, start_time, round = get_stats()

    if (player_number > number_of_players):
        return render_template('player.html', player_number=player_number, player_word="Oops...",start_time=start_time,round=round,word_message="Seems like this player is not in the game this round ",round_message="...And this is still round "+str(round))

    player_word = get_player_word(player_number)

    return render_template('player.html', player_number=player_number, player_word=player_word,start_time=start_time,round=round,word_message=get_word_message(player_number),round_message=get_round_message(round), player_background_colors = player_background_colors,player_text_colors = player_text_colors)

# a route where we will display a welcome message via an HTML template
@app.route("/set/<int:number_of_players>")
def set_for_players(number_of_players):

    setup = startup(number_of_players)

    start_time = setup['start_time']
    setup['round'] = 1

    save_setup(setup)

    return render_template('index.html', message="Started for " + str(number_of_players) + " players", number_of_players=number_of_players,start_time=start_time)

@app.route("/newround")
def newround():

    number_of_players, start_time, round = get_stats()

    setup = startup(number_of_players)

    start_time = setup['start_time']
    round = setup['round']

    save_setup(setup)

    return render_template('index.html', message="New round!", round=round,number_of_players=number_of_players,start_time=start_time)

@app.route("/cheatsheet")
def cheatsheet():

    number_of_players, start_time, round = get_stats()

    number_of_players = int(number_of_players)

    players = []

    for player_number in range(1,number_of_players+1):
        player = {}
        player['word'] = get_player_word(player_number)
        player['number'] = player_number

        players.append(player)

    return render_template('cheatsheet.html', message="" + str(number_of_players) + " players game", number_of_players=number_of_players,start_time=start_time,players=players, round=round)


# a route where we will display a welcome message via an HTML template
@app.route("/reset")
def reset_rounds():

    reset_setup()

    return render_template('index.html', message="Game reset! Please set the first round with the correct num of players", number_of_players=10,start_time=start_time, round=round)

# run the application
if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)
