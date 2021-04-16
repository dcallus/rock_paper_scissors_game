from flask import render_template, redirect
from app import app
from models.game import *
from models.game_play import *
from models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Rock/Paper/Scissors')

@app.route('/<player_1_gesture>/<player_2_gesture>')
def show(player_1_gesture, player_2_gesture):
    # assign gestures to players
    player_1.set_gesture(player_1_gesture.title())
    player_2.set_gesture(player_2_gesture.title())

    # get winning player
    winner = get_results(player_1, player_2)
    return render_template('result.html', title='Rock/Paper/Scissors', winner=winner, player_1=player_1, player_2=player_2)