
import getpass


#login do usuário
def login():
    usuario = input("Digite seu usuário:")
    print(usuario)
    senha = getpass.getpass ("Digite sua senha:").strip()

    if not senha:
        print("Senha inválida! Não pode ser vazia.")
        return False

    if not senha.isdigit():
        print("Senha inválida! Use somente números.")
        return False
    print(f"Bem-vindo(a/e), {usuario}!\n")
    return True




biblioteca = [  
    
    { "autor":"Machado de Assis","livros": [{"titulos": "Dom Casmurro", "ano": 1899},
                                            {"titulos": "Memórias Póstumas de Brás Cubas", "ano": 1881}, 
                                            {"titulos":"Quincas Borba", "ano": 1891}]},


    {"autor":"Graciliano Ramos", "livros": [{"titulos":"Vidas Secas", "ano": 1938},
                                            {"titulos":"S. Bernardo", "ano": 1934},
                                            {"titulos":"A Grande Sereia", "ano": 1938},]},

    
    {"autor":"Guimarães Rosa", "livros": [{"titulos":"Grande Sertão: Veredas", "ano": 1956},
                                            {"titulos":"Sagarana", "ano": 1946},
                                            {"titulos":"Corpo de Baixo", "ano": 1956},]},



    {"autor":"Euclides da Cunha", "livros": [{"titulos":"Os Sertões","ano": 1902}] },

    {"autor":"Aluísio Azevedo", "livros": [{"titulos":"O Cortiço", "ano": 1890}]},

    {"autor":"José de Alenca", "livros": [{"titulos":"Iracema", "ano": 1865},
                                            {"titulos":"A Moreninha", "ano": 1844},]},

    {"autor":"Jorge Amado", "livros": [{"titulos": "Capitães da Areia", "ano": 1937}] },

    {"autor":"Clarice Lispector", "livros": [{"titulos":"A Hora da Estrela", "ano": 1977},
                                            {"titulos":"Perto do Coração Selvagem", "ano": 1943},]},

    
    {"autor":"Lima Barreto", "livros": [{"titulos":"Triste Fim de Policarpo Quaresma", "ano": 1915}] },


    {"autor":"Manoel de Barros", "livros": [{"titulos":"Livro sobre Nada", "ano": 1996}] },

    ] 

if not login():
    exit()  # Se o login não for válido, o programa para



#Lista de livros disponíveis

todos_os_livros = []
contador = 1

print("Livros disponíveis:\n")
for autor in biblioteca:
    for livro in autor["livros"]:
        print(f"{contador}. {livro['titulos']} ({autor['autor']}), {livro['ano']}")
        todos_os_livros.append(livro['titulos'])
        contador += 1

# Escolhendo o livro

while True:
    try:
        escolha = int(input("Digite o número do livro que deseja:"))
        if 1<= escolha <= len(todos_os_livros):
            livro_escolhido = todos_os_livros[escolha - 1]
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Digite um número válido!")


# Confirmação
print(f"você escolheu '{livro_escolhido}'. Confira seu email para acessar o livro.")