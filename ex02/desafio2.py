#REFATORAMENTO

CONSTANTE_BONUS = 1000

nome_usuario = input("Digite seu nome:" )

# Adicionanda duas funções que verificam se o campo esta vazio ou se o nome foi digitado errado

if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("O campo 'nome' não pode ficar vazio! ") 
    exit()   
###########################################################    

try:
    salario_usuario = float(input("Digite seu salário: "))
    if salario_usuario < 1500:
        print("Erro: o salário deve ser igual ou maior que R$1.500,00!")
        exit()
    else:
        print(f"Seu salario é R$:{salario_usuario}.")
except ValueError:
    print("Erro: você deve inserir apenas números!")
    exit()


#####################################################

try:

    bonus_usuario = float(input("Digite o seu bônus: "))

    valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

    if bonus_usuario < 300:
        print("Erro: o valor do bônus deve ser igual ou maior que R$300,00")
    else:    
        print(f"O usuário {nome_usuario} possui o bônus de {valor_bonus}.")
    
except ValueError:
  print("Erro: você deve inserir apenas números!")
exit()