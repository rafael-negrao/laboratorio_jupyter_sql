# O escopo de negocio foi alterado

As seguintes tabelas foram adicionadas ao modelo de banco de dados para incorporar novas funcionalidades:

## Modelo de entidade de relacionamento - MER
![mer-v.1.1.0.png](imagens%2Fmer-v.1.1.0.png)

## Abrindo conexão com o banco de dados
```python
%load_ext sql
%sql postgresql://user_app:user_app@db_lab_postgres:5432/db_lab_postgres
```

## 1. Tabela Transportadora
Responsável por armazenar informações sobre as transportadoras que entregam os pedidos.

```sql
CREATE TABLE transportadora
(
    id       SERIAL PRIMARY KEY,
    nome     VARCHAR(100) NOT NULL,
    email    VARCHAR(100),
    telefone VARCHAR(15)
);
```

## 2. Tabela FormaPagamento
Armazena os diferentes tipos de formas de pagamento que podem ser usados para liquidar um pedido.

```sql
CREATE TABLE forma_pagamento
(
    id                   SERIAL PRIMARY KEY,
    tipo_forma_pagamento TEXT CHECK (tipo_forma_pagamento IN ('PIX', 'CartaoCredito')) NOT NULL
);
```

## 3. Tabela Entrega
Registra informações sobre as entregas de pedidos, incluindo datas previstas e reais de entrega, associadas aos pedidos e transportadoras.

```sql
CREATE TABLE entrega
(
    id                INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_prevista     DATE,
    data_entrega      DATE,
    pedido_id         INT NOT NULL,
    transportadora_id INT NOT NULL,
    CONSTRAINT fk_entrega_pedido
        FOREIGN KEY (pedido_id) REFERENCES pedido (id),
    CONSTRAINT fk_entrega_transportadora
        FOREIGN KEY (transportadora_id) REFERENCES transportadora (id)
);
```

## 4. Adicionar Forma de Pagamento ao Pedido
Inclui uma referência à forma de pagamento em cada pedido, para melhor rastreamento financeiro.

```sql
ALTER TABLE pedido
    ADD COLUMN forma_pagamento_id INT,
ADD CONSTRAINT fk_pedido_forma_pagamento
    FOREIGN KEY (forma_pagamento_id)
    REFERENCES forma_pagamento(id);
```

Estas alterações permitem um melhor gerenciamento de logística, pagamentos e entrega de pedidos, essenciais para operações de venda e e-commerce.

## Rodar os scripts de carga
```python
%sql --file setup-scripts/06_carga-novas-tabelas.sql
```

```python
%sql --file setup-scripts/09_carga_entregas_sem_python.sql
```


## Navegação
- [Anterior](15-exemplo-union-all.md)
- [Próximo](17-exercicios-sem-gabarito.md)
