import requests
testing = 0
import random
import time
start_time = time.time()
grid = [[]]

mob_types = ['C', 'E', 'Z']  #Types of mobs
inventory = []# inventory
actions = ['m', 'h']# actions available
SIZE = 6 # size of map


def postreq(time_taken,username):#posting a request to google forms(for fun i guess)
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSf7vV7VB1IrV805TLdE_P7WYq7NWmTrbVpqJqiPHBOahJuGeQ/formResponse'
    form_data = {'entry.964781626':username,
            'entry.586933075':time_taken,
            'draftResponse':[],
            'pageHistory':0
    }
    user_agent = {'Referer':'https://docs.google.com/forms/u/0/d/e/1FAIpQLSf7vV7VB1IrV805TLdE_P7WYq7NWmTrbVpqJqiPHBOahJuGeQ/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(url, data=form_data, headers=user_agent)
    if r.status_code == 200:
        print("OK\n")
    else:
        print("Not OK... Form was not sent...")
    return

def print_grid():
	for row in grid:
		for elt in row:
			print("[{}]".format(elt), end='')
		print("")


def welcome():
	print("""
Welcome to Minecraft but it's 2d and you can't mine!
The results will be sent to a google forms, and at the end there will be a high score!
link to results: \nhttps://docs.google.com/spreadsheets/d/1CaXrtUaoG6W3SUOThs5PBPtwwI1bkkNtUsET0m-W0ks/edit?usp=sharing
This text-based project is very fun!
The way to give commands is to use verbs, followed by the parameter.
For example, to move left, you would type 
m\nl
Type the first letter of the command in lowercase.
You can move around using [m]ove [u]p, [d]own, [l]eft, [r]ight commands.
For the full list of commands, type [h]elp\n
When attacking(you move towards it and killed it),
Endermen will hit you for 1hp
Zombies will hit you for 1hp
Creepers will hit you for 2hp
When being attacked(the mob moved towards you)
Endermen will hit you for 3hp
Zombies will hit you for 4hp
Creepers will hit you for 5hp
""")


def get_pos(x, y): #Making sure that the index doesn't go lesser than 0 or more than 5
	if x < 0:
		x = SIZE - 1
	elif x >= SIZE:
		x = 0
	if y < 0:
		y = SIZE - 1
	elif y >= SIZE:
		y = 0
	return x, y


def main():
	endfight = False
	mobs = []
	xPos = 0
	yPos = 0
	health = 20
	welcome()
	name = input("A sign reads: What's your name?: (Enter your name): ")
	print("Welcome {}!".format(name))
	global grid
	grid = [['.' for j in range(SIZE)] for i in range(SIZE)]
	turn = 0
	grid[0][0] = 'X'
	while health > 0:
		turn += 1
		print_grid()
		print("TURN {}, TIME: {}s".format(turn, round(time.time() - start_time,3)))
		print("Inventory: ", inventory)
		print("Health: ", health)
		if inventory.count('Ender pearl') >= 4:
			endfight = True
			print("YOU HAVE SUMMONED THE ENDER DRAGON! FINISH HIM TO WIN!!!(The ender dragon likes to play scissors paper stone so beat him at that)")
			# clear the board
			for i in range(SIZE):
				for j in range(SIZE):
					if grid[i][j] != 'X':
						grid[i][j] = '.'
		while endfight:
			cmove = random.choice(["Stone", "Paper", "Scissors"])
			if testing:
				cmove = "Stone"
			pmove = input('What is your move?["Stone", "Paper", "Scissors"]: ')
			validchoice = ["Stone", "Paper", "Scissors"]
			while pmove not in validchoice:
				pmove = input("Enter a valid choice!: ")
			print("Ender dragon played {}".format(cmove))
			if pmove == cmove:
				print("DRAW!")
			elif pmove == "Scissors":
				if cmove == "Stone":
					print("YOU LOSE!")
					return
				else:
					print("YOU WIN!")
					print("Your time is {}".format(round(time.time() - start_time,3)))
					postreq(round(time.time() - start_time, 3), name)
					return
			elif pmove == "Paper":
				if cmove == "Scissors":
					print("YOU LOSE!")
					return
				else:
					print("YOU WIN!")
					print("Your time is {}".format(round(time.time() - start_time, 3)))
					postreq(round(time.time() - start_time, 3), name)
					return
			elif pmove == "Stone":
				if cmove == "Paper":
					print("YOU LOSE!")
					return
				else:
					print("YOU WIN!")
					print("Your time is {}s".format(round(time.time() - start_time, 3)))
					postreq(round(time.time() - start_time, 3),name)

					return

		action = input("Input action: ")
		while action not in actions:
			action = input("Input a valid action!: ")
		if action == 'm':
			direction = input("Which direction to move to?: ")
			while direction not in ['u','r','d','l']:
				direction = input("Enter valid direction,[u,l,d,r]")
			# movement of playe, see if the player meets a mob
			if direction == 'u': # going up
				grid[yPos][xPos] = '.'
				yPos -= 1
				xPos,yPos = get_pos(xPos,yPos)
			elif direction == 'r':# going right
				grid[yPos][xPos] = '.'
				xPos += 1
				xPos,yPos = get_pos(xPos,yPos)
			elif direction == 'd':# going down
				grid[yPos][xPos] = '.'
				yPos += 1
				xPos,yPos = get_pos(xPos,yPos)
			elif direction == 'l':# going left
				grid[yPos][xPos] = '.'
				xPos -= 1
				xPos,yPos = get_pos(xPos,yPos)
			else:
				assert False #it should not happen
			if grid[yPos][xPos] in mob_types:
				if grid[yPos][xPos] == 'C':
					health -= 2
					inventory.append("Gunpowder")
					print("BOOM! THE CREEPER EXPLODED!")
				elif grid[yPos][xPos] == 'Z':
					health -= 1
					inventory.append("Rotten flesh")
					print("You've slain a zombie.")
				else:
					health -= 1
					inventory.append("Ender pearl")
					print("You've slain an enderman")
				mobs = [cmob for cmob in mobs if cmob[1] != yPos or cmob[2] != xPos]
			grid[yPos][xPos] = 'X'
		if action == 'h':
			print("""
COMMANDS:
h -> DISPLAY THIS COMMAND
m -> MOVE TO A CERTAIN DIRECTION IN [u,l,d,r], which means up, left, down, right
Mobs in this game-> [C]reeper, [Z]ombie, [E]nderman. Your objective is to collect 4 ender pearls from killing the endermen, which will spawn the enderdragon.
You should try your best to avoid creepers and zombies, as they will damage you and make you lost health. Once you lose 10 health, you will automatically die and game over for you.
Writing 'h' also serves as skipping a turn, which means you don't have to move to wait for endermen to spawn.
""")
		if len(mobs) != 0 and random.randint(1, 10) == 1: #Despawned
			mobs.pop(0)
		if len(mobs) < 5 and random.randint(1, 3) == 1: #Spawn a new mob at a random location
			mobs.append([random.choice(['C','Z','E']),random.randint(0,5), random.randint(0,5)])
		for mob in mobs:
			if random.randint(1, 2) == 1:
				grid[mob[1]][mob[2]] = '.'
				y, x = get_pos(mob[1] + random.randint(0, 1), mob[2] + random.randint(0, 1))
				# print(mob[1],mob[2],y,x)
				if grid[y][x] in mob_types:
					# There's another mob here, remove that mob
					mobs = [cmob for cmob in mobs if cmob[1] != y or cmob[2] != x]
				elif grid[y][x] == 'X':
					# Player is here, damage the player
					if mob[0] == 'C':
						health -= 5
						inventory.append("Gunpowder")
						print("BOOM! THE CREEPER EXPLODED!")
					elif mob[0] == 'Z':
						health -= 4
						inventory.append("Rotten flesh")
						print("You've slain a zombie.")
					else:
						health -= 3
						inventory.append("Ender pearl")
						print("You've slain an enderman")
					continue
				mob[1], mob[2] = y, x
			grid[mob[1]][mob[2]] = mob[0]
			grid[yPos][xPos] = 'X'
	print("You have died.")

if __name__ == '__main__':
	main()
	k=input("you may close this window now")
