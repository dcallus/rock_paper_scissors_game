from flask import render_template, request
from app import app
from models.game import *
from models.game_play import *
from models.player import *

def process_form():
    user_name = request.form['player-name']

    if user_name:
        player_1 = Player(user_name)
    else:
        player_1 = Player("Player")

    user_choice = request.form['rps-menu']
    player_1.set_gesture(user_choice)

    return player_1

def create_computer_game(big_bang_mode=False):
    vs_computer_game = Game(player_1)
    if big_bang_mode:
        vs_computer_game.create_computer_player(big_bang_mode=True)
    else:
        vs_computer_game.create_computer_player()
    return vs_computer_game

def get_game_result(player_1, player_2):
    winner = get_results(player_1, player_2)
    return winner


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
    return render_template('2player.html', title='Rock/Paper/Scissors', winner=winner, player_1=player_1, player_2=player_2)

@app.route('/play')
def play_computer_home():
    return render_template('play_computer.html', title='Rock/Paper/Scissors')

@app.route('/play', methods=['POST'])
def play_computer():
    player_1 = process_form()

    vs_computer_game = create_computer_game()
    player_2 = vs_computer_game.player_2
    winner = get_game_result(player_1, player_2)

    return render_template('play_computer.html', title='Rock/Paper/Scissors', winner=winner, player_1=player_1, player_2=player_2)

@app.route('/play-bigbang')
def play_bigbang_home():
    return render_template('play_bigbang.html', title='Rock/Paper/Scissors')

@app.route('/play-bigbang', methods=['POST'])
def play_bigbang():
    player_1 = process_form()
    vs_computer_game = create_computer_game(big_bang_mode=True)
    player_2 = vs_computer_game.player_2
    winner = get_game_result(player_1, player_2)

    return render_template('play_bigbang.html', title='Rock/Paper/Scissors/Lizard/Spock', winner=winner, player_1=player_1, player_2=player_2)