CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    idade INT
);

INSERT INTO usuarios (nome, email, idade) VALUES
('João Silva', 'joao@email.com', 30),
('Maria Santos', 'maria@email.com', 25),
('Pedro Oliveira', 'pedro@email.com', 35);
