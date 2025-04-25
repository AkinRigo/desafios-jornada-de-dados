# 📚 Sistema de Escolha de Livros

Este projeto é um programa em Python que simula o processo de **login** e **seleção de livros** de uma biblioteca virtual feito no exercício 8.

---

## 🚀 Como Funciona

1. O usuário insere:
   - Nome de usuário
   - Senha (apenas números permitidos)

2. Após o login:
   - A lista de livros disponíveis é exibida.
   - O usuário escolhe o livro pelo número correspondente.

3. O sistema confirma a escolha e simula o envio do livro por e-mail.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Biblioteca padrão:
  - `getpass` (para ocultar a senha no terminal)

---

## 📋 Requisitos

- Python instalado (versão 3 ou superior).
- Terminal ou prompt de comando para execução.

---

## ▶️ Como Executar

1. Clone este repositório ou baixe o arquivo `ex08.py`.
2. Navegue até a pasta do projeto via terminal:

   ```bash
   cd /caminho/para/o/projeto


✅ Funcionalidades
🔒 Login seguro com senha oculta.

✅ Validação de senha numérica.

📚 Lista de livros exibida com autor e ano.

🎯 Seleção de livros através do terminal com confirmação.

⚠️ Observações

- Durante a digitação da senha, nenhum caractere será exibido (por segurança usando getpass).

- Para facilitar testes durante o desenvolvimento, você pode substituir getpass.getpass() por input().

Exemplo de modificação para testes:

# Original:
senha = getpass.getpass("Digite sua senha:")

# Para testes:
senha = input("Digite sua senha:") 


---

## 🧠 Conceitos de Python Usados

### 1. Entrada de Dados
- `input()` para capturar usuário e escolha do livro.
- `getpass.getpass()` para entrada de senha de forma segura (sem exibir no terminal).

### 2. Funções
- Uso de `def` para criar a função `login()`, separando a lógica de autenticação.

### 3. Estruturas de Dados
- **Listas (`[]`)**: usadas para armazenar a coleção de autores e seus livros.
- **Dicionários (`{}`)**: usados para organizar os dados de autores e livros com pares `chave: valor`.

### 4. Laços de Repetição
- `for`: percorre autores e livros para exibir opções ao usuário.
- `while True`: mantém o programa rodando até o usuário fazer uma escolha válida.

### 5. Condicionais
- `if`, `else`, `if not`: para validar senha, verificar se a escolha está no intervalo válido, etc.

### 6. Tratamento de Erros
- `try-except`: para capturar exceções, como quando o usuário digita algo que não é número.

### 7. Interpolação de Strings
- Uso de **f-strings**: exemplo — `f"{contador}. {livro['titulos']}"`.

### 8. Controle de Fluxo
- `break`: utilizado para sair do laço `while` quando uma entrada válida é recebida.

---

## ✨ Extras Abordados

- Organização de código em blocos lógicos e legíveis.
- Simulação básica de login/autenticação.
- Manipulação de estruturas aninhadas (listas dentro de dicionários e vice-versa).
- Comentários explicativos no código.

---

## 📈 Possíveis Melhorias Futuras

- Implementar persistência de dados com arquivos `.json` ou banco de dados.
- Permitir cadastro de novos usuários.
- Adicionar categorias ou filtros de busca para os livros.
- Melhorar a segurança com autenticação real (ex: `hashlib`, autenticação por token).

---

## 📌 Observações

- A senha só aceita números.
- O programa não salva usuários ou livros escolhidos após ser encerrado.
- Rodar este programa requer um terminal que suporte a função `getpass()`.

---

