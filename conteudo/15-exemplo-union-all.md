# Exemplo do uso de UNION ALL

## Contexto de Negócio
Uma empresa deseja analisar o impacto de promoções e feriados específicos nas vendas para planejar melhor as campanhas futuras e ajustar a gestão de estoque. Os períodos de interesse incluem a Black Friday e o Ano Novo, ambos de alta atividade comercial.

## Abrindo conexão com o banco de dados
```python
%load_ext sql
%sql postgresql://user_app:user_app@db_lab_postgres:5432/db_lab_postgres
```

## Cenários e SQL Queries

### Cenário 1: pedidos Durante a Black Friday
**Objetivo:** Determinar o volume de pedidos durante a Black Friday para avaliar a eficácia de estratégias de desconto e promoção.

```sql
SELECT pedido.id AS pedidoID, pedido.data_pedido AS Datapedido, cliente.nome AS clienteNome
FROM pedido
JOIN cliente ON pedido.cliente_id = cliente.id
WHERE pedido.data_pedido BETWEEN '2022-11-24' AND '2022-11-25';
```

### Cenário 2: pedidos Durante o Ano Novo
**Objetivo:** Analisar os pedidos feitos durante o Ano Novo para entender a demanda de produtos e a eficiência das promoções de fim de ano.

```sql
SELECT pedido.id AS pedidoID, pedido.data_pedido AS Datapedido, cliente.nome AS clienteNome
FROM pedido
JOIN cliente ON pedido.cliente_id = cliente.id
WHERE pedido.data_pedido BETWEEN '2022-12-26' AND '2023-01-01';
```

### Combinação dos Cenários com UNION ALL
**Objetivo:** Produzir um relatório detalhado que mostra a atividade total de pedidos para ambos os eventos sem eliminar duplicatas, permitindo uma análise detalhada da atividade em cada evento.

```sql
-- pedidos durante a Black Friday
SELECT 'Black Friday' AS Evento, pedido.id AS pedidoID, pedido.data_pedido AS Datapedido, cliente.nome AS clienteNome
FROM pedido
JOIN cliente ON pedido.cliente_id = cliente.id
WHERE pedido.data_pedido BETWEEN '2022-11-24' AND '2022-11-25'
UNION ALL
-- pedidos durante o Ano Novo
SELECT 'Ano Novo' AS Evento, pedido.id AS pedidoID, pedido.data_pedido AS Datapedido, cliente.nome AS clienteNome
FROM pedido
JOIN cliente ON pedido.cliente_id = cliente.id
WHERE pedido.data_pedido BETWEEN '2022-12-26' AND '2023-01-01';
```

Este relatório combinado proporciona uma visão completa do impacto de cada evento nas vendas, crucial para planejamento estratégico, marketing e operações.



## Navegação
- [Anterior](14-exemplo-union.md)
- [Próximo](16-fase2-o-escopo-aumentou.md)
