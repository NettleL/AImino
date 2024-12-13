mark = input('MARK: ')

while mark != '':
    markval = int(mark)
    if markval < 50:
        print('FAILURE')
    elif markval >= 50 and markval <60 :
        print('D')
    elif markval >= 60 and markval <70 :
        print('C')
    elif markval >= 70 and markval <80 :
        print('B')
    elif markval >= 80 and markval <90 :
        print('A')
    elif markval >= 90 and markval <101 :
        print('A+')
    else:
        print('LIAR')
    mark = input('MARK: ')

print('')