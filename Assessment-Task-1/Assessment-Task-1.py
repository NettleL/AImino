import time, os
import random
from colorama import Fore, Back, Style
from SubjectData import * #Contains all subject data - e.g questions/answers + content
from Colour import * #Contains colour function (to colour text)

#Initiates global variable for while loops
subjectchoice = ''
activitychoice = ''

# STAT LISTS
# Will ontain user stats for respective subject quizzes - list of tuplets (time, score of each attempt)
physicsstats = []
biostats = []
chemstats = []

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
    
def subjectchoicefunction(): #Checks if subject choice is valid
    global subjectchoice
    subjectchoice = input(colr('SUBJECT CHOICE (1, 2, 3, 4 or exit): '))
    while subjectchoice not in ['1', '2', '3', '4', 'exit']: 
        print('Please enter a valid response - 1, 2, 3, 4 or exit')
        subjectchoice = input(colr('SUBJECT CHOICE (1, 2, 3, 4 or exit): ')) 
    return subjectchoice #returns valid subject choive

def activitychoicefunction(): #Checks if activity choice (content/quiz) is valid
    global activitychoice
    activitychoice = input(colr('SECTION CHOICE (1, 2 or exit): '))
    while activitychoice not in ['1', '2', 'exit']: 
        print('Please enter a valid response - 1, 2 or exit')
        activitychoice = input(colr('SECTION CHOICE (1, 2 or exit): ')) 
    return activitychoice #returns valid activity choice

