#half dollars, quarters, dimes, nickels and pennies. How many ways to
#give change for 1 dollar.

def changeCount(n, types):
    if n == 0:
        return (1)
    if n < 0:
        return (0)
    if len (types)==0:
        return(0)
    else:
        return(changeCount(n, types[1:])+changeCount(n-types[0], types[0:]))


types = (50, 25, 10, 5, 1)
n= 11
print (changeCount(n,types))
