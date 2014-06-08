
board = [ 1, 2, 3, 4, 5, 6, 7, 8,9]

def display_board(board):
	for i in range(0,9):
		if board[i]%3 == 0:
			print '%s %s' % (board[i], '|')
			print '_ _ _ _ _ _'
		else:
			 print '%s %s' % (board[i], '|')

display_board(board)

