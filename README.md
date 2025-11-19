# Laboratório Jupyter SQL

## 📚 Sobre o Projeto

Este projeto tem fim **educacional** e o objetivo é **ensinar SQL** de forma prática e interativa, utilizando Jupyter Notebook para executar consultas SQL diretamente no navegador.

## 🎯 Objetivos

- Aprender comandos SQL básicos e avançados
- Praticar queries em ambiente isolado e seguro
- Experimentar com bancos de dados MySQL e PostgreSQL
- Visualizar resultados de queries de forma interativa

## 🛠️ Tecnologias Utilizadas

- **Docker & Docker Compose** - Containerização dos serviços
- **Jupyter Notebook** - Interface interativa para execução de código
- **MySQL 8.0.31** - Banco de dados relacional
- **PostgreSQL 15** - Banco de dados relacional
- **JupySQL** - Extensão para executar SQL no Jupyter
- **Python** - SQLAlchemy, PyMySQL, psycopg2

## 🚀 Como Executar

### Pré-requisitos

- Docker
- Docker Compose

### Passo a passo iniciar o ambiente

1. **Clone o repositório**

```bash
git clone git@github.com:rafael-negrao/laboratorio_jupyter_sql.git
cd laboratorio_jupyter_sql
```

2. **Inicie os containers**

Iniciar os containers compilando a imagem do Jupyter Notebook

```bash
docker compose up -d --build
```

Iniciar os containers após a compilação da imagem do Jupyter Notebook

```bash
docker compose up -d
```

3. **Acesse o Jupyter Notebook**

Abra seu navegador e acesse: `http://localhost:8888`

4. **Conecte-se ao banco de dados**

4.1. Carregar o módulo `sql`

```jupyter
%load_ext sql
```

4.2. Conectar ao banco de dados PostgreSQL

```jupyter
%sql postgresql://admin:admin@postgres-sql-aula:5432/curso_sql
```

4.3. Fechar a conexãom com o banco de dados PostgreSQL

```jupyter
%sql --close postgresql://admin:***@postgres-sql-aula:5432/curso_sql
```


## 📂 Estrutura do Projeto

```
laboratorio_jupyter_sql/
├── docker-compose.yaml     # Configuração dos containers
├── jupyter/Dockerfile      # Dockerfile para criar imagem do Jupyter
├── notebooks/              # Notebooks Jupyter
└── README.md               # Este arquivo
```


## 🔧 Configuração

### Credenciais do Banco de Dados

**PostgreSQL:**
- Host: `postgres-sql-aula`
- Porta: `5432`
- Database: `curso_sql`
- Usuário: `admin`
- Senha: `admin`

## 🛑 Parar o Projeto

```shell script
docker compose down
```

Para remover também os volumes (dados):
```shell script
docker compose down -v
```

## 🤝 Contribuindo

Este é um projeto educacional. Sinta-se à vontade para:

- Adicionar novos exemplos
- Melhorar a documentação
- Reportar problemas
- Sugerir melhorias

## 📄 Licença

Este projeto é de uso educacional livre.

## ✨ Autor

Projeto criado para fins educacionais de ensino de SQL.

