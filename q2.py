vetA = [float(i) for i in input().split(' ') if i]


def mediaAritmetica(vet):
    soma = 0
    media = 0
    for itt in range(0, len(vet)):
        soma += vet[itt]
    media = soma/len(vet)
    return media

media = mediaAritmetica(vetA)

def somaCalculada(vet):
    soma = 0
    for itt in range(0, len(vet)):

        soma += 2*((4*vet[itt] - 3*media)**2)*2*vet[itt]

    return soma

contaFinal = (2/(3*(23*23))*somaCalculada(vetA))**0.5

print("{:.2f}".format(contaFinal))
