print('')
print("CALCULATOR - BASIC OPERATIONS")
print('')

no1 = float(input('Number 1: '))
no2 = float(input('Number 2: '))

# 1. ------
print(no1, '+', no2, '=', no1+no2)

# 2. ------
print(no1, '-', no2, '=', no1-no2)

# 3. ------
print(no1, 'x', no2, '=', no1*no2)

# 4. ------
print(no1, '÷', no2, '=', no1/no2)

# 5. ------
import math

# 6. ------
print('')
print("CALCULATOR - SQUARE ROOT")
print('')
squarerootno = float(input('Number: '))
print('The square root of', squarerootno, 'is', math.sqrt(squarerootno))

# 7. ------
print('')
print("CALCULATOR - HYPOTENUSE")
print('')
hypotenuseno1 = float(input('Number 1: '))
hypotenuseno2 = float(input('Number 2: '))
print('The hypotenuse of a triangle with sides ', hypotenuseno1, 'and', hypotenuseno2, 'is', math.hypot(hypotenuseno1, hypotenuseno2))

# 8. ------
print('')
print("CALCULATOR - CIRCLE")
print('')
radius = float(input('Radius: '))
print('The circumference of a circle with a radius of', radius, 'is', 2*math.pi*radius)

# 9. ------
print('')
print("CALCULATOR - SIMPLE INTEREST")
print('')
principalamount = float(input('Principal Amount: '))
interestrate = float(input('Interest Rate (%): '))
timeperiod = float(input('Time Period (years): '))
simpleinterest = principalamount * (interestrate/100) * timeperiod
print(f'The simple interest accumulateed on ${principalamount} at an interest rate of {interestrate}% over {timeperiod} years is ${simpleinterest}', )
print('')

print('~ THE END ~')
print('')