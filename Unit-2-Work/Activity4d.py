pet1 = {
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '419a Windsor Road, Baulkham Hills, 2153',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}
pet2 = {
'name' : 'Ronnie',
'animal category' : 'Bat',
'age' : 30,
'vaccinated' : True,
'credit card' : '4321 3457 6232 3243',
'billing address' : '1 Winston Court, Baulkham Hills, NSW 2153',
'owner name' : 'Annette Jinkins',
'account balance' : 921.59,
}
pet3 = {
'name' : 'Nonnie',
'animal category' : 'Narwhal',
'age' : 25,
'vaccinated' : False,
'credit card' : '4321 1234 4321 1234',
'billing address' : '419b Windsor Road, Baulkham Hills, 2153',
'owner name' : 'Anne Jonkins',
'account balance' : 599.21,
}

newname= {'name':'Connie'}
pet1.update(newname)

oldage = pet1['age'] 
newage = {'age': oldage + 1}
pet1.update(newage)

print(pet1['name'])
print(pet1['age'])

