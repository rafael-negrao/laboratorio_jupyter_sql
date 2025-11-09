# Exercício 4: Criação de views

## Abrindo conexão com o banco de dados
```python
%load_ext sql
%sql postgresql://user_app:user_app@db_lab_postgres:5432/db_lab_postgres
```

## Criar a View detalhe_pedido_cliente
```sql
DROP VIEW IF EXISTS v_detalhe_pedido_cliente;
CREATE VIEW v_detalhe_pedido_cliente AS
SELECT
    c.id AS cliente_id,
    c.nome AS cliente_nome,
    c.email AS cliente_email,
    prd.id AS produto_id,
    prd.nome AS produto_nome,
    prd.preco AS produto_preco,
    p.id AS pedido_id,
    p.data_pedido AS data_pedido,
    ic.quantidade AS quantidade,
    ic.preco_unitario AS preco_unitario,
    (ic.quantidade * ic.preco_unitario) AS total_item
FROM
    pedido p
        INNER JOIN cliente c ON p.cliente_id = c.id
        INNER JOIN item_pedido ic ON p.id = ic.pedido_id
        INNER JOIN produto prd ON ic.produto_id = prd.id;
```

## Navegação
- [Anterior](05-exercicios-alterando-tabelas.md)
- [Próximo](07-select-tipos-de-joins.md)
