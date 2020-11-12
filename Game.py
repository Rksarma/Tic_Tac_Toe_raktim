# Display board Function

from IPython.display import clear_output
clear_output()
def display_board(board):
    clear_output()
    print('|' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('|' + '_' + ' |' + '__' + ' | ' + '__' + '|')
    print('|' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('|' + '_' + ' |' + '__' + ' | ' + '__' + '|')
    print('|' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')

# Marker Choice Function

def marker_choice():
    choice = ''
    while choice not in ['X','O']:
        choice = input('Player 1 choose your marker X/O : ').upper()
    if choice == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Place marker function
def place_marker(board,marker,position):
    board[position] = marker

# Win check function

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # row 1(down)
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # row 2
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # row 3
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # column 1
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # column 2
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # column 3
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # Diagonal 1
            (board[9] == mark and board[5] == mark and board[1] == mark))  # Diagonal 2

# Check space Function
def check_space(board,position):
    return board[position] == ' '

# Fill up check
def fill_up(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True
# Player choice function

def player_input(board):
    position = 0
    while not check_space(board,position):
        position = int(input('Choose your next position 1 - 9 :  '))
    return position

# Play first function
from random import randint
def player_first():
    flip = randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

# Replay Function
def game_replay():
    replay = ''
    while replay not in ['Y','N']:
        replay = input('Do you want to play again ?? Y/N : ').upper()
    if replay == 'Y':
        return True
    else:
        print('We are soory to leave you like this !!')
        return False







while True:
    the_board = [' ']*10
    display_board(the_board)
    player1_marker , player2_marker = marker_choice()

    turn = player_first()
    print( turn + ' will go first')

    play_game = input('Are ready to play the game ?? Y/N')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            position = player_input(the_board)
            place_marker(the_board,player1_marker,position)
            # win or Loss
            if win_check(the_board,player1_marker) :
                print('Player 1 won the game !!')
                display_board(the_board)
                game_on = False
            else:
                if fill_up(the_board):
                    display_board(the_board)
                    print('Game Tie !!')
                    game_on = False
                else:
                    turn = 'Player2'

        else:

            display_board(the_board)
            position = player_input(the_board)
            place_marker(the_board, player2_marker, position)
            # win or Loss
            if win_check(the_board, player2_marker):
                print('Player 2 won the game !!')
                display_board(the_board)
                game_on = False
            else:
                if fill_up(the_board):
                    display_board(the_board)
                    print('Game Tie !!')
                    game_on = False
                else:
                    turn = 'Player1'

    if not game_replay():
        break









