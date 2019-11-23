lista = [1, 2, [3,4], [5,6]]

def recursiveSum(lista2):
    if len (lista2) ==1:
        return lista2[0]
    else:
        return (recursiveSum(lista2[1:])+lista2[0])

def recursiveListSum(lista):
    if type(lista[0])== int:
        result = lista[0]
    else:
        result = recursiveSum(lista[0])
    if len(lista)==1:
        return result
        
    else:
        return (result+recursiveListSum(lista[1:]))


print (recursiveListSum(lista))

