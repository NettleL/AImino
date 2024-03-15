#Will use in quiz - to visualise the score of the user after each question
import os
import time

def title():
    print('''
ASSESSMENT TASK 1 - MOVING BAR TEST
      ''')

title()
name = input('Enter Name: ')
score = 0
def bar(score,name): #defines the function that displays the bar
    newbar = (f'''{name}
______{'___'*score}
   {'   '*score} {score} |
______{'___'*score} 
          ''')
    # adds more length to bar 
    # ______
    #       |
    # ______
    # for each new score (bar becomes bigger/smaller based on score)
    return newbar

print('')
print(bar(score,name)) 
print(bar(score,'bot1')) 

for answer in range(9):
    score = score + 1
    print(bar(score,name))
    print(bar(score-1,'bot1'))
#    sleep(1) - WANT TO CLEAR SCREEN AFTER EVERY BAR - DOESN'T WORK - NEED TO FIX
#    clear()
#    title()
# I used the for loop to test if the changing of the bar works, 
 
