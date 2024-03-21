#Will use in quiz - to visualise the score of the user after each question
import os
import time

def title():
    print('''
ASSESSMENT TASK 1 - MOVING BAR TEST
 ___  __        __       ___    __                   __   ___  __   ___  ___  __  ___ 
|__  |  \ |  | /  `  /\   |  | /  \ |\ |    |  |\/| |__) |__  |__) |__  |__  /  `  |  
|___ |__/ \__/ \__, /~~\  |  | \__/ | \|    |  |  | |    |___ |  \ |    |___ \__,  |  
                                                                               
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
    time.sleep(1)
    os.system('cls')
    title()
# I used the for loop to test if the changing of the bar works, 
 