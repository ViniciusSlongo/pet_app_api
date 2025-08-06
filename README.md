# Pet Adoption API

Uma API REST para sistema de adoção/divulgação de pets desenvolvida em Python com Flask.

## 🚀 Funcionalidades

- **Cadastro de usuários** com senhas criptografadas (bcrypt)
- **Login seguro** com verificação de hash
- **Criação e consulta de publicações** de animais para adoção
- **Integração com PostgreSQL** usando Peewee ORM
- **Configuração via variáveis de ambiente**

## 🔧 Configuração

### Pré-requisitos

- Python 3.11+
- PostgreSQL
- Docker e Docker Compose (opcional)

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```bash
cp .env.example .env
```

Configure as seguintes variáveis:

```env
# Database Configuration
DB_NAME=pet_adoption_db
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui

# Application Configuration
SECRET_KEY=sua_chave_secreta_aqui
FLASK_ENV=production

# Server Configuration
PORT=5002
HOST=0.0.0.0
```

## 🐳 Instalação com Docker

1. Clone o repositório
2. Configure o arquivo `.env`
3. Execute com Docker Compose:

```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8081`

## 🔨 Instalação Manual

1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o arquivo `.env`
4. Execute a aplicação:

```bash
python -m src.app
```

## 📡 Endpoints da API

### Autenticação

- **POST** `/api/cadastro` - Cadastrar novo usuário
- **POST** `/api/login` - Fazer login

### Publicações

- **GET** `/api/publicacoes` - Listar todas as publicações
- **GET** `/api/publicacoes/<usuario_id>` - Listar publicações de um usuário
- **POST** `/api/publicacao` - Criar nova publicação

### Health Check

- **GET** `/` - Verificar se a API está funcionando

## 🔐 Segurança

- **Senhas criptografadas**: Todas as senhas são hasheadas com bcrypt
- **Configurações seguras**: Credenciais via variáveis de ambiente
- **Validação de entrada**: Verificação básica de dados de entrada

## ⚠️ Migração de Senhas

**IMPORTANTE**: Se você já possui dados no banco com senhas em texto plano, será necessário:

1. Resetar todas as senhas existentes, OU
2. Implementar um script de migração para hashear as senhas existentes

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
src/
├── app.py          # Aplicação Flask principal
├── models.py       # Modelos de dados (Peewee ORM)
├── repository.py   # Camada de acesso a dados
├── services.py     # Lógica de negócio
└── constants.py    # Configurações e constantes
```

### Melhorias Implementadas

✅ **Hash seguro de senhas** com bcrypt  
✅ **Configuração via variáveis de ambiente**  
✅ **Atualização para Python 3.11**  
✅ **Docker Compose moderno** (versão 3.8)  
✅ **Correção de bugs** (payload duplicado)

## 📝 Licença

Este projeto está sob a licença MIT.