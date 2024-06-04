class Pet:
    def __init__(self, name, category, vaxx, ccard, age = 3):
        self.name = name
        self.category = category
        self.vaxx = vaxx
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

def __str__(self):
    my_status = f'''Name: {self.name}
Payment details = {self.ccard}
Vaccinated Status = {self.vaxx}
    '''
    return my_status

Bonnie = Pet("Bonnie", 'cat', "True", '', '4')
print(__str__(Bonnie))