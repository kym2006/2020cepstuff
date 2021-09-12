SIZE = 4
import pprint
import random
def createNull(row, col):
    return [[0 for i in range(col)] for j in range(row)]
def printBoard(state):
	'''prints each element. Takes up 5 spaces in total'''
	for i in range(SIZE):
		for j in range(SIZE):
			print("{}".format(str((state[i][j],'-')[state[i][j]==0]) + " "*(5-len(str(state[i][j])))),end='')
		print('')

def move(state, direction):
	done = createNull(SIZE,SIZE)
	if direction == 'u':
		for times in range(10): #try to "relax" for 10 times(this is too much but ok)
			for j in range(SIZE):
				for i in range(1,SIZE):
					if done[i][j]:
						continue
					elif state[i][j] == 0:
						continue
					elif state[i-1][j] == 0:
						state[i-1][j] = state[i][j]
						state[i][j] = 0
					elif state[i-1][j] == state[i][j] and done[i-1][j] == 0:
						state[i-1][j] += state[i][j]
						state[i][j] = 0
						done[i-1][j] = 1
	
	elif direction == 'l':
		for times in range(10):
			for i in range(SIZE):
				for j in range(1,SIZE):
					if done[i][j]:
						continue
					elif state[i][j] == 0:
						continue
					elif state[i][j-1] == 0:
						state[i][j-1] = state[i][j]
						state[i][j] = 0
					elif state[i][j-1] == state[i][j] and done[i][j-1] == 0:
						state[i][j-1] += state[i][j]
						state[i][j] = 0
						done[i][j-1] = 1
	
	if direction == 'r':
		for times in range(10):
			for i in range(SIZE):
				for j in range(SIZE-2,-1,-1):
					if done[i][j]:
						continue
					elif state[i][j] == 0:
						continue
					elif state[i][j+1] == 0:
						state[i][j+1] = state[i][j]
						state[i][j] = 0
					elif state[i][j+1] == state[i][j] and done[i][j+1] == 0:
						state[i][j+1] += state[i][j]
						state[i][j] = 0
						done[i][j+1] = 1
	elif direction == 'd':
		for times in range(10):
			for j in range(SIZE):
				for i in range(SIZE-2,-1,-1):
					if done[i][j]:
						continue
					elif state[i][j] == 0:
						continue
					elif state[i+1][j] == 0:
						state[i+1][j] = state[i][j]
						state[i][j] = 0
					elif state[i+1][j] == state[i][j] and done[i+1][j] == 0:
						state[i+1][j] += state[i][j]
						state[i][j] = 0
						done[i+1][j] = 1
						
												
			
	return state 

def genrand(state): 
	''' generates a random 2 or 4 anywhere on the board that is unfilled. '''
	li = []
	for i in range(SIZE):
		for j in range(SIZE):
			if state[i][j] == 0:
				li.append((i,j))
	coord = random.choice(li)
	state[coord[0]][coord[1]] = random.randint(1,2) * 2
	return state

def valid(state):
	cnt = 0
	for i in range(SIZE):
		for j in range(SIZE):
			cnt += state[i][j] == 0
	return not not cnt

def win(state):
	for i in range(SIZE):
		for j in range(SIZE):
			if state[i][j] == 2048:
				return True

def main():
	global SIZE
	SIZE = int(input("Input size of the board: "))
	state = createNull(SIZE,SIZE)
	state = genrand(state)
	while valid(state):
		printBoard(state)
		where = input("input your move: [u,l,d,r]: ")
		while where not in ['u','l','d','r']:
			where = input("input your move: [u,l,d,r]: ")
		state = move(state, where)
		
		if win(state):
			print("You won!")
		state = genrand(state)
	print("You lost!")


main()
