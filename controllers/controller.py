from flask import render_template, redirect
from app import app
from models.game import *
from models.game_play import get_results

@app.route('/<player_1>/<player_2>')
def show(player_1, player_2):
    result = get_results(player_1, player_2)
    return result