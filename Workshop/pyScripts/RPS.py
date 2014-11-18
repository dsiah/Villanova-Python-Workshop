# Learning Control Flow: Pt. 1
import random

# Our game logic is placed into this function
def verboseMatchUp (player):
	# this is the *easy* solution -- this solution style does not scale well
	computer = random.randrange(1, 4)

	# What a mess :S
	if (player == 1 and computer == 3):
		print "You win!", "computer played: ",computer
	elif (player == 1 and computer == 2):
		print "You lose :(", "computer played: ",computer
	elif (player == 2 and computer == 3):
		print "You lose :(", "computer played: ",computer
	elif (player == 2 and computer == 1):
		print "You win!", "computer played: ",computer
	elif (player == 3 and computer == 2):
		print "You win!", "computer played: ",computer
	elif (player == 3 and computer == 1):
		print "You lose :(", "computer played: ",computer	
	else:
		print "Tie.", "computer played: ",computer

# Escape characters \n is newline and \t is tab
print "Welcome, lets play RPS\n\tRock = 1; Paper = 2; Scissor = 3"

# raw_input allows us to provide a prompt to the user and accept that answer
user = raw_input('>')
# convert user (which is a string) to an integer
user = int(user)
# Run the game
verboseMatchUp(user)