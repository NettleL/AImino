# 1. Password Checker
print('''
----- PASSWORD CHECKER -----     
''')

def validUsername(username):
    usernameList = []
    for letter in username:
        usernameList.append(letter)
    if len(usernameList) >= 8 and usernameList[0].isupper() and usernameList[-2].islower() and usernameList[-1].isdigit():
        print(f'Username {username} is Valid')
    
validUsername('NESA24s3')

# 2. Timetable Maker
print('''
----- TIMETABLE -----      
''')


subjects = ['English Advanced', 'Maths Extension', 'Biology', 'Chemistry', 'Software Engineering']
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in dayList:
    print(day)
    for period in range(5):
        print(f'    Period {1+period}: {subjects[period]}')
    firstSubject = subjects[0]
    subjects.pop(0)
    subjects.append(firstSubject)
    
# 3. Pizza
print('''
----- PIZZA COST -----      
''')

orders = [('m',3),('l',2), ('s',4)]

def algorithm(order):
    totalCost = 0
    costList = []
    for letter, number in order:
        cost = 10
        if letter == 'm':
            cost += 2
        elif letter =='l':
            cost += 4
        cost += (number*1.5)
        costList.append(cost)
        totalCost += cost
    pizzanumber = 1
    for fincost in costList:
        print(f'Pizza {pizzanumber}: ${fincost}')
        pizzanumber += 1
    print(f'Total Cost: ${totalCost}')
    print('')
    
algorithm(orders)
        
