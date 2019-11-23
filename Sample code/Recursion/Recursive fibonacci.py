


def treeRecursiveFibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return(treeRecursiveFibonacci(n-1)+treeRecursiveFibonacci(n-2))

def recursiveFibonacci(n):
    
    def fibit (a,b,count):
        if count == 0:
            return a
        else:
            c=a+b
            b=a
            a=c
            count-=1
            return(fibit(a,b,count))
        
    return(fibit(0,1,n))

    
bubble=35

for i in range (bubble):
    print (treeRecursiveFibonacci(i))

for i in range (bubble):
    print(recursiveFibonacci(i))
