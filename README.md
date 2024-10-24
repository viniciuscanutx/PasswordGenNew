
# Password Generator 🔒

Este é um **Gerador de Senhas Seguras** desenvolvido em Python utilizando `Flet` para a interface gráfica. O objetivo é criar senhas seguras para diferentes sites e serviços, além de salvá-las em um banco de dados local para fácil acesso. 🛡️

## 🖥️ Visão Geral

O projeto oferece uma interface simples onde você pode:
- Criar uma conta e ter senhas separadas para cada conta criada.
- Inserir o e-mail, nome de usuario ou site associado ao serviço.
- Definir o tamanho da senha entre 6 e 24 caracteres.

## 🚀 Funcionalidades

- **Geração de senhas seguras**: Senhas contendo letras maiúsculas, minúsculas, números e caracteres especiais.
- **Interface amigável**: Feito com `Flet` para ser simples e fácil de usar.
- **Armazenamento seguro**: As senhas geradas são automaticamente salvas em um banco de dados local.
- **Quantidade personalizável de caracteres**: Escolha o comprimento desejado da sua senha.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flet**: Biblioteca de interface gráfica.
- **Random**: Módulo da biblioteca padrão para geração de senhas aleatórias.

## 📦 Instalação

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/password-generator.git
   ```

2. Navegue até o diretório do projeto:

    ```bash
    cd password-generator
    ```

3. Execute o gerador de senhas: 

    ```bash
    python app.py
    ```

## 📝 Como Usar

1. E-mail/Senha: Insira um usuario ou email e senha e crie sua conta.

2. Clique em gerenciar senhas e escolha uma quantidade de caracteres e digite para onde irá essa senha.

3. Clique no botão Gerar Senha para gerar uma senha segura.

4. A senha gerada será exibida na tela e salva no banco.

## 🎨 Customização

O tema utilizado para a interface é padrão. Caso ele não esteja disponível, o aplicativo usará o tema padrão do Flet.

## ✨ Melhorias Futuras

- Adicionar suporte para criptografia das senhas salvas.

- Banco de dados online para melhor suporte a usuários.

- Busca de senhas.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📜 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.