def bar(score,name): #defines the function that displays the bar
    newbar = (f'''{colr(name)}
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

def answer(): #gets answer, checks validity of answer and returns answer when valid - similar to subject + activity choice functions
  ans = input('→ ')
  while ans not in ['a','b','c','d']:
    print('Invalid. Please enter in either a, b, c or d')
    ans = input('→ ')
  return ans

def questions(dict, score): #asks questions from dictionary, checks answer and adds score
    correct = ''
    tempqs = dict.copy() # creates a temporary dictionary copy (so questions can be deleted from tempdict after they are asked, but not from the actual dictionary - therefore it can be accessed when the quiz is reattempted.)
    while tempqs != {}: #while the temporary dictionary has not run out of questions
        print(bar(score, name)) #show the score on the progress bar
        qno = random.choice(list(tempqs.keys())) #picks a random key from dictionary
        print(tempqs[qno][0]) #prints the question
        print('')
        ans = answer() #answer function
        if ans == tempqs[qno][1]: #if answer is correct
            correct = colr('Correct')
            score = score + 1
        else: #If answer is wrong, show wrong and display explanation
            correct = (f'''{colr('Wrong')} 
{tempqs[qno][2]}''')
        del tempqs[qno] #deletes q. from tempdict so its not asked again in the quiz attempt
        cleartitle()
        print(correct) #prints either 'correct' or 'wrong + explanation
        print('')
    return score #returns total score of that quiz (i.e three questions)

def table(stats): #Creates a table based on stats
    print('''
+---------+----------+---------+
| ATTEMPT | TIME (s) |  SCORE  |
+---------+----------+---------+''') 
    attempt = 1 #IS AN INTEGER
    for stat in stats: #For every row needed
        if len(str(stat[0])) > 6: #If too many digits to align nicely
            alignedtime = 'ERROR!'
        else:
            alignedtime = str(stat[0]).ljust(6) #Aligns nicely - padding
        if attempt > 999:
            alignedattempt = attempt #After 999 attempts honestly i don't think they'll care if the tables messed up.
        else:
            alignedattempt = str(attempt).ljust(3) #Aligns nicely - padding
        print(f'''|  {colr(alignedattempt)}    |  {colr(alignedtime)}  |    {colr(str(stat[1]))}    |
+---------+----------+---------+''') #creates a new row
        attempt += 1

def alltables(subject,dictionary): #Just some formatting for Option 4. of main menu - scoreboards
    print(colr('─────'), bold(subject), colr('─────'))
    table(dictionary)
    if dictionary == []:
        print(f'''|            {colr('EMPTY')}             |
+---------+----------+---------+''')
    print('')
    
def subjectfunction(subject): #Main function for everything in a subject.
    content = '' #content of the subject selected
    qeasy = {}  #easy questions of the subject selected
    qmid = {}   #medium questions of the usbject selected
    qhard = {}  #hard questions of the subject selected
    
    #Establishes the content and questions for each subject
    if subject == 'physics': 
        content = physicscontent
        qeasy = physicsqseasy
        qmid = physicsqsmid
        qhard = physicsqshard
        finstats = physicsstats
    elif subject == 'bio':
        content = biocontent
        qeasy = bioqseasy
        qmid = bioqsmid
        qhard = bioqshard
        finstats = biostats
    elif subject == 'chem':
        content = chemcontent
        qeasy = chemqseasy
        qmid = chemqsmid
        qhard = chemqshard
        finstats = chemstats
    
    cleartitle()
    print(activityinfo) #activity menu
    activitychoicefunction() #asks user for activity choice and returns valid choice.
    while activitychoice != 'exit': 
        while activitychoice == '1': #content
            cleartitle()
            print(content) #prints content
            input(colr('Please enter in anything to continue: ')) #User can continue once they finished reading
            cleartitle()
            print(activityinfo) #returns to activity menu
            activitychoicefunction()
        while activitychoice == '2': #quiz
            cleartitle()
            print(questioninfo)
            input(colr('Please enter in anything to start the quiz: ')) #user can start when they want
            cleartitle()
            starttime = time.time() #timer starts
            sceasy = questions(qeasy, 0) #easy qs + gets score
            scmid = questions(qmid, sceasy) #medium qs + adds score to easyq score
            schard = questions(qhard, scmid) #hard qs + adds score to the easyq and midq score
            endtime = time.time() #timer stops
            total_time = endtime - starttime #IS FLOAT
            finstats.append(tuple([round(total_time,2),schard])) #appends the time and total score to the subject stats list
            #shows final score (on bar and directly)
            print(bar(schard,name))
            print(colr('FINAL SCORE ='), schard)
            #makes a pretty table
            table(finstats)
            print('')
            print('NOTE: If Time (s) displays (ERROR!), the attempt time was > 999999 seconds')
            input(colr('Please enter in anything to continue: ')) #user can continue whenever they want
            cleartitle()
            print(activityinfo) #activity menu
            activitychoicefunction()
    cleartitle()
    print(programinfo)
    subjectchoicefunction()

#_________________________________________________________________________________ MAIN
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
input(colr('Please enter in anything to start: ')) #User can continue at their own pace after reading disclaimer
cleartitle()

name = input(colr('PLEASE ENTER YOUR NAME: ')) #gets name

programinfo = (f'''
Hello, {colr(name)}!
      
This program is divided into four sections
{colr('''
1. Physics
2. Biology
3. Chemistry
4. Scoreboard
''')}
Please choose a section by entering the corresponding number below. Type in 'exit' to exit the program
      ''')

activityinfo = (f'''
This subject is divided into two sections
{colr('''
1. Content
2. Questions
''')}
Please choose a section by entering the corresponding number below. Type in 'exit' to exit this subject
                ''')

questioninfo = (f'''
There are 9 questions in a subject {colr('''
3 Easy
3 Medium
3 Hard''')}
This is timed {colr(':)')}
''')

print(programinfo)
subjectchoicefunction() #first subject choice

while subjectchoice != 'exit': #while the subject choice is not exit
    #PHYSICS
    while subjectchoice == '1': 
        subjectfunction('physics')
        
    # BIOLOGY
    while subjectchoice == '2':
        subjectfunction('bio')
    
    # CHEMISTRY
    while subjectchoice == '3':
        subjectfunction('chem')
    
    #SCOREBOARD
    while subjectchoice == '4':
        cleartitle() 
        if physicsstats == [] and biostats == [] and chemstats == []: #If the user has not attempted any quizzes
            print(f'{colr("DO A QUIZ!!! YOU'VE GOT THIS,")} {name.upper()}{colr('!')}')
        else:
            print(f'{colr("GOOD JOB,")} {name.upper()}{colr('!')}')
        print('')
        #makes pretty tables
        alltables(' PHYSICS ',physicsstats) 
        alltables(' BIOLOGY ',biostats)
        alltables('CHEMISTRY',chemstats)
        print('')
        input(colr('Please enter in anything to continue: ')) #user can continue when they want
        cleartitle()
        print(programinfo) #main menu
        subjectchoicefunction()
   
#END     
cleartitle()
print(colr('FINAL SCORES :)')) #final scores
print('')
alltables(' PHYSICS ',physicsstats)
alltables(' BIOLOGY ',biostats)
alltables('CHEMISTRY',chemstats)
print('')
input(colr('Please enter in anything to continue: '))

#END SCREEN
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

