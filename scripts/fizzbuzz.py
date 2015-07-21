n = int(raw_input())

def fizzbuzz(n):
    for x in range(n):
        if x == 0:
            continue
        elif x % 3 == 0 and x % 5 == 0:
            print 'FizzBuzz'
        elif x % 3 == 0:
            print 'Fizz'
        elif x % 5 == 0:
            print 'Buzz'
        else:
            print x

fizzbuzz(n)
