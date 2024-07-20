/*
Nome: Anderson Marden de Sousa Silva
Dre: 119113730
*/

CREATE DATABASE IF NOT EXISTS locadora_veiculos;
USE locadora_veiculos;

CREATE TABLE Pessoa (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Endereco_Endereco VARCHAR(255),
    Endereco_Cidade VARCHAR(100),
    Endereco_Estado VARCHAR(50),
    Endereco_CEP VARCHAR(20),
    Telefone VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE Cliente (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CPF_CNPJ VARCHAR(20) UNIQUE NOT NULL,
    Tipo ENUM('PF', 'PJ') NOT NULL,
    ID_Pessoa INT,
    FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa(ID)
);

CREATE TABLE PessoaFisica (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CPF VARCHAR(11) UNIQUE NOT NULL,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID)
);

CREATE TABLE PessoaJuridica (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CNPJ VARCHAR(14) UNIQUE NOT NULL,
    NomeFantasia VARCHAR(100),
    RazaoSocial VARCHAR(100),
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID)
);

CREATE TABLE Funcionario (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Pessoa INT,
    ID_Cliente INT,
    CNH VARCHAR(20),
    DataExpiracaoCNH DATE,
    FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa(ID),
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID)
);

CREATE TABLE Grupo (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Descricao TEXT,
    ValorDiaria DECIMAL(10, 2)
);

CREATE TABLE Veiculo (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Placa VARCHAR(10) UNIQUE NOT NULL,
    Chassis VARCHAR(20) UNIQUE NOT NULL,
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Cor VARCHAR(20),
    ArCondicionado BOOLEAN,
    Mecanizacao ENUM('Manual', 'Automática'),
    Cadeirinha BOOLEAN,
    Dimensoes_Comprimento VARCHAR(20),
    Dimensoes_Largura VARCHAR(20),
    Dimensoes_Altura VARCHAR(20),
    Grupo INT,
    Fotos VARCHAR(255),
    EstadoConservacao TEXT,
    PressaoPneus VARCHAR(20),
    NivelOleo VARCHAR(20),
    FOREIGN KEY (Grupo) REFERENCES Grupo(ID)
);

CREATE TABLE Carro (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NumeroPassageiros INT,
    NumeroPortas INT,
    ID_Veiculo INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID)
);

CREATE TABLE Motocicleta (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Cilindradas INT,
    ID_Veiculo INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID)
);

CREATE TABLE Caminhao (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CapacidadeCarga DECIMAL(10, 2),
    ID_Veiculo INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID)
);

CREATE TABLE Acessorio (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE VeiculoAcessorio (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Veiculo INT,
    ID_Acessorio INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID),
    FOREIGN KEY (ID_Acessorio) REFERENCES Acessorio(ID)
);

CREATE TABLE Reserva (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente INT,
    ID_Veiculo INT,
    DataReserva DATE,
    DataRetirada DATE,
    DataDevolucao DATE,
    EstadoReserva VARCHAR(50),
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID),
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID)
);

CREATE TABLE Locacao (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Reserva INT,
    ID_Cliente INT,
    ID_Veiculo INT,
    DataRetirada DATE,
    HoraRetirada TIME,
    DataDevolucaoPrevista DATE,
    DataDevolucaoRealizada DATE,
    HoraDevolucao TIME,
    PatioSaida VARCHAR(100),
    PatioChegada VARCHAR(100),
    EstadoEntrega TEXT,
    EstadoDevolucao TEXT,
    ProtecoesAdicionais TEXT,
    ValorFinal DECIMAL(10, 2),
    FOREIGN KEY (ID_Reserva) REFERENCES Reserva(ID),
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID),
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID)
);

CREATE TABLE Prontuario (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Veiculo INT,
    DataRegistro DATE,
    DescricaoRegistro TEXT,
    TipoRegistro VARCHAR(50),
    ID_Funcionario INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID),
    FOREIGN KEY (ID_Funcionario) REFERENCES Funcionario(ID)
);
