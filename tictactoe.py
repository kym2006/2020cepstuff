def instruction():
	print("""
This is a Tic Tac Toe game.
Player 1 will be 'X' and player 2 will be 'o'
The position to place on the board will be as follow:
       1|2|3
       -----
       4|5|6
       -----
       7|8|9)
""")


def showBoard(state):

	print(state[0],state[1],state[2],sep='|')
	print(state[3],state[4],state[5],sep='|')
	print(state[6],state[7],state[8],sep='|')

def update_state(player, position,state):
	if player == 1:
		state[position-1] = 'x'
	elif player == 2:
		state[position-1] = 'o'

def whoWin(state, player):
	if state[0] == player and state[1] == player and state[2] == player:
		return player
	if state[3] == player and state[4] == player and state[5] == player:
		return player
	if state[6] == player and state[7] == player and state[8] == player:
		return player
	if state[0] == player and state[3] == player and state[6] == player:
		return player
	if state[1] == player and state[4] == player and state[7] == player:
		return player
	if state[2] == player and state[5] == player and state[8] == player:
		return player
	if state[0] == player and state[4] == player and state[8] == player:
		return player
	if state[2] == player and state[4] == player and state[6] == player:
		return player
	return "DRAW!"
def main():
	instruction()
	state = [
	'.','.','.',
	'.','.','.',
	'.','.','.'
	]
	last = 'x'
	while whoWin(state,last) == "DRAW!" and '.' in state:
		p1 = int(input("Player 1's move: "))
		while(state[p1-1] != '.'):
			p1 = int(input("Enter valid move for P1!"))
		update_state(1,p1,state)
		showBoard(state)
		last = 'x'
		if whoWin(state,'x') != "DRAW!":
			break
		if '.' not in state:
			break
		p2 = int(input("Player 2's move: "))
		while(state[p2-1] != '.'):
			p2 = int(input("Enter valid move for P2!"))
		update_state(2,p2,state)
		showBoard(state)
		last = 'o'
		if(whoWin(state,'o') != "DRAW!"):
			break
	if whoWin(state,last) == "DRAW!":
		print("DRAW!")
	else:
		print("{} won!".format(whoWin(state,last)))
	print("Thank you for playing this very fun game!")

main()