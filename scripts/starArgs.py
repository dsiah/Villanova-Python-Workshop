def endless(*args):
    for arg in args:
        if type(arg) is str:
            print arg
        elif type(arg) == list:
            for i in arg:
                print i,

endless('a', 'b', 'c')

listomania = ['d', 'e', 'f']

endless(listomania)
