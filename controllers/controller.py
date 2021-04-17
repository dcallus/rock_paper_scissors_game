from flask import render_template, request
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

@app.route('/play')
def play_computer_home():
    return render_template('play_computer.html', title='Rock/Paper/Scissors')

def process_form():
    user_name = request.form['player-name']

    if user_name:
        player_1 = Player(user_name)
    else:
        player_1 = Player("Player")

    user_choice = request.form['rps-menu']
    player_1.set_gesture(user_choice)

    vs_computer_game = Game(player_1)
    vs_computer_game.create_computer_player()
    player_2 = vs_computer_game.player_2

    winner = get_results(player_1, player_2)

    return (winner, player_1, player_2)

@app.route('/play', methods=['POST'])
def play_computer():
    game_data = process_form()
    winner = (game_data[0])
    player_1 = (game_data[1])
    player_2 = (game_data[2])
    return render_template('result.html', title='Rock/Paper/Scissors', winner=winner, player_1=player_1, player_2=player_2)

@app.route('/play-bigbang')
def play_bigbang_home():
    return render_template('play_bigbang.html', title='Rock/Paper/Scissors')

@app.route('/play-bigbang', methods=['POST'])
def play_bigbang():
    game_data = process_form()
    winner = (game_data[0])
    player_1 = (game_data[1])
    player_2 = (game_data[2])
    return render_template('result.html', title='Rock/Paper/Scissors/Lizard/Spock', winner=winner, player_1=player_1, player_2=player_2)