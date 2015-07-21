iterate = int(raw_input('Enter integer:\n'))

def pretty(iterate):
    for i in range(1, iterate):
        print '#' * i
    print
    for i in range(1, iterate):
        print '#' * (iterate - i)

pretty(iterate)
