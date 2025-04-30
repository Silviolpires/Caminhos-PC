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
- **Novo**: Cadastro e gerenciamento de trilhas com associação a guias (pessoas físicas)

### Estrutura do Sistema
- Sistema de formulários para cadastro com validações
- Modelo de dados com relações apropriadas
- Interface de usuário responsiva usando Bootstrap
- **Novo**: Relacionamento ManyToMany entre Trilhas e Pessoas Físicas (guias)

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
  - Relacionamento com trilhas como guia

- **PessoaJuridica**
  - Informações do responsável
  - Informações do empreendimento

- **Novo: Trilha**
  - Nome, descrição, distância, duração e nível de dificuldade
  - Relacionamento ManyToMany com PessoaFisica (guias)
  - Controle de data de criação e atualização

## Módulos do Sistema

### Home e Cadastros
Gerencia o cadastro e manutenção de pessoas físicas e jurídicas.

### Fórum
Permite interação entre os usuários do sistema.

### Trilhas
**Novo módulo** que permite:
- Cadastro completo de trilhas com informações detalhadas
- Associação de múltiplos guias (pessoas físicas) a cada trilha
- Interface amigável para gerenciar guias por trilha
- Listagem e visualização detalhada de trilhas
- Operações completas de CRUD (Criar, Ler, Atualizar, Deletar)

## Guia de Instalação e Execução

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação
1. Clone o repositório
git clone [URL-DO-REPOSITÓRIO]
cd APP-CPC

2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Execute as migrações
python manage.py makemigrations
python manage.py migrate

5. Inicie o servidor de desenvolvimento
python manage.py runserver

6. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## Melhorias Futuras
- Implementação completa do sistema de autenticação do Django
- Desenvolvimento de uma área de usuário após o login
- Implementação de recursos para gerenciar eventos
- Melhorias na interface do usuário e experiência de uso
- Expansão do módulo de trilhas com recursos como mapas e avaliações

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
[Especificar a licença do projeto]