minhaLista = []
soma = 0
quantidadeDeValores = int(input("Digite a quantidade de valores na lista: "))

print("Digitando a primeira lista")
for i in range(quantidadeDeValores):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    minhaLista.append(valor)

for i in range(0, len(minhaLista), 2):
    soma += minhaLista[i]

resultado = soma
print("A soma dos elementos de índice par é:", resultado)
