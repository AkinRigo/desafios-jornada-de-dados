# integre na solução anterior um fluxo de while
# que repita o fluxo até que o usuário insira as informações corretas


CONSTANTE_BONUS = 1000

# Adicionanda duas funções que verificam se o campo esta vazio ou se o nome foi digitado errado

nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome_usuario = input("Digite seu nome:" )

        #verifica se o nome esta vazio
        if len(nome_usuario) == 0:
            raise ValueError ("O campo 'nome' não pode ficar vazio! ") 
        # verifica se há números no nome
        elif nome_usuario.isdigit():
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome_usuario)
            nome_valido = True
    except ValueError as e:
        print(e)

###########################################################  
#  


while salario_valido is not True:
    try:
        salario_usuario = float(input("Digite seu salário: "))
        if salario_usuario < 1500:
            print("Erro: o salário deve ser igual ou maior que R$1.500,00!")
            salario_valido = True
    except ValueError:
        print("Erro: você deve inserir apenas números!")


#####################################################


while bonus_valido is not True:

    try:

        bonus_usuario = float(input("Digite o seu bônus: "))

        valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

        if bonus_usuario < 300:
            print("Erro: o valor do bônus deve ser igual ou maior que R$300,00")
        else:    
            print(f"O usuário {nome_usuario} possui o bônus de {valor_bonus}.")
        
    except ValueError:
        print("Erro: você deve inserir apenas números!")