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

# attempt a relative import
try:
    from .game import engine
except (ImportError, ValueError):
    from game import engine

app = Flask(__name__, template_folder="../templates", \
                      static_folder="../static")

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "You are playing Shakeaspeare in Paradise!"

    number_of_players, start_time, round = engine.get_stats()

    return render_template('index.html', message=message, \
                                         number_of_players=number_of_players, \
                                         start_time=start_time, \
                                         round = round)

# a route where we will display a welcome message via an HTML template
@app.route("/player/<int:player_number>")
def player(player_number):

    player_background_colors    = ['#8749b3',' #ff4d4d', '#ffa600', '#1732ff', '#ff4400', '#eb1f10', '#452302', '#098a00', '#adadad', '#000000', '#ffffff']
    player_text_colors          = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#000000']

    # Purple, Pink, Yellow, Blue, Orange, Red, Brown, Green, Gray, Black, White

    number_of_players, start_time, round = engine.get_stats()

    if (player_number > number_of_players):
        return render_template('player.html', player_number=player_number, player_word="Oops...",start_time=start_time,round=round,word_message="Seems like this player is not in the game this round ",round_message="...And this is still round "+str(round))

    player_word = engine.get_player_word(player_number)

    return render_template('player.html', player_number=player_number,\
                                          player_word=player_word, \
                                          start_time=start_time, \
                                          round=round, \
                                          word_message=engine.get_word_message(player_number), \
                                          round_message=engine.get_round_message(round), \
                                          player_background_colors = player_background_colors, \
                                          player_text_colors = player_text_colors)

# a route where we will display a welcome message via an HTML template
@app.route("/set/<int:number_of_players>")
def set_for_players(number_of_players):

    setup = engine.startup(number_of_players)

    start_time = setup['start_time']
    setup['round'] = 1

    engine.save_setup(setup)

    return render_template('index.html', message="Started for " + str(number_of_players) + " players", \
                                         number_of_players=number_of_players, \
                                         start_time=start_time)

@app.route("/newround")
def newround():

    number_of_players, start_time, round = engine.get_stats()

    setup = engine.startup(number_of_players)

    start_time = setup['start_time']
    round = setup['round']

    engine.save_setup(setup)

    return render_template('index.html', message="New round!", \
                                         round=round, \
                                         number_of_players=number_of_players, \
                                         start_time=start_time)

@app.route("/cheatsheet")
def cheatsheet():

    number_of_players, start_time, round = engine.get_stats()

    number_of_players = int(number_of_players)

    players = []

    for player_number in range(1,number_of_players+1):
        player = {}
        player['word'] = engine.get_player_word(player_number)
        player['number'] = player_number

        players.append(player)

    return render_template('cheatsheet.html', message="" + str(number_of_players) + " players game", \
                                              number_of_players=number_of_players, \
                                              start_time=start_time, \
                                              players=players, \
                                              round=round)


# a route where we will display a welcome message via an HTML template
@app.route("/reset")
def reset_rounds():

    reset_setup()

    return render_template('index.html', message="Game reset! Please set the first round with the correct num of players", \
                                         number_of_players=10, \
                                         start_time=start_time, \
                                         round=round)

# run the application
if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)
