print('')
duration = int(input("Duration (hrs): "))
membership = input("Membership type: ")
dayinput = input("Day of the week? (mon/tue/wed/thurs/fri/sat/sun) ")

def checkweek(day):
    if day.lower() == 'mon' or day.lower() == 'tue' or day.lower() == 'wed' or day.lower() == 'thurs' or day.lower() == 'fri':
        return 'weekday'
    elif day.lower() == 'sat' or day.lower() == 'sun':
        return 'weekend'
    else:
        return 'idk'
    
if membership == 'platinum':
    if checkweek(dayinput) == 'weekday':
        print("First hour free and after that $2/ hour")
        print('Parking Fees = $' + str((duration-1)*2))
    elif checkweek(dayinput) == 'weekend':
        print("First 2 hours free and after that $1/ hour")
        print('Parking Fees = $' + str((duration-2)*1))
    elif checkweek(dayinput) == 'idk':
        print("I'm sorry, but", dayinput ,"is not a valid day")
    else:
        print('''Our program is not working right now. Please leave a message. We will ignore it :) ''')
        trash = input()
        
elif membership == 'gold':
    if checkweek(dayinput) == 'weekday':
        print('first hour free and after that $2.5/ hour')
        print('Parking Fees = $' + str((float(duration)-1)*2.5))
    elif checkweek(dayinput) == 'weekend':
        print('first 2 hours free and after that $2.5/ hour')
        print('Parking Fees = $' + str((float(duration)-2)*2.5))
    elif checkweek(dayinput) == 'idk':
        print("I'm sorry, but", dayinput ,"is not a valid day")
    else:
        print('''Our program is not working right now. Please leave a message. We will ignore it :) ''')
        trash = input()
    
else:
    if checkweek(dayinput) == 'weekday':
        print("first hour free and after that $3/ hour")
        print('Parking Fees = $' + str((duration-1)*3))
    elif checkweek(dayinput) == 'weekend':
        print("first 2 hours free and after that $3/ hour")
        print('Parking Fees = $' + str((duration-2)*3))
    elif checkweek(dayinput) == 'idk':
        print("I'm sorry, but", dayinput ,"is not a valid day")
    else:
        print('''Our program is not working right now. Please leave a message. We will ignore it :) ''')
        trash = input()
        
