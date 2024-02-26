print('')
import random
humanmove = input("Scissors, Paper, Rock? ").lower()
movelist = ['scissors', 'paper', 'rock']

humancounter = 0
computercounter = 0
tiecounter = 0

def isvalid(humanmove):
    if humanmove in movelist:
        return 'valid'
    else:
        return 'invalid'

def WinOrLose(computermove, humanmove):
    if computermove == 'rock' and humanmove == 'paper':
        return 'humanwins'
    elif computermove == 'scissors' and humanmove == 'rock':
        return 'humanwins'
    elif computermove == 'paper' and humanmove == 'scissors':
        return 'humanwins'
    elif computermove == 'paper' and humanmove == 'rock':
        return 'computerwins'
    elif computermove == 'rock' and humanmove == 'scissors':
        return 'computerwins'
    elif computermove == 'scissors' and humanmove == 'paper':
        return 'computerwins'
    else:
        return 'tie'
    
    
while humanmove != '':
    if isvalid(humanmove) == 'valid': 
        computermove = random.choice(movelist)
        print('Computer:', computermove)
        print('Human:', humanmove)
        if WinOrLose(computermove, humanmove) == 'humanwins':
            print('You won!')
            humancounter = humancounter + 1
        elif WinOrLose(computermove, humanmove) == 'computerwins':
            print('You lost!')
            computercounter = computercounter + 1
        else:
            print('Tie') 
            tiecounter = tiecounter + 1
        print('')
        print("Your score:", humancounter)
        print("Computer score:", computercounter)
        print("Ties:", tiecounter)
        print('')
        humanmove = input("Scissors, Paper, Rock? ").lower()  
    else:
        humanmove = input("Invalid Move. Scissors, Paper, Rock? ").lower()
        
print("")
    
