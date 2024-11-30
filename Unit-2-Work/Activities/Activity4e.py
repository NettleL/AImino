class pet:
    def __init__(self, name, species, age, vaxxed, ccard, address, owner='unknown', account=0):
        self.name = name
        self.species  = species
        self.age = age
        self.vaxxed = vaxxed
        self.ccard = ccard
        self.address = address
        self.owner = owner
        self.account = account

Bonnie = pet("Bonnie", 'cat', "4", "True", '4321 3457 6232 3243', '419a Windsor Road, Baulkham Hills, 2153', "Connie Connel", 1000)
Foxy = pet("Foxy", 'dog', "4", "True", '4321 3457 6232 3243', '419a Windsor Road, Baulkham Hills, 2153', "Connie Connel", 1000)
print(Bonnie.vaxxed)