import random

class Dice:
    def roll():
        return (random.randint(1,6),random.randint(1,6))


roll= Dice.roll()
print(roll)
