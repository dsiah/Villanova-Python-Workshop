# how to snippets of code that serve as patterns to use when programming
condition = True
condition2 = False 

#if 
if (condition):
	#do stuff
	print "Stuff"

#if/elif/else
if (condition):
	print condition
elif (condition2):
	print condition2
else:
	print "Catch all"

#defining functions  
def nameofFunc (argument):
	# argument is optional 
	# do stuff with argument
	print argument

# This can get confusing -- a list can hold lists and dictionaries
# they index at 0
list1 = ["hi", [1, 2, 3], 4]

# Woah this is a pretty loaded expression
# for [ variable name ] in [ set ]:
#     do stuff --> then x gets incremented	
for x in range(0, len(list1)):
	print list1[x]