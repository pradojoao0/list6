vetX = [int(i) for i in input().split(" ") if i]
vetY = [6,5,9,2,6,1,6,7,1,2,3,6,8,9,9,6,1,3]



perm = 0


for i in range(1, len(vetX)):
    if((vetX[0] == vetY[18 - i]) and (vetX[i] == vetY[0])):
        perm = 1
        break
    else:
        i += 1


if(perm == 1):
    print(f"i = {i}")
else:
    print("i = 18")
