import locale
locale.setlocale(locale.LC_ALL, '')  # Windows (pode funcionar dependendo da região)



from colorama import init, Fore, Style

init(autoreset=True)

nome_valido = False
salario_valido = False
bonus_valido = False

# Validação do nome
while not nome_valido:
    try:
        nome_usuario = input(Fore.CYAN + "Digite seu nome: ")

        if len(nome_usuario.strip()) == 0:
            raise ValueError(Fore.YELLOW + "⚠️ O campo 'nome' não pode ficar vazio!") 
        elif nome_usuario.isdigit():
            raise ValueError(Fore.RED + "❌ O nome não deve conter números.")
        else:
            print(Fore.GREEN + f"✅ Nome válido: {nome_usuario}")
            nome_valido = True
    except ValueError as e:
        print(e)

# Validação do salário
while not salario_valido:
    try:
        salario_usuario = float(input(Fore.CYAN + "Digite seu salário: "))
        if salario_usuario < 1500:
            print(Fore.YELLOW + "⚠️ Erro: o salário deve ser igual ou maior que R$1.500,00!")
        else:
            print(Fore.GREEN + f"✅ Salário registrado: R${salario_usuario:.2f}")
            salario_valido = True
    except ValueError:
        print(Fore.RED + "❌ Erro: você deve inserir apenas números!")

# Validação do bônus
while not bonus_valido:
    try:
        bonus_usuario = float(input(Fore.CYAN + "Digite o seu bônus: "))
        if bonus_usuario < 300:
            print(Fore.YELLOW + "⚠️ Erro: o valor do bônus deve ser igual ou maior que R$300,00")
        else:
            valor_bonus = 1000 + (salario_usuario * (bonus_usuario / 100))
            print(Fore.GREEN + f"✅ O usuário {nome_usuario} possui o bônus de R${valor_bonus:.2f}.")
            bonus_valido = True
    except ValueError:
        print(Fore.RED + "❌ Erro: você deve inserir apenas números!")

# Resultado final
salario_formatado = locale.currency(salario_usuario, grouping=True)
bonus_formatado = locale.currency(valor_bonus, grouping=True)

print(Style.BRIGHT + Fore.CYAN + f"\n🎉 {nome_usuario}, seu salário é {salario_formatado} e seu bônus final é {bonus_formatado}.")
