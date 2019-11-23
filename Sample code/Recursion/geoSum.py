#geometric sum


def geoSum(n):
    if n < 0:
        return 0
    else:
        return (1/2**n + geoSum(n-1))

print(geoSum(7))
