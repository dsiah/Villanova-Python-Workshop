"""
A female first name generator.

The program sifts through a large list of about female names from
english speaking countries. User is asked to enter the (integer)
number of first names they would like to have generated.

Credit for the list of female names goes to Colin Mackay. List located in the
resource directory of the Xander.Password Validator.

David Siah 5/29/14
"""
import random

lines = open('FemaleNames.txt').read().splitlines()

def chooseF(iter):
    for i in range(iter):
        chosenName =random.choice(lines)
        capChosenName = chosenName.capitalize()
        print capChosenName

raw = int(raw_input("How many first names would you like?\n"))

chooseF(raw)
