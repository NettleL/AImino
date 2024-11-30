number = int(input("NUMBER: "))
numberfac = number
while number != 1:
    number = number - 1
    numberfac = numberfac * number
    
print('FACTORIAL:', numberfac)
print('')