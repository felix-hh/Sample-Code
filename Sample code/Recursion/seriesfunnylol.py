#n+(n-2)+(n-4)... (until n-x =< 0)

def series(n):
    if n-2<=0:
        return n
    else:
        return n + series(n-2)

print(series(6))
