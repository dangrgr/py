a = 10
b = 20
c = 30

'''// Base Syntax for if conditional statements

if expression: 
    statement
    statement
    statement
elif expression:
    statement
    statement
    statement
else:
    statement
    statement
    statement

Outside of conditional

//'''

if a == 10:
    print "a is %s" % a

    if b == 20:
        print "b is 20"
    elif c == 30:
        print 'c is 30'
    else:
        if True:
            print 'whatever'  #Try not to nest 3 levels or more

else:
    print 'main else'

print 'outside of if'
