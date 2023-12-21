def mostrarMenu():
    print('Digite 1 para somar')
    print('Digite 2 para subtrair')
    print('Digite 3 para dividir')
    print('Digite 4 para multiplicar')
    print('Digite outro numero para sair')

def soma(n1,n2):
    resultado = n1+n2
    return resultado

def subtrair(n1,n2):
    resultado = n1-n2
    return resultado

def dividir(n1,n2):
    resultado = n1/n2
    return resultado

def multiplicar(n1,n2):
    resultado = n1*n2
    return resultado

def validar(n1,n2,operacao):
    if operacao == 1:
        resultado = soma(n1,n2)
    elif operacao == 2:
        resultado = subtrair(n1,n2)
    elif operacao == 3:
        resultado = dividir(n1,n2)
    elif operacao == 4:
        resultado = multiplicar(n1,n2)
    else:
        print('Operação inválida!')
        aux = False
    if aux == True:
        print('Resultado', resultado)

aux = True
while aux == True:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o primeiro numero: '))
    mostrarMenu()
    operacao = int(input('Digite a operação: '))
    validar(n1,n2,operacao)