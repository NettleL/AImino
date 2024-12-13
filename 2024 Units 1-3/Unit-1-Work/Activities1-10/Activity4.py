print('')

print("~ WHILE LOOPS ~")
print('')
# 1. ------
print('1. WHILE LOOP 1-10 ')
print('')
number1 = 1
while number1 <=10:
    print(number1)
    number1 = number1 + 1
print('')

# 2. ------
print('2. HOW MANY TIMES CAN YOU DIVIDE A NUMBER BY 2 ')
print('')
ognumber2 = int(input('Enter a number: '))
number2 = ognumber2
numberofnumbers = 0
while number2/2 >= 1:
    print(number2,'÷ 2 =', number2/2)
    number2 = number2/2
    numberofnumbers = numberofnumbers + 1
    
print(f'You can divide {ognumber2} {numberofnumbers} times before it is less than 1')
print('')

# 3. ------ {INFINITE LOOP}
print('3. INFINTIE LOOP ')
print('')

print('~ FOR LOOPS ~')
print('')
# 4. ------
print('4. FOR LOOP 1-10 ')
print('')
for  number4 in range(10):
    print(number4 + 1)
print('')

# 5. ------
print('5. PRINT EVERY LETTER IN A WORD ')
print('')
string5 = input('Enter a word: ')
for letter in string5:
    print(letter)
print('')

# 6. ------
print('6. FOR LOOP 1-100 (weirdly) ')
print('')
for number6 in range(1,26,3):
    print(number6)
print('')
for number6 in range(30,101,5):
    print(number6)
print('')

