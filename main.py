def tamanho(palavra):
    contador = 0
    for letra in palavra:
        contador += 1
    return contador
print(tamanho("carlos"))

def concatenacao(palavra,palavra1):
    resultado = ""
    for letra in [palavra,palavra1]:
        resultado += letra
    return resultado
print (concatenacao("car", "los"))

def comparacao(palavra,palavra1):
    for letra in palavra:
        for letra1 in palavra1:
            if (letra == letra1):
                return True
            else:
                return False
print (comparacao("Carlos", "Carlos"))

def subPalavra (palavra, indiceI, indiceF):
    sub = ""
    count = 0
    for x,y in enumerate(palavra):
        if (x==(indiceI+count)):
            count += 1 
            sub += y 
            if(x == indiceF):
                break
    return sub
print(subPalavra("carlos", 1, 2))