def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
test_board = ['@','X','O','X','O','X','O','X','O','X']
display_board(test_board)
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('p1: do u eant x or o: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
def place_marker(board,marker,position):
    board[position]=marker
display_board(test_board)
def winner(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 
winner(test_board,'X')
import random
def who():
    if random.randint(0, 1)==0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board,position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('select ur nxt pos: '))
    return position
def replay():
    return input('want to ply again: ').lower().startswith('y')
print('wlwcome to tictactoe')
while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = who()
    print(turn + ' will go first.')
    
    play_game = input('ready to play?????.')
    
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='Player 1':
            
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if winner(theboard, player1_marker):
                display_board(theboard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn='Player 2'
        else:
            display_board(theboard)
            position=player_choice(theboard)
            place_marker(theboard, player2_marker, position)
            if winner(theboard, player2_marker):
                display_board(theboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


