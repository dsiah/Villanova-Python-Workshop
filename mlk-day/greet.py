# This is a super basic program which illustrates
# the difference between using "print" and "return"
# in functions. There's two different ways
# to achieve the same thing.

# Use print inside the function
def print_greet(name):
    print 'Hello ' + name

print_greet('Jack')
print_greet('Jill')
print_greet('Bob')

# Use return inside the function, and then
# use print afterwards 
def return_greet(name):
    return 'Hello ' + name
    
print return_greet('Jack')
print return_greet('Jill')
print return_greet('Bob')
