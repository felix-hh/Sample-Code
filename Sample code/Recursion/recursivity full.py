#sum, multiplication and exponentiation as iterative processes of counting

def sum (n, m):
    if n==0 and m == 0:
        return 0
    else:
        if n == 0:
            m-=1
        else:
            n-=1
        return (1+sum(n,m))

def multiply (n, m):
    if m==0:
        return 0
    else:
        return(sum(n,multiply (n, m-1)))

print (multiply (4,88))
