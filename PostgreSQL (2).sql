CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    data_cadastro DATE
);

INSERT INTO clientes (nome, data_cadastro) VALUES
('João', '2024-07-14'),
('Maria', '2024-07-14'),
('Pedro', '2024-07-13');

SELECT COUNT(*) AS total_clientes
FROM clientes
WHERE data_cadastro = '2024-07-14';
