import time, os
from colorama import Fore, Back, Style

#NOTE - WHAT ABOUT QUIZZZLET

subjectchoice = ''

def clearscreen(): #clears screen
    if os.name == 'posix': #if os is Mac or Linux
        _ = os.system('clear')
    else: #if os is Windows
        _ = os.system('cls')
    #https://www.skillvertex.com/blog/clear-screen-in-python/#:~:text=If%20it's%20Linux%20or%20Mac,system('cls').

def title(): #prints title (used after screen is cleared)
    clearscreen()
    print('''
___  ___  __  ___       ___ ___ 
 |  |__  (__`  |  |    |__   |  
 |  |___ .__)  |  |___ |___  |  

 ∘₊✧────────── 2.0 ──────────✧₊∘
                                                              
      ''')

def subjectchoicefunction():
    global subjectchoice
    subjectchoice = input('SUBJECT CHOICE: ')
    while subjectchoice not in ['1', '2', 'exit']:
        print('Please enter a valid number - either 1 or 2 or exit')
        subjectchoice = input('SUBJECT CHOICE: ')
    return subjectchoice

title()
print('ENTER SUBJECT CHOICE')
subjectchoicefunction()

while subjectchoice != 'exit':
    #PHYSICS SHOULD I DO A WHILE LOOP??
    while subjectchoice == '1': #MAYBE DO A DOUBLE CHECK - I.E ARE YOU SURE
        print('')
        print('Physics')
        time.sleep(1)
        title()
        print('PHYS STUFF')
        subjectchoicefunction()
    

    # EARTH AND SPACE  SHOULD I DO A WHILE LOOP??
    while subjectchoice == '2':
        print('')
        print('Earth and Space')
        time.sleep(1)
        title()
        print('E+S STUFF')
        subjectchoicefunction()

clearscreen()
print('BYEBYE')