
#Input and init


#average



#abs error




#report
def estimateRoot(guess, n):
    def average(number1, number2):
        return ((number1+number2)/2)
    
    def absError(guess,n):
        x= guess*guess-n
        if x < 0:
            return -x
        else:
            return x
    #guess
    def improveGuess(guess,n):
        return (average(guess, n/guess))

    
    if absError(guess,n)>n*0.1:
        return (estimateRoot (average(guess, n/guess), n))
        
    else:
        return (guess)

for i in range (200):
    print(estimateRoot(1, i+1))


#Closure


