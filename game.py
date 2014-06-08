class Game(Player):

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	def display_board(self):
		print '%s %s %s %s %s %s' % (self.board[0], '|', self.board[1], '|', self.board[2], '|')
		print '%s %s %s %s %s %s' % (self.board[3], '|', self.board[4], '|', self.board[5], '|')
		print '%s %s %s %s %s %s' % (self.board[6], '|', self.board[7], '|', self.board[8], '|')

	def win(self):
		WINNING_MOVES = ((0, 1, 2),(3, 4, 5), (6, 7, 8), (0, 3, 6),
                         (1, 4, 7), (2, 5, 8), (0, 4, 8),(2, 4, 6))

		if player1.getMoves() in WINNING_MOVES:
			print '', player1.name, 'won'
		elif player2.getMoves() in WINNING_MOVES:
			print '', player1.name, 'won'
		else:
			print 'Nobody won.'
