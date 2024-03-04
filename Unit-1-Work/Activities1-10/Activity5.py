print('')
# 1. ------
print('1. A QUARTER OF A YEAR')
print('')
month1 = int(input('Enter the month as a number between 1-12: '))
if month1 in range(1,4):
    if month1 == 1:
        print(f"The 1st month of the year is in the 1st quarter of the year")
    if month1 == 2:
        print(f"The 2nd month of the year is in the 1st quarter of the year")
    if month1 == 3:
        print(f"The 3rd month of the year is in the 1st quarter of the year")
elif month1 in range(4,7):
    print(f"The {month1}th month of the year is in the 2nd quarter of the year")
elif month1 in (7,10):
    print(f"The {month1}th month of the year is in the 3rd quarter of the year")
elif month1 in (10,13):
    print(f"The {month1}th month of the year is in the 4th quarter of the year")
else:
    print('ERROR: invalid input')
    
print('')
# 2. ------
print('2. ROMAN NUMERALS')
print('')  
rnlist = ['O', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
rninput = int(input('Enter a number between 1-10: '))


if rninput in range(1,11):
    print(f'The roman numeral for {rninput} = {rnlist[rninput]}')
else:
    print('ERROR: invalid input')
    
print('')

# 3. ------
print('3. MAGIC DATES')
print('')
day3 = int(input('Please enter in a date in numberical form: '))
month3 = int(input('Please enter in a month in numberical form (1-12): '))
year3 = int(input('Please enter in a year in numberical form (two digits): '))

if month3*day3 == year3:
    print('It is a magic date!')
else:
    print('It is not a magic date')
print('')  

# 4. ------
print('4. VALID NUMBER INFORMATION')
print('')
nolist4 = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
nolistfinal4 = []
for no4 in nolist4:
    if no4 in range(0,101):
        nolistfinal4.append(no4)

print(f'The average of the numbers of the list in the range 0-100 = {sum(nolistfinal4)/len(nolistfinal4)}')

print('')

# 5. ------
print('5. SENTENCE CAPITALISER')
print('')
finalstrings = ''
sentences5 = input('Enter a few sentences: ')
splitsentences5 = sentences5.split('. ')
for sentences in splitsentences5:
    finalstrings = finalstrings + sentences.capitalize() + '. '
print(finalstrings)