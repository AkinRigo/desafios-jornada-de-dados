texto = input("Digite uma palavra:")

def letras(str):
    dicionario = {}

    for letra in str:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1  
        
    return dicionario


resultado = letras(texto)
print(resultado)
