import getpass

usuario_correto = "akin"
senha_correta = "2304"

def login():
    usuario = input("Usuário:")
    print(usuario)
    senha = getpass.getpass ("Senha:").strip()
    return usuario == usuario_correto and senha == senha_correta

tentativas = 3

while tentativas > 0:
    try:
        if login():
            print("Acesso autorizado!")
            break
        else:
            tentativas -= 1
            print(f"Dados incorretos. Tentativas restantes: {tentativas}")
            



