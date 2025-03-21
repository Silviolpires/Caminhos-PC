# APP-CPC

## Descrição
O APP-CPC é uma aplicação Django desenvolvida para gerenciamento de cadastros de pessoas físicas e jurídicas, com suporte a trilhas e eventos.

## Funcionalidades

### Implementadas
- Cadastro completo de Pessoa Física (dados pessoais, contato e segurança)
- Cadastro completo de Pessoa Jurídica (dados do responsável e do empreendimento)
- Cadastro detalhado de endereço
- Listagem de parceiros com filtros de busca
- Sistema básico de login
- Criptografia de senhas usando as funções de hash do Django

### Estrutura do Sistema
- Sistema de formulários para cadastro com validações
- Modelo de dados com relações apropriadas
- Interface de usuário responsiva usando Bootstrap

## Tecnologias Utilizadas
- Django 4.x
- Python 3.x
- Bootstrap 5
- SQLite (banco de dados)

## Segurança
O sistema implementa criptografia de senhas usando as funções nativas do Django:
- `make_password()`: Utilizada para criptografar senhas no momento do cadastro
- `check_password()`: Utilizada para verificar senhas no momento do login

Estas funções proporcionam um nível adequado de segurança, aplicando algoritmos de hash com salt para proteção das senhas dos usuários.

## Modelos de Dados
- **Pessoa** (Modelo abstrato)
  - Informações básicas compartilhadas entre pessoas físicas e jurídicas

- **PessoaFisica**
  - Informações completas para cadastro de pessoas físicas

- **PessoaJuridica**
  - Informações do responsável
  - Informações do empreendimento

## Guia de Instalação e Execução

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação
1. Clone o repositório
   ```
   git clone [URL-DO-REPOSITÓRIO]
   cd APP-CPC
   ```

2. Crie e ative um ambiente virtual
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento
   ```
   python manage.py runserver
   ```

6. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## Melhorias Futuras
- Implementação completa do sistema de autenticação do Django
- Desenvolvimento de uma área de usuário após o login
- Implementação de recursos para gerenciar trilhas e eventos
- Melhorias na interface do usuário e experiência de uso

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
[Especificar a licença do projeto]