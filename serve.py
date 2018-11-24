# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:56:00 2018

@author: lucas.tostes
"""

from flask import Flask
from flask import render_template
from random import shuffle
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def get_stats():
    stats = pd.read_csv("data/stats.csv")
    
    number_of_players = stats.loc[0][2]
    start_time        = stats.loc[1][2]
    
    return number_of_players, start_time

def load_words(words_path='palavras.csv'):
    raw_words = pd.read_csv(words_path)
    return list(raw_words[raw_words.columns[0]])

def startup(numberofplayers):
    words = load_words(words_path='palavras.csv')
    shuffle(words)
    
    number_of_players = numberofplayers
    start_time = datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    
    player_words = []
    
    for player_number in range(0,number_of_players):
        player_words.append(words[int((player_number)/2)])
    
    shuffle(player_words)
    
    ret = {"words":words, "number_of_players":number_of_players, "start_time":start_time,"player_words":player_words}

    return ret

def save_setup(setup):
    
    number_of_players = setup['number_of_players']
    start_time = setup['start_time']
    player_words = setup['player_words']
    
    stats_raw = [['number_of_players',number_of_players],['start_time',start_time ]]
    stats = pd.DataFrame(stats_raw)
    stats.to_csv("data/stats.csv")
    
    for player_number in range(0,len(player_words)):
        player_word = player_words[player_number]
        player_file = pd.DataFrame([player_word])
        player_file.to_csv("data/player" + str(player_number+1) + ".csv")
        print("Writing :::: data/player" + str(player_number+1) + ".csv")
        
    return

def get_player_word(player_number):
    print("Reading :::: data/player" + str(player_number) + ".csv")
    player_file = pd.read_csv("data/player" + str(player_number) + ".csv")
    player_word = player_file.iloc[0][1]
    
    return player_word

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    message = "You are playing Shakeaspeare in Paradise!"
    
    number_of_players, start_time = get_stats()
    
    return render_template('index.html', message=message, number_of_players=number_of_players,start_time=start_time)

# a route where we will display a welcome message via an HTML template
@app.route("/player/<int:player_number>")
def player(player_number):
    
    number_of_players, start_time = get_stats()
    
    player_word = get_player_word(player_number)
    
    return render_template('player.html', player_number=player_number, player_word=player_word,start_time=start_time)

# a route where we will display a welcome message via an HTML template
@app.route("/set/<int:number_of_players>")
def set_for_players(number_of_players):  
    
    setup = startup(number_of_players)
    
    start_time = setup['start_time']
    
    save_setup(setup)
    
    return render_template('index.html', message="Started for " + str(number_of_players) + " players", number_of_players=number_of_players,start_time=start_time)
    
@app.route("/cheatsheet")
def cheatsheet():  
    
    number_of_players, start_time = get_stats()
    
    number_of_players = int(number_of_players)
    
    players = []
    
    for player_number in range(1,number_of_players+1):
        player = {}
        player['word'] = get_player_word(player_number)
        player['number'] = player_number
        
        players.append(player)
        
    return render_template('cheatsheet.html', message="Game with " + str(number_of_players) + " players", number_of_players=number_of_players,start_time=start_time,players=players)
    
# run the application
if __name__ == "__main__":    
    app.run(host= '0.0.0.0',debug=True)
    