-- 1. Cria o banco de dados
CREATE DATABASE americanas_projeto;

-- 2. Seleciona o banco de dados
USE americanas_projeto;

-- 3. Cria a tabela de usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);
