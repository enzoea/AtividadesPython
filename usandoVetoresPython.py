# Inserção de valores comum
nota1 = 10
nota2 = 2
nota3 = 6
nota4 = 8

# Declaração de um vetor inserindo valores manualmente
vet = [10,2,6,8]

# Mostrando o vetor posição por posição
print(vet[0])
print(vet[1])
print(vet[2])
print(vet[3])

# Mostrando o vetor com estrutura de repetição
x=0
while x<=3:
    print(vet[x])
    x+=1

# Inserindo um vetor em branco
vet2 = []

# Inserindo valores com método de inserção
vet2.append(10)
vet2.append(11)
vet2.append(12)

# Inserindo valores no vetor aatravés de um input
numero1 = int(input('digite o valor do numero 1'))
vet2.append(numero1)
numero1 = int(input('digite o valor do numero 1'))
vet2.append(numero1)
numero1 = int(input('digite o valor do numero 1'))
vet2.append(numero1)
numero1 = int(input('digite o valor do numero 1'))
vet2.append(numero1)
numero1 = int(input('digite o valor do numero 1'))
vet2.append(numero1)

# Recebendo valores com estrutura de repetição
x = 0
while x<5:
    numero1 = int(input('digite o valor do numero 1'))
    vet2.append(numero1)
    x+=1

# utilizando repetição for
for i in range (0,4):
    vet2.append(int(input('digite o valor do numero 1')))