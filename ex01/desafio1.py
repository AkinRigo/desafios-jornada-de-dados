CONSTANTE_BONUS = 1000

nome_usuario = input("Digite seu nome:" )

salario_usuario = float(input("Digite seu salário: "))

bonus_usuario = float(input("Digite o seu bônus: "))

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O usuário {nome_usuario} possui o bônus de {valor_bonus}.")