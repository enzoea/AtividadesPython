n = int(input("Quantos números reais você deseja armazenar na lista? "))
numeros = []

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

menor_numero = numeros[0]
indice_menor = 0

for i in range(1, len(numeros)):
    if numeros[i] < menor_numero:
        menor_numero = numeros[i]
        indice_menor = i

print(f"O menor número na lista é {menor_numero} e está na posição (índice) {indice_menor}.")