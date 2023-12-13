linhas = int(input('Digite o valor das linhas '))
colunas = int(input('Digite o valor das linhas '))

matriz = []

x=0
while x < linhas:
    vet = []
    y=0

    while y < colunas:
        vet.append(input('Digite um valor: '))
        y+=1

    mat.append(vet)
    x+=1

x=0
while x < linhas:
    print(mat[x])
    x+=1

print(mat)