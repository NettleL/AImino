class Pet:
    def __init__(self, name, category, vaxx = False, age = 1):
        self.name = name
        self.category = category
        self.vaxx = vaxx
        self.age = age
        self.ccard = 'unknown'

p1 = Pet('Bonnie', 'Cat')
p2 = Pet('Clyde', 'Dog',age = 7)
p3 = Pet(category = 'Rabbit', name = 'Ruby', age = 13)
p4 = Pet('George','Cat',age = 6)
p5 = Pet('The Man In The Yellow Hat','Monkey',age = 12, vaxx = True)

petlist = [p1, p2, p3, p4, p5]
for pet in petlist:
    if pet.vaxx == False:
        print(f'{pet.name} is now vaccinated')
    else:
        print(f'{pet.name} was already vaccinated')

