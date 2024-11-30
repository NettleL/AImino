name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '419a Windsor Road, Baulkham Hills, 2153'
owner_name = 'Alex Nguyen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False

def changebalance(balance, change):
    balance = balance + change
    return balance

def vaxxstatus(name, vaccinated, change):
    if vaccinated == True:
        if change == 'unvaxxed':
            vaccinated == False
            return(f'{name} is no longer vaccinated')
        else:
            return(f'{name} is vaccinated')
    if vaccinated == False:
        if change == 'vaxxed':
            vaccinated == True
            return(f'{name} is vaccinated')
        else:
            return(f'{name} is not vaccinated')

        
    

help()
increase_age()
print(age)
verify_credit_card('1234 4334 1001 0000')

ccardinput = input('Credit Card (xxxx xxxx xxxx xxxx): ')
if verify_credit_card(ccardinput) == True:
    print('Card Accepted')
    ccard = ccardinput
    account_balance = round(changebalance(account_balance, -39),2)
    

print(vaxxstatus('Bonnie', vaccinated, 'vaxxed'))


#print(account_balance)