CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(150),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clientes (nome, email, status)
VALUES 
('Cliente Teste 1', 'cliente1@email.com', 'ativo'),
('Cliente Teste 2', 'cliente2@email.com', 'ativo');