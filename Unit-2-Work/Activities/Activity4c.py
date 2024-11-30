Pet_name = 'Foxy'
Species =  'Dog'
Age = 8
Vaccination_Status = False 


pet_name = ['Foxy', 'Doggy', 'April', 'Glassy', 'Hootie ']
species = ['Dog', 'Fox', 'Mayfly', 'Glass Sponge', 'Blowfish']
age = ['8', '2', '0.00137', '10000', '3' ]
vaccination_status = [False, True, False, False, True]

def vaccinate(animal):
    if animal in pet_name:
        index = pet_name.index(animal)
        vaccination_status[index] = True
        print(f"{animal}'s vaccination status = {vaccination_status[index]}")
    else:
        print(f'{animal} not in records')

def remove(animal):
    if animal in pet_name:
        index = pet_name.index(animal)
        del pet_name[index]
        del species[index]
        del age[index]
        del vaccination_status[index]
        print(f"{animal} has been removed")
    else:
        print(f'{animal} not in records')  
    
vaccinate('Foxy')
remove('April')
