#harmonic sum

def harmSeries(n):
    if n ==1:
        return 1
    else:
        return(1/n+harmSeries(n-1))

print(harmSeries(500))
