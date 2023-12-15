mat = []
vetSoma = []
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

x=0
while x<linhas:
    vet = []
    soma=0
    y=0
    while y<colunas:
        valor = int(input('Digite o valor: '))
        vet.append(valor)
        soma+=valor
        y+=1
    mat.append(vet)
    vetSoma.append(soma)
    x+=1

aux = 1- int(input('Digite o numero da linha que deseja fazer a media: '))
media = vetSoma[aux]/colunas

print('Media: ',media)