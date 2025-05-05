# APP-CPC

## Descrição
O APP-CPC é uma aplicação Django desenvolvida para gerenciamento de cadastros de pessoas físicas e jurídicas, com suporte a trilhas, fóruns e uma área de usuário logado personalizada.

## Funcionalidades

### Implementadas
- Cadastro completo de Pessoa Física (dados pessoais, contato e segurança)
- Cadastro completo de Pessoa Jurídica (dados do responsável e do empreendimento)
- Cadastro detalhado de endereço
- Listagem de parceiros com filtros de busca
- Sistema de autenticação com sessão personalizada
- Criptografia de senhas usando as funções de hash do Django
- Cadastro e gerenciamento de trilhas com associação a guias (pessoas físicas)
- **Novo**: Área de usuário logado com dashboard personalizado
- **Novo**: Diferenciação de conteúdo para usuários logados e não logados
- **Novo**: Sistema de permissões baseado no tipo de usuário (física/jurídica)
- **Novo**: Controle de acesso administrativo para trilhas (superusers e staff)

### Estrutura do Sistema
- Sistema de formulários para cadastro com validações
- Modelo de dados com relações apropriadas
- Interface de usuário responsiva usando Bootstrap
- Relacionamento ManyToMany entre Trilhas e Pessoas Físicas (guias)
- **Novo**: Sistema de sessão personalizado para autenticação
- **Novo**: Arquitetura de dashboard com visualizações específicas por tipo de usuário
- **Novo**: Decoradores para verificação de permissões administrativas

## Tecnologias Utilizadas
- Django 4.x
- Python 3.x
- Bootstrap 5
- SQLite (banco de dados)
- JavaScript (interações no dashboard)

## Segurança
O sistema implementa:
- Criptografia de senhas usando as funções nativas do Django
- **Novo**: Sistema de sessão para manter dados do usuário logado
- **Novo**: Proteção de rotas com verificação de autenticação
- **Novo**: Controle de acesso baseado no tipo de usuário
- **Novo**: Permissões administrativas baseadas em superusers e staff do Django

## Modelos de Dados
- **Pessoa** (Modelo abstrato)
  - Informações básicas compartilhadas entre pessoas físicas e jurídicas

- **PessoaFisica**
  - Informações completas para cadastro de pessoas físicas
  - Relacionamento com trilhas como guia

- **PessoaJuridica**
  - Informações do responsável
  - Informações do empreendimento

- **Trilha**
  - Nome, descrição, distância, duração e nível de dificuldade
  - Relacionamento ManyToMany com PessoaFisica (guias)
  - Controle de data de criação e atualização

## Módulos do Sistema

### Home e Cadastros
Gerencia o cadastro e manutenção de pessoas físicas e jurídicas.
- **Novo**: Visualização diferenciada para usuários logados e não logados

### Fórum
Permite interação entre os usuários do sistema.
- Visualização de fóruns para todos os usuários
- **Novo**: Criação, edição e exclusão de fóruns apenas para usuários logados

### Trilhas
Módulo que permite:
- Visualização de trilhas para todos os usuários
- **Atualizado**: Cadastro e edição de trilhas apenas para superusers e staff
- **Novo**: Inscrição em trilhas para pessoas físicas logadas
- **Novo**: Associação de múltiplos guias a trilhas

### Dashboard (Novo)
Área exclusiva para usuários logados com:
- Dashboard personalizado baseado no tipo de usuário
- Sistema de breadcrumbs para navegação
- Menu lateral adaptativo
- Para Pessoas Físicas:
  - Visualização e gerenciamento do perfil
  - Gerenciamento de trilhas associadas
- Para Pessoas Jurídicas:
  - Visualização e gerenciamento do perfil
  - Gerenciamento de informações do empreendimento
  - Visualização de estatísticas

## Arquitetura da Área de Usuário Logado

### Sistema de Autenticação
- Armazenamento de informações de usuário na sessão Django
- Decorador personalizado para proteção de rotas
- Funcionalidade de logout com limpeza de sessão

### Estrutura de Templates
- Template base global (home_view/base.html)
- Template intermediário do dashboard (dashboard/dashboard.html)
- Templates específicos para cada funcionalidade do dashboard

### Sistema de Navegação
- Menu principal adaptativo (diferente para usuários logados e não logados)
- Menu lateral no dashboard com opções específicas por tipo de usuário
- Sistema de breadcrumbs para facilitar a navegação

## Problemas Conhecidos e Limitações
- Referências a URLs entre aplicativos devem incluir o namespace apropriado (ex: `forum_view:forum`)
- É necessário criar e configurar corretamente o novo aplicativo `dashboard` no settings.py
- O sistema de autenticação atual é baseado em sessão e não utiliza o sistema nativo do Django
- Os botões "Inscrever-se" nas trilhas ainda não estão funcionais
- A criação e edição de posts no fórum não está implementada para usuários logados

## Guia de Instalação e Execução

### Pré-requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação
1. Clone o repositório
git checkout -b feature/user-area
git clone [URL-DO-REPOSITÓRIO]
cd APP-CPC

2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Crie o aplicativo dashboard
python manage.py startapp dashboard

5. Adicione o aplicativo dashboard ao INSTALLED_APPS no arquivo settings.py
```python
INSTALLED_APPS = [
    # ... apps existentes
    'dashboard',
]

Execute as migrações

python manage.py makemigrations
python manage.py migrate

Inicie o servidor de desenvolvimento

python manage.py runserver

Acesse a aplicação em http://localhost:8000

Melhorias Futuras

Migração para o sistema de autenticação nativo do Django
Implementação de funcionalidades avançadas no perfil do usuário
Integração de um sistema de notificações
Implementação de recursos para gerenciar eventos
Melhorias na interface do usuário e experiência de uso
Adição de painéis estatísticos mais avançados para pessoas jurídicas

Próxima Versão (Sugestões)

Implementação da funcionalidade de inscrição em trilhas: Corrigir os botões "Inscrever-se" nas trilhas para permitir que usuários se inscrevam corretamente
Sistema de criação e edição de fóruns para usuários logados: Implementar a funcionalidade para que usuários logados possam criar, editar e excluir posts no fórum
Aprimoramento do sistema de permissões: Expandir o controle de acesso baseado em superusers e staff para outras áreas do sistema além das trilhas
Interface administrativa personalizada: Desenvolver uma interface personalizada para administradores gerenciarem o sistema sem necessidade de acessar o admin do Django

Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
Licença
[Especificar a licença do projeto]

Esta versão atualizada do README inclui as mudanças implementadas no sistema de permissões para trilhas e adiciona nossas discussões sobre as funcionalidades de inscrição em trilhas e gerenciamento de fóruns como sugestões para a próxima versão.