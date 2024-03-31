import time, os
from colorama import Fore, Back, Style
from SubjectData import *
from Colour import *
#NOTE - WHAT ABOUT QUIZZZLET
subjectchoice = ''
activitychoice = ''

physicsscore = []
bioscore = []
chemscore = []

def clearscreen(): #clears screen
    if os.name == 'posix': #if os is Mac or Linux
        _ = os.system('clear')
    else: #if os is Windows
        _ = os.system('cls')
    #https://www.skillvertex.com/blog/clear-screen-in-python/#:~:text=If%20it's%20Linux%20or%20Mac,system('cls').

def cleartitle(): #clearsscreen + prints title
    clearscreen()
    print(f'''{colr('''
___  ___  __  ___       ___ ___ 
 |  |__  (__`  |  |    |__   |  
 |  |___ .__)  |  |___ |___  |''')}  

 ∘₊✧────────── 2.0 ──────────✧₊∘
                                                              
      ''')
    
def subjectchoicefunction():
    global subjectchoice
    subjectchoice = input(colr('SUBJECT CHOICE (1, 2, 3 or exit): '))
    while subjectchoice not in ['1', '2', '3', 'exit']:
        print('Please enter a valid response - 1, 2, 3, exit')
        subjectchoice = input(colr('SUBJECT CHOICE (1, 2, 3 or exit): '))
    return subjectchoice

def activitychoicefunction():
    global activitychoice
    activitychoice = input(colr('SECTION CHOICE (1, 2 or exit): '))
    while activitychoice not in ['1', '2', 'exit']:
        print('Please enter a valid response - 1, 2 or exit')
        activitychoice = input(colr('SECTION CHOICE (1, 2 or exit): '))
    return activitychoice

def answer(): #gets answer, checks validity of answer and returns answer when valid.
  ans = input('→ ')
  while ans not in ['a','b','c','d']:
    print('Invalid')
    ans = input('→ ')
  return ans

def questions(dict): #asks questions from dictionary, checks answer and adds score
  score = 0 #initial score
  tempqs = dict.copy() # creates a temporary dictionary copy (so questions can be deleted from tempdict after they are asked, but not from the actual dictionary - therefore it can be accessed when the quiz is reattempted.)
  while tempqs != {}: #while the temporary dictionary has not run out of questions
    qno = random.choice(list(tempqs.keys())) #picks a random key from dictionary
    print(tempqs[qno][0]) #prints the question
    print('')
    ans = answer() #answer function
    if ans == tempqs[qno][1]: #if answer is correct
     print('Correct')
     score = score + 1 #add 1 to score
    else:
      print('Wrong')
    del tempqs[qno] #deletes q. from tempdict so its not asked again in the quiz attempt
  return score 
  print('Done!')

def subjectfunction(subject):
    content = ''
    qeasy = {}
    qmid = {}
    qhard = {}
    if subject == 'physics':
        content = physicscontent
        qeasy = physicsqseasy
        qmid = physicsqseasy # MAKE THESE PHYSICS Qs MID
        qhard = physicsqseasy # MAKE THESE PHYSICS Qs MID
        finscore = physicsscore
    elif subject == 'bio':
        content = biocontent
    elif subject == 'chem':
        content = chemcontent
    cleartitle()
    print(activityinfo)
    activitychoicefunction()
    while activitychoice != 'exit':
        while activitychoice == '1':
            cleartitle()
            print(content)
            input(colr('Please enter in anything to continue: '))
            cleartitle()
            print(activityinfo)
            activitychoicefunction()
        while activitychoice == '2':
            cleartitle()
            ### ADD QUESTIONS INFORMATION
            sceasy = questions(qeasy)
            scmid = questions(qmid)
            schard = questions(qhard)
            finscore.append(sceasy + scmid + schard)
            print(finscore)
            input(colr('Please enter in anything to continue: '))
            cleartitle()
            print(activityinfo)
            activitychoicefunction()
    cleartitle()
    print(programinfo)
    subjectchoicefunction()


clearscreen()
#INITIAL TITLE
print(f'''
      
{colr('''                                                                                                           
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
''')}
All content is taken from Zhang, J. et al., Oxford Insight Science 8 student book, Victoria, Oxford University Press, 2014.

''')
time.sleep(1)
input(colr('Please enter in anything to start: '))
cleartitle()

name = input(colr('PLEASE ENTER YOUR NAME: ')) #gets name

programinfo = (f'''
Hello, {colr(name)}!
      
This program is divided into three sections
{colr('''
1. The Physical World
2. The Living World
3. The Chemical World
''')}
Please choose a section by entering the corresponding number below. Type in 'exit' to exit the program
      ''')

activityinfo = (f'''
This subject is divided into two sections
{colr('''
1. Content
2. Questions
''')}
Please choose a section by entering the corresponding number below. Type in 'exit' to exit the program
                ''')

print(programinfo)
subjectchoicefunction()

while subjectchoice != 'exit':
    #PHYSICS
    while subjectchoice == '1':
        subjectfunction('physics')
        
    # BIOLOGY
    while subjectchoice == '2':
        subjectfunction('bio')
    
    # CHEMISTRY
    while subjectchoice == '3':
        subjectfunction('chem')

clearscreen()
print(f''' 
                                                                                                                   *****           *****
                                                                                                                ****   ****     ****   ****
{colr("8 888888888o `8.`8888.      ,8' 8 8888888888             8 888888888o `8.`8888.      ,8' 8 8888888888  ")}       ***         *** ***         ***      
{colr("8 8888    `88.`8.`8888.    ,8'  8 8888                   8 8888    `88.`8.`8888.    ,8'  8 8888        ")}      **             ***             **
{colr("8 8888     `88 `8.`8888.  ,8'   8 8888                   8 8888     `88 `8.`8888.  ,8'   8 8888        ")}     **               *              **
{colr("8 8888     ,88  `8.`8888.,8'    8 8888                   8 8888     ,88  `8.`8888.,8'    8 8888        ")}     **                             **
{colr("8 8888.   ,88'   `8.`88888'     8 888888888888           8 8888.   ,88'   `8.`88888'     8 888888888888")}     ***                          **
{colr("8 8888888888      `8. 8888      8 8888                   8 8888888888      `8. 8888      8 8888        ")}        ***                      ***
{colr("8 8888    `88.     `8 8888      8 8888                   8 8888    `88.     `8 8888      8 8888        ")}          ***                  ***
{colr("8 8888      88      8 8888      8 8888                   8 8888      88      8 8888      8 8888        ")}            ****            ****
{colr("8 8888    ,88'      8 8888      8 8888                   8 8888    ,88'      8 8888      8 8888        ")}               ****       ****
{colr("8 888888888P        8 8888      8 888888888888           8 888888888P        8 8888      8 888888888888")}                  ***   ***
                                                                                                                           *****
                                                                                                                             *
{name.upper()}
''')










