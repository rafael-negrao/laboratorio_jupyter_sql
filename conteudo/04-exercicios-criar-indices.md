# Exercício 2: Criação de Índices

## Abrindo conexão com o banco de dados
```python
%load_ext sql
%sql postgresql://user_app:user_app@db_lab_postgres:5432/db_lab_postgres
```

## Adicionar um índice ao campo email da tabela cliente
```sql
CREATE INDEX idx_email ON cliente(email);
```
## Adicionar um índice ao campo nome da tabela produto
```sql
CREATE INDEX idx_nome_produto ON produto(nome);
```

## Navegação
- [Anterior](03-exercicios-criar-tabela.md)
- [Próximo](05-exercicios-alterando-tabelas.md)
