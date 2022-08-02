import numpy as np

def menorElemento(vetA, x, y, z):
    if(vetA[x] <= vetA[y] and vetA[x] <= vetA[z]):
        return vetA[x]
    elif(vetA[y] <= vetA[x] and vetA[y] <= vetA[z]):
        return vetA[y]
    elif(vetA[z] <= vetA[y] and vetA[z] <= vetA[x]):
        return vetA[z]


vetA = [int(i) for i in input().split(' ') if i]
vetB = np.zeros(21, dtype ="int")


for p in range(0, len(vetA)):
    if(p == 0):
        vetB[p] = menorElemento(vetA, 20, 0, 1)
    elif(p == 20):
        vetB[p] = menorElemento(vetA, 19, 20, 0)
    elif(1 <= p and p < 20):
        vetB[p] = menorElemento(vetA, p-1, p, p+1)


print(*vetB)



