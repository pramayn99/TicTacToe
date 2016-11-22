from IPython.display import clear_output

board=[' ']*10
game_state=True
announce=''

def reset_Board():
	global board,game_state
	board=[' ']*10
	game_state=True

def display_Board():
	clear_output()
	print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
	print "-----------"
	print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
	print "-----------"
	print " "+board[1]+" | "+board[2]+" | "+board[3]+" "

def win_check(board,player):
	if (board[7]==board[8]==board[9]==player) or\
		(board[4]==board[5]==board[6]==player) or\
		(board[1]==board[2]==board[3]==player) or\
		(board[7]==board[5]==board[3]==player) or\
		(board[9]==board[5]==board[1]==player) or\
		(board[7]==board[4]==board[1]==player) or\
		(board[8]==board[5]==board[2]==player) or\
		(board[9]==board[6]==board[3]==player):
		return True
	else:
		return False

def full_Board_check(board):
	if " " in board[1:]:
		return False
	else:
		return True

def ask_player(mark):
	global board
	req='Choose where to place your '+mark+':'
	while True:
		try:
			choice=int(raw_input(req))
		except ValueError:
			print("Sorry,Please input a number between 1 to 9.")
			continue

		if board[choice]==' ':
			board[choice]=mark;
			break;
		else:
			print "That space isn't empty!"
			continue
			
def player_choice(mark):
	global board,game_state,announce
	announce=''
	mark=str(mark)
	ask_player(mark)

	if win_check(board,mark):
		clear_output()
		display_Board()
		announce=mark+" wins! Congratulations."
		game_state=False

	clear_output
	display_Board()

	if full_Board_check(board):
		announce='Tie!'

	return game_state,announce

def play_game():
	reset_Board()
	global announce

	X='X'
	O='O'
	display_Board()
	while True:
		clear_output()
		

		game_state,announce=player_choice(X)
		print announce
		if game_state==False:
			break

		game_state,announce=player_choice(O)
		print announce
		if game_state==False:
			break

	rematch=raw_input('Would you like to play again?y/n:')
	if rematch=='y':
		play_game()
	else:
		print 'Thanks for playing!'

play_game()




