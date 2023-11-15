def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = 'O número {} é primo'.format(numero)
    if not resultado:
        mensagem = 'O número {} NÃO é primo'.format(numero)
    return mensagem

numero = 7
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
