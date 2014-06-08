class Game:

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	def display_board(self):
		print '%s %s %s %s %s %s' % (self.board[0], '|', self.board[1], '|', self.board[2], '|')
		print '%s %s %s %s %s %s' % (self.board[3], '|', self.board[4], '|', self.board[5], '|')
		print '%s %s %s %s %s %s' % (self.board[6], '|', self.board[7], '|', self.board[8], '|')

	


