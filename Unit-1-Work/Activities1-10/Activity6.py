# pip install tabulate - if not working, maybe try this
# https://www.statology.org/create-table-in-python/
from tabulate import tabulate
import os


def clearscreen(): #clears screen
    print('PRESS ENTER TO CONTINUE')
    input()
    if os.name == 'posix': #if os is Mac or Linux
        _ = os.system('clear')
    else: #if os is Windows
        _ = os.system('cls')
    #https://www.skillvertex.com/blog/clear-screen-in-python/#:~:text=If%20it's%20Linux%20or%20Mac,system('cls').

clearscreen()

# 1. ------
print('1. BINARY VALUES 0-16')
print('')
data1 = []
for integer1 in range(17):
    data1.append(tuple((integer1, bin(integer1))))
print(tabulate(data1, headers=['Decimal', 'Binary'], tablefmt="fancy_grid"))
print('')
clearscreen()

# 2. ------
print('2. DECIMAL TO BINARY')
print('')
input2 = int(input('Decimal: '))
print('Binary:',bin(input2))
print('')
clearscreen()

# 3. ------
print('3. HEXADECIMAL VALUES 0 - 15')
print('')
data3 = []
for integer3 in range(16):
    data3.append(tuple((integer3, hex(integer3))))
print(tabulate(data3, headers=['Decimal', 'Hexadecimal'], tablefmt="fancy_grid"))
print('')
clearscreen()

# 4. ------
print('4. DECIMAL TO HEXADECIMAL')
print('')
input4 = int(input('Decimal: '))
print('Hexadecimal:',hex(input4))
print('')
clearscreen()

# 5. ------
print('5. STRING TO DECIMAL INTEGER')
print('')
input5 = input('String: ')
print(int(input5, 10))
print('')
clearscreen()

# 6. ------
print('6. BINARY + HEXADECIMAL')
print('')
dec6 = 0
bin6 = 0
hex6 = 0
data6 = []
columnnames6 = ['Decimal', 'Binary', 'Hexadecimal']
for integer6 in range(1, 256):
    dec6 = integer6
    bin6 = bin(integer6)
    hex6 = hex(integer6)
    data6.append(tuple((dec6,bin6,hex6)))
#print(data6)
print(tabulate(data6, headers=columnnames6, tablefmt="fancy_grid"))
clearscreen()

print('')
print('THE END :)')