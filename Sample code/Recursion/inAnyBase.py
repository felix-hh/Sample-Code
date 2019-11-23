
n= 31
base = 3

def inAnyBase(n, base):
    if n <base:
        return str(n%base)
    else:
        return (inAnyBase(n//base, base)+str(n%base))

print(inAnyBase(n,base))
