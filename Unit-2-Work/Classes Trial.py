class Turtle:
	def __init__(self, name, colour):
		self.name = name
		self.colour = colour
		self.position = 1
		print(self.name, self.colour, self.position)
	def move(self, distance):
		self.position = self.position + distance
		print(self.name, "new distance",  self.position)
        
	def changeColour(self, colour):
		self.colour = colour
		print(self.name, "new colour",  self.colour)

turt1 = Turtle("Flatty", "green")
turt2 = Turtle("Loggie", "brown")
turt3 = Turtle("Hawksy", "beige")

turt1.move(5)
turt3.changeColour('hawk-colored')
