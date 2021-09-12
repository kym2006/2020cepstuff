import turtle
import random
import time

#the great marble race
print("SEE IF YOU'RE FASTER THAN A FOR LOOP!")
colors = ['blue', 'red', 'yellow', 'purple', 'green', 'orange']
random.shuffle(colors)#get a random list
marbles = []

for i in range(len(colors)):
    now = turtle.Turtle()#initialize turtle
    now.shapesize(0.3)#change size
    now.shape('circle')#change the shape
    now.penup()#invis
    now.color = colors[i]#change color
    now.pencolor(colors[i])#change color
    marbles.append(now)#add it to list
height = 200
for t in marbles:
    t.goto(-200,height)#go to this position
    height -= 66.6#decrease the height

user = turtle.Turtle()
user.shapesize(0.3)
user.shape('turtle')
user.penup()
user.color('black')
user.pencolor('black')
user.goto(-200,height)#settings for the user's turtle(the bottom left one)

def press(a,b):
    user.forward(5)

turtle.onscreenclick(press)

for turn in range(100):
    for i in marbles:
        i.forward(random.randint(1,5))

def fun(a,b):
    pass
turtle.onscreenclick(fun)
pos = user.xcor()#get how far the user travelled, compare with the furthest turtle
'''
for turn in range(1000):
    for i in marbles:
        i.forward(random.randint(1,5))
'''
big = -200
for t in marbles:
    big = max(big,t.xcor())
if pos>big:
    user.write("YOU WIN!")
else:
    user.write("You SLOW :(!")


turtle.done()