import time, os
from colorama import Fore, Back, Style

#NOTE - WHAT ABOUT QUIZZZLET

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
    
def validity(input, parameter): #checks validity MIGHT NEED TO DELETE
    if parameter == 'num':
        return input.isnumeric()
    elif parameter == 'alpha':
        return input.isalpha()
    else:
        return 'ISSUE'
     

#INITIAL TITLE
print('''
      
                                                                                                                
8888888 8888888888 8 8888888888     d888888o. 8888888 8888888888 8 8888         8 8888888888 8888888 8888888888 
      8 8888       8 8888         .`8888:' `88.     8 8888       8 8888         8 8888             8 8888       
      8 8888       8 8888         8.`8888.   Y8     8 8888       8 8888         8 8888             8 8888       
      8 8888       8 8888         `8.`8888.         8 8888       8 8888         8 8888             8 8888       
      8 8888       8 888888888888  `8.`8888.        8 8888       8 8888         8 888888888888     8 8888       
      8 8888       8 8888           `8.`8888.       8 8888       8 8888         8 8888             8 8888       
      8 8888       8 8888            `8.`8888.      8 8888       8 8888         8 8888             8 8888       
      8 8888       8 8888        8b   `8.`8888.     8 8888       8 8888         8 8888             8 8888       
      8 8888       8 8888        `8b.  ;8.`8888     8 8888       8 8888         8 8888             8 8888       
      8 8888       8 888888888888 `Y8888P ,88P'     8 8888       8 888888888888 8 888888888888     8 8888       

DISCLAIMER: We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Quizlet
      ''')

time.sleep(2)
title()

name = input('PLEASE ENTER YOUR NAME: ') #gets name

print(f'''Hello, {name}!
      
This program is divided into four sections
1. The Physical World
2. Earth and Space
3. The Living World
4. The Chemical World

Please choose a section by entering the corresponding number below
      ''')

subjectchoice = input('SUBJECT CHOICE: ')
while subjectchoice not in ['1', '2', '3', '4']:
    print('Please enter a valid number - either 1, 2, 3 or 4')
    subjectchoice = input('SUBJECT CHOICE: ')

if subjectchoice == '1': #MAYBE DO A DOUBLE CHECK - I.E ARE YOU SURE
    print('')
    print('Physics')
    time.sleep(1)
    title()
elif subjectchoice == '2':
    print('')
    print('Earth and Space')
    time.sleep(1)
    title()
elif subjectchoice == '3':
    print('')
    print('BIOLOGY!!!!!!!!!')
    time.sleep(1)
    title()
elif subjectchoice == '4':
    print('')
    print('Chemistry')
    time.sleep(1)
    title()

