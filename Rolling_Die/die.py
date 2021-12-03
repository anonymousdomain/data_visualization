from random import randint


class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()
results = []
for sides in range(100):
    result = die.roll()
    results.append(result)

frquencies=[]

for value in range(1,die.num_sides+1):
    frquency=results.count(value)
    frquencies.append(frquency)
    
print(frquencies)
