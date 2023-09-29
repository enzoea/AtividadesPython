
mensagem = input("Digite a mensagem que deseja criptografar: ")
chave = int(input("Digite a chave de criptografia (um número inteiro): "))

mensagem_criptografada = ""

for aux in mensagem:
    if aux.isalpha():
        maiuscula = aux.isupper()
        aux = aux.lower()
        codigo = ord(aux) - ord('a')
        codigo = (codigo + chave) % 26
        aux = chr(codigo + ord('a'))
        if maiuscula:
            aux = aux.upper()
    mensagem_criptografada += aux

print("Mensagem criptografada: " + mensagem_criptografada)