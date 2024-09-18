CREATE DATABASE IF NOT EXISTS farmacia;
USE farmacia;


CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único para cada usuário
    nome VARCHAR(255) NOT NULL,        -- Nome do usuário
    cpf CHAR(11) NOT NULL UNIQUE,      -- CPF do usuário (11 caracteres, sem formatação)
    data_nascimento DATE NOT NULL,      -- Data de nascimento do usuário
    senha VARCHAR(255) NOT NULL        -- Senha do usuário
);

-- Adiciona um índice único no CPF para garantir que não haja duplicados
CREATE UNIQUE INDEX idx_cpf ON usuario(cpf);
