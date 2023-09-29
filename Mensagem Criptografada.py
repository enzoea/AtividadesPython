
mensagem = input("Digite a mensagem que deseja criptografar: ")
chave = int(input("Digite a chave de criptografia (um número inteiro): "))

mensagem_criptografada = ""

for aux in mensagem:
    # isalpha() serve para identificar um caractere que não é letra dentro de uma string, ou seja, um caractere inválido
    if aux.isalpha():
        # isupper() Para detectar se uma string é toda maiúscula ou toda minúscula, usamos o método isupper() que retorna True se todos caracteres forem maiúsculos, e False se não forem.
        maiuscula = aux.isupper()
        # lower() Converte todos os caracteres da string em minúsculas.
        aux = aux.lower()
        # O caractere é convertido para minúscula, e a posição relativa à letra 'a' (de 0 a 25) é calculada usando
        codigo = ord(aux) - ord('a')
        # aplicando a cifra de cesar
        codigo = (codigo + chave) % 26
        # A posição é convertida de volta para um caractere usando
        aux = chr(codigo + ord('a'))
        if maiuscula:
            aux = aux.upper()
    mensagem_criptografada += aux

print("Mensagem criptografada: " + mensagem_criptografada)
