for x in range(1,100):
    factors = 0
    print('-------------')
    print('Number: ' + str(x))
    for i in range(1,x):
        if x%i == 0:
            print('--#>' + (str(i)))
            factors += 1
    print('Total: ' + str(factors))