# Roll a die using the "random" library
import random

# This is the roll_dice funtion.
# This function takes an input value
# which is the number of sides of the die.
# The number of sides defaults to the integer 6.
def roll_dice(sides=6):
    return random.randrange(sides) + 1

# Now we can see the output of a rolled
# die with a particular number of sides
print roll_dice()  # This has 6 sides, by default
print roll_dice(8)
print roll_dice(24)
