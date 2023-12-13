matriz1 = [
    [1,1],
    [1,1]
]
matriz2 = [
    [1,1],
    [1,1]
]

soma = []

x=0
while x<2:
    y=0
    vet = []
    while y<2:
        vet.append(matriz1[x][y] + matriz2[x][y])
        y+=1
    soma.append(vet)
    x+=1

print(soma)