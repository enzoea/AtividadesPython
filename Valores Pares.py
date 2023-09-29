# Lendo todos os elementos pares de ua lista

quantidadeDeValores = int(input("Digite a quantidade de valores na lista: "))
VALORES = []
VALORESPARES = []
# Lê os valores da lista
for i in range(quantidadeDeValores):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    VALORES.append(valor)

# Verifica se a lista não está vazia
if len(VALORES) == 0:
    print("A lista está vazia. Não é possível calcular a diferença.")
else:
    for i in range(quantidadeDeValores):
        if VALORES[i] %2 == 0:
            VALORESPARES.append(VALORES[i])

print(VALORESPARES)