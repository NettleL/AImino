import time, os
from colorama import Fore, Back, Style
from SubjectData import *

#NOTE - WHAT ABOUT QUIZZZLET
subjectchoice = ''

def clearscreen(): #clears screen
    if os.name == 'posix': #if os is Mac or Linux
        _ = os.system('clear')
    else: #if os is Windows
        _ = os.system('cls')
    #https://www.skillvertex.com/blog/clear-screen-in-python/#:~:text=If%20it's%20Linux%20or%20Mac,system('cls').

def cleartitle(): #clearsscreen + prints title
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

def subjectchoicefunction():
    global subjectchoice
    subjectchoice = input('SUBJECT CHOICE (1,2,3 or exit): ')
    while subjectchoice not in ['1', '2', '3', 'exit']:
        print('Please enter a valid response - 1, 2, 3, exit')
        subjectchoice = input('SUBJECT CHOICE (1,2,3 or exit): ')
    return subjectchoice

clearscreen()
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

All content is taken from Zhang, J. et al., Oxford Insight Science 8 student book, Victoria, Oxford University Press, 2014.
      ''')

time.sleep(4)
cleartitle()

name = input('PLEASE ENTER YOUR NAME: ') #gets name

programinfo = (f'''Hello, {name}!
      
This program is divided into three sections
1. The Physical World
2. The Living World
3. The Chemical World

Please choose a section by entering the corresponding number below. Type in 'exit' to exit the program
      ''')

print(programinfo)
subjectchoicefunction()

while subjectchoice != 'exit':
    #PHYSICS
    while subjectchoice == '1':
        print('')
        print('Physics')
        time.sleep(1)
        cleartitle()
        print(physicscontent)
        ### TEST - GOING BACK TO HOME SCREEN
        input('')
        cleartitle()
        print(programinfo)
        subjectchoicefunction()
        
    # BIOLOGY
    while subjectchoice == '2':
        print('')
        print('Biology')
        time.sleep(1)
        cleartitle()
        print('BIO STUFF')
        ### TEST - GOING BACK TO HOME SCREEN
        time.sleep(2)
        cleartitle()
        print(programinfo)
        subjectchoicefunction()
    
    # CHEMISTRY
    while subjectchoice == '3':
        print('')
        print('Chemistry')
        time.sleep(1)
        cleartitle()
        print('CHEM STUFF')
        ### TEST - GOING BACK TO HOME SCREEN
        time.sleep(2)
        cleartitle()
        print(programinfo)
        subjectchoicefunction()

clearscreen()
print('BYEBYE')