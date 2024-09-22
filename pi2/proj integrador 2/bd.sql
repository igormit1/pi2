CREATE DATABASE farmacia;
USE farmacia;

CREATE TABLE if not exists Pessoa (
    ID_Pessoa INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CPF VARCHAR(11) NOT NULL UNIQUE,
	Email VARCHAR(30) NOT NULL,
    Endereco VARCHAR(255) NOT NULL,
    Ocupacao VARCHAR(15) NOT NULL,
    Senha CHAR(64) NOT NULL
);

CREATE TABLE if not exists Medicamento (
    ID_Medicamento INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Medicamento VARCHAR(100) NOT NULL,
    nome_generico VARCHAR(100) NULL,
    categoria VARCHAR(100) NULL,
    distribuidor  VARCHAR(100) NULL,
    Data_Validade DATE NOT NULL,
    Preço DECIMAL(10, 2) NOT NULL
);

CREATE TABLE if not exists Entrega (
    ID_Entrega INT AUTO_INCREMENT PRIMARY KEY,
    ID_balconista int,
    ID_cliente int,
    Data_Entrega DATE NOT NULL,
    valor_total DECIMAL(10, 2) NULL,
    FOREIGN KEY (ID_balconista) REFERENCES Pessoa(ID_Pessoa),
	FOREIGN KEY (ID_cliente) REFERENCES Pessoa(ID_Pessoa)
);

create table if not exists entrega_medicamento (
ID_Entrega_ref INT,
FOREIGN KEY (ID_Entrega_ref) REFERENCES Entrega(ID_Entrega),
ID_Medicamento_ref INT,
FOREIGN KEY (ID_medicamento_ref) REFERENCES medicamento(ID_medicamento),
quantidade int not null);
 
select * from pessoa;