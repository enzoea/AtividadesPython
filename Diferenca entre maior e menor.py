# Desenvolva um programa que calcule e exiba a diferença 
# entre o maior e o menor elemento de uma lista 
# denominada VALORES. Os valores da lista devem ser lidos.

quantidadeDeValores = int(input("Digite a quantidade de valores na lista: "))
a = []
b = []
c = []

# Lê os valores da lista
print("Digitando a primeira lista")
for i in range(quantidadeDeValores):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    a.append(valor)

print("Digitando a segunda lista")
for i in range(quantidadeDeValores):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    b.append(valor)

# Armazenando os valores da lista A na lista C2
c = a
a = b
b = c 

print("Lista a: ",a)
print("Lista b: ",b)
