#smallest divisor

def smallestDivisor (number,n):
    if number%n ==0:
        return (n)
    else:
        return(smallestDivisor (number, nextt(n)))

def nextt (n):
    if n == 2:
        return 3
    else:
        return n+2





print(smallestDivisor (1999,2))
