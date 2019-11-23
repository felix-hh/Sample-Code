


### How many ways do we have to give 100 cents change with half dollars, quarters, dimes, nickels and pennies?


listOfCoins = [50,25,10,5,1]
n=100

def countWays(n, listOfCoins):
    if n<0:
        return 0
    if len(listOfCoins)==0:
        return 0
    if n==0:
        return 1
    else:
        return (countWays(n-listOfCoins[0], listOfCoins) + countWays (n, listOfCoins[1:]))


print(countWays(n, listOfCoins))
    
