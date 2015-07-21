"""
A male first name generator.

The program sifts through a list of about 3,800 male names from
english speaking countries. User is asked to enter the (integer)
number of first names they would like to have generated.

Credit for the list of names goes to Grady Ward (Project Gutenberg)
See the aaPG-Readme.txt in the directory for more information.

David Siah 5/29/14
"""
import random

lines = open('MaleNames.txt').read().splitlines()

def chooseM(iter):
    for i in range(iter):
        chosenName = random.choice(lines)
        print chosenName

raw = int(raw_input("How many first names would you like?\n"))

chooseM(raw)
