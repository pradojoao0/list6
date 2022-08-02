vet = [int(i) for i in input().split(" ") if i]


par = 0

if(len(vet) % 2 == 0):
    media = (len(vet) // 2) - 1
    par = 1
else:
    media =  (len(vet) // 2)



infinite = 0
c = 0
while(infinite == 0):
    if (c != media):
        if (vet[c] > vet[len(vet) - (c + 1)]):
            aux = vet[c]
            vet[c] = vet[len(vet) - (c + 1)]
            vet[len(vet) - (c + 1)] = aux
            c += 1
        else:
            c+= 1

    elif (c == media and par == 1):
        if (vet[c] > vet[c + 1]):
            aux = vet[c]
            vet[c] = vet[c + 1]
            vet[c + 1] = aux
            break

    elif (c == media and par != 1):
        break


print(*vet)
