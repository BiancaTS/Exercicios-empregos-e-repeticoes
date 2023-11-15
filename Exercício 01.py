def ehPar(n):
    r = (n%2==0)
    return r
def soma_par(list):
    soma=0
    for num in list:
        if(ehPar(num)):
            soma=soma+num
    return soma
lista = [10,2,5,7,6,3]
soma=soma_par(lista)
print('O somatório dos elementos pares da lista é:{}'.format(soma))