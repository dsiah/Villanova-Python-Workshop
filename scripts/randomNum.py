"""
Program that generates random PA phone numbers, and then copies the last
phone number in the program to your clipboard so you can paste it.

Input the number of phone numbers you want to generate (only integers please)

(Script utilizes Pyperclip)

- David Siah
"""

from random import randint, sample
import pyperclip

areaCodes = [215, 610, 484]

#str(num) replaced by sample(areaCodes, 1) which chooses a random
def phoneGen(user):
    useR = int(user)
    for i in range(useR):
        numberToCopy = (str(sample(areaCodes, 1)).replace('[','').replace(']','') +
        '-' + str(randint(100,999)) + '-' + str(randint(1000,9999)))
        print numberToCopy
        return numberToCopy

def phoneGenII(user):
    useR = int(user)
    for i in range(useR):
      numberToCopy = (str(sample(areaCodes, 1)).replace('[','').replace(']','') +
      '-' + str(randint(100,999)) + '-' + str(randint(1000,9999)))
      print numberToCopy
      if i == (user-1):
        pyperclip.copy(numberToCopy)

user = int(raw_input("# of phone numbers to generate (integers only): "))
phoneGenII(user)
finale = raw_input("Press Enter to Exit...")
