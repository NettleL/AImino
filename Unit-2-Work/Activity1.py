import os
from turtle import Turtle
from random import randint

# NOTE:     I ALSO FOUND THE WINNDER OF THE RACE
#           AND DREW THE CIRCLE AROUND THE WINNING TURTLES STARTING POINT IN THE TURLES COLOUR
#           AND I'M VERY PROUD OF IT :)
#


winner = [] #will hold scores of all turtles
    
    #Turtles - NOTE: all colours are biologically accurate I think :)
    
#Flatback Turtle
Flatback = Turtle()
Flatback.color('OliveDrab2')
Flatback.shape('turtle')
Flatback.penup()
Flatback.goto(-160, 100)
Flatback.pendown()

#Green Turtle
Green = Turtle()
Green.color('OliveDrab4')
Green.shape('turtle')
Green.penup()
Green.goto(-160, 70)
Green.pendown()

#Loggerhead Turtle
Loggerhead = Turtle()
Loggerhead.color('Orange4')
Loggerhead.shape('turtle')
Loggerhead.penup()
Loggerhead.goto(-160, 40)
Loggerhead.pendown()

#Hawksbill Turtle
Hawksbill = Turtle()
Hawksbill.color('LightGoldenrod3')
Hawksbill.shape('turtle')
Hawksbill.penup()
Hawksbill.goto(-160, 10)
Hawksbill.pendown()

    #Movement
for movement in range(100):
    Flatback.forward(randint(1,5))
    Green.forward(randint(1,5))
    Loggerhead.forward(randint(1,5))
    Hawksbill.forward(randint(1,5))

    #WINNER
    
#Finds final coordinates of turtles
flatbackpos = Flatback.pos()
greenpos = Green.pos()
loggerheadpos = Loggerhead.pos()
hawksbillpos = Hawksbill.pos()

#appends x-value of final coordinates to list
winner.append((flatbackpos[0], 'flatback'))
winner.append((greenpos[0], 'green'))
winner.append((loggerheadpos[0],'loggerhead'))
winner.append((hawksbillpos[0], 'hawksbill'))

#sorts lists
sortedwinner = sorted(winner)

#Finds name of turtle in last spot (i.e with furthest distance)
finalwinner = ((sortedwinner[3])[1])
print('WINNER: ', finalwinner)


coord = 0 #establishes coordinate variable
circol = 'white' #establishes circle fill colour variable

#Sets coordinates and fill colour of circle based on the winners colour and starting position
if finalwinner == 'flatback':
    coord = 100
    circol = 'olivedrab2'
elif finalwinner == 'green':
    coord = 70
    circol = 'olivedrab4'
elif finalwinner == 'loggerhead':
    coord = 40
    circol = 'orange4'
elif finalwinner == 'hawksbill':
    coord = 10
    circol = 'lightgoldenrod'



randomint = randint(10,50)
turtley = Turtle()
turtley.color('darkolivegreen', circol) #fills circle with the colour of the winning turtle
turtley.shape('blank') # Other possible shapes -> arrow, blank, circle, classic, square, triangle, turtle
turtley.width(5) #width of the shape
turtley.penup()
turtley.goto(-160, coord - randomint) #sets start of circle underneath starting point of winning turtle so that the circle is around the starting point of the winning turtle
turtley.pendown()
turtley.begin_fill()
turtley.circle(randomint)
turtley.end_fill()

input("Press Enter to close")

