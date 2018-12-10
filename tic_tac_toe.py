'''
Milestone project #1 - Tic Tac Toe game
'''
import random 


def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def start_game():
	while True:
		print 'Starting Tic Tac Toe game\n'
		game_on = True
		board = [' '] *10
		p_turn = random.randint(0,1)
		p1_mark, p2_mark = player_mark()
		while game_on:
			if p_turn == 0:
				print 'It is Player 1 turn\n'
				p_pos = get_player_input(board)
				board = place_player_input(board, p1_mark, p_pos)
				display_board(board)
				player1_win = check_game_state(board, p1_mark)
				if player1_win:
					game_on = False
					print 'Player 1 wins!!!\n'
				else:
					 draw = check_full_board(board)
					 if draw:
					 	print 'Its a Tie!!!\n'
					 	break
				p_turn = 1
			else:
				print 'It is Player 2 turn\n'
				p_pos = get_player_input(board)
				board = place_player_input(board, p2_mark, p_pos)
				display_board(board)
				player2_win = check_game_state(board, p2_mark)
				if player2_win:
					game_on = False
					print 'Player 2 wins!!!\n'
				else:
					 draw = check_full_board(board)
					 if draw:
					 	print 'Its a Tie!!!\n'
					 	break
				p_turn = 0

		else:
			if not game_over():
				break

def player_mark():
	'''
	Player mark choices
	'''
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = raw_input('Do you want to play with X or O: ').upper()
	if marker == 'X':
		return ('X', 'O')
	elif marker == 'O':
		return ('O', 'X')

def get_player_input(board):
	'''
	Takes player input and returns player marker and board position.
	'''
	board_position = None
	while True:
		board_position = raw_input('Enter free board position between 1 and 9: ')
		if board_position in [str(x) for x in xrange(1, 10)] and board[int(board_position)] == ' ':
			board_position = int(board_position)
			break
	return board_position
	
def check_full_board(board):
	'''
	Checks if the game board have free spots.
	'''
	for i in xrange(1, len(board)):
		if not (board[i] == 'X' or board[i] == 'O'):
			return False
	else:
		return True

def place_player_input(board, p_marker, p_board_pos):
	'''
	Takes player marker and board position 
	and places it on the marker
	'''
	board[p_board_pos] = p_marker
	return board

def check_game_state(board, mark):
	'''checks game status'''
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or
	    (board[4] == mark and board[5] == mark and board[6] == mark) or
	    (board[1] == mark and board[2] == mark and board[3] == mark) or
	    (board[7] == mark and board[4] == mark and board[1] == mark) or
	    (board[8] == mark and board[5] == mark and board[2] == mark) or
	    (board[9] == mark and board[6] == mark and board[3] == mark) or
	    (board[7] == mark and board[5] == mark and board[3] == mark) or
	    (board[9] == mark and board[5] == mark and board[1] == mark))

def game_over():
	'''
	Ends the game, prints the results and starts a new game.

	'''
	user_input = ''
	while not (user_input == 'y' or user_input == 'n'):
		user_input = raw_input('Do you want to start a new game (Y, N)?: ').lower()
	if user_input ==  'y':
		start_game()
	else:
		return False

if __name__ == '__main__':
	start_game()