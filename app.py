import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

'''
Anderson Marden de Sousa Silva 
Dre: 119113730
'''

# Função para criar a conexão com o banco de dados
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='locadora_veiculos',
            user='root',
            password='82021495'
        )
        if connection.is_connected():
            print("Conexão com o banco de dados foi estabelecida.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para fechar a conexão com o banco de dados
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão com o banco de dados foi encerrada.")

# Funções para Cadastro da Frota

def cadastrar_veiculo():
    placa = placa_entry.get()
    chassis = chassis_entry.get()
    marca = marca_entry.get()
    modelo = modelo_entry.get()
    cor = cor_entry.get()
    grupo = grupo_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Veiculo (Placa, Chassis, Marca, Modelo, Cor, Grupo) VALUES (%s, %s, %s, %s, %s, %s)",
                (placa, chassis, marca, modelo, cor, grupo)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def atualizar_prontuario_veiculo():
    veiculo_id = veiculo_id_prontuario_entry.get()
    descricao_registro = descricao_registro_entry.get()
    tipo_registro = tipo_registro_entry.get()
    funcionario_id = funcionario_id_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Prontuario (ID_Veiculo, DataRegistro, DescricaoRegistro, TipoRegistro, ID_Funcionario) VALUES (%s, CURDATE(), %s, %s, %s)",
                (veiculo_id, descricao_registro, tipo_registro, funcionario_id)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Prontuário atualizado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def cadastrar_foto_veiculo():
    veiculo_id = veiculo_id_foto_entry.get()
    caminho_foto = caminho_foto_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE Veiculo SET Fotos = %s WHERE ID = %s",
                (caminho_foto, veiculo_id)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Foto do veículo cadastrada com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

# Funções para Cadastro de Clientes Locatários

def cadastrar_cliente_pf():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    cidade = cidade_entry.get()
    estado = estado_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    cpf = cpf_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Primeiro, inserir dados na tabela Pessoa
            cursor.execute(
                "INSERT INTO Pessoa (Nome, Endereco_Endereco, Endereco_Cidade, Endereco_Estado, Endereco_CEP, Telefone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (nome, endereco, cidade, estado, cep, telefone, email)
            )
            pessoa_id = cursor.lastrowid  # Obter o ID da pessoa recém-inserida
            
            # Depois, inserir dados na tabela Cliente
            cursor.execute(
                "INSERT INTO Cliente (CPF_CNPJ, Tipo, ID_Pessoa) VALUES (%s, 'PF', %s)",
                (cpf, pessoa_id)
            )
            cliente_id = cursor.lastrowid  # Obter o ID do cliente recém-inserido
            
            # Finalmente, inserir dados na tabela PessoaFisica
            cursor.execute(
                "INSERT INTO PessoaFisica (CPF, ID_Cliente) VALUES (%s, %s)",
                (cpf, cliente_id)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Cliente PF cadastrado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def cadastrar_cliente_pj():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    cidade = cidade_entry.get()
    estado = estado_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    cnpj = cnpj_entry.get()
    nome_fantasia = nome_fantasia_entry.get()
    razao_social = razao_social_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Primeiro, inserir dados na tabela Pessoa
            cursor.execute(
                "INSERT INTO Pessoa (Nome, Endereco_Endereco, Endereco_Cidade, Endereco_Estado, Endereco_CEP, Telefone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (nome, endereco, cidade, estado, cep, telefone, email)
            )
            pessoa_id = cursor.lastrowid  # Obter o ID da pessoa recém-inserida
            
            # Depois, inserir dados na tabela Cliente
            cursor.execute(
                "INSERT INTO Cliente (CPF_CNPJ, Tipo, ID_Pessoa) VALUES (%s, 'PJ', %s)",
                (cnpj, pessoa_id)
            )
            cliente_id = cursor.lastrowid  # Obter o ID do cliente recém-inserido
            
            # Finalmente, inserir dados na tabela PessoaJuridica
            cursor.execute(
                "INSERT INTO PessoaJuridica (CNPJ, NomeFantasia, RazaoSocial, ID_Cliente) VALUES (%s, %s, %s, %s)",
                (cnpj, nome_fantasia, razao_social, cliente_id)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Cliente PJ cadastrado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def cadastrar_motorista():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    cidade = cidade_entry.get()
    estado = estado_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    cnh = cnh_entry.get()
    data_expiracao_cnh = data_expiracao_cnh_entry.get()
    cliente_id = cliente_id_motorista_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Primeiro, inserir dados na tabela Pessoa
            cursor.execute(
                "INSERT INTO Pessoa (Nome, Endereco_Endereco, Endereco_Cidade, Endereco_Estado, Endereco_CEP, Telefone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (nome, endereco, cidade, estado, cep, telefone, email)
            )
            pessoa_id = cursor.lastrowid  # Obter o ID da pessoa recém-inserida
            
            # Depois, inserir dados na tabela Funcionario
            cursor.execute(
                "INSERT INTO Funcionario (ID_Pessoa, ID_Cliente, CNH, DataExpiracaoCNH) VALUES (%s, %s, %s, %s)",
                (pessoa_id, cliente_id, cnh, data_expiracao_cnh)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Motorista cadastrado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

# Funções para Reserva de Veículo e Relatórios

def gerar_relatorio_patio():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Veiculo")
            veiculos = cursor.fetchall()
            relatorio_text.delete(1.0, tk.END)
            relatorio_text.insert(tk.END, "Relatório de Pátio:\n")
            for veiculo in veiculos:
                relatorio_text.insert(tk.END, f"{veiculo}\n")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
        finally:
            cursor.close()
            close_connection(connection)

def gerar_relatorio_locacao():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Locacao")
            locacoes = cursor.fetchall()
            relatorio_text.delete(1.0, tk.END)
            relatorio_text.insert(tk.END, "Relatório de Locação:\n")
            for locacao in locacoes:
                relatorio_text.insert(tk.END, f"{locacao}\n")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
        finally:
            cursor.close()
            close_connection(connection)

def gerar_relatorio_fila_espera():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Reserva WHERE EstadoReserva = 'Em espera'")
            reservas = cursor.fetchall()
            relatorio_text.delete(1.0, tk.END)
            relatorio_text.insert(tk.END, "Relatório de Fila de Espera:\n")
            for reserva in reservas:
                relatorio_text.insert(tk.END, f"{reserva}\n")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
        finally:
            cursor.close()
            close_connection(connection)

# Funções para Acompanhamento de Contrato de Locação

def iniciar_locacao():
    cliente_id = cliente_id_entry.get()
    veiculo_id = veiculo_id_entry.get()
    data_retirada = data_retirada_entry.get()
    hora_retirada = hora_retirada_entry.get()
    data_devolucao_prevista = data_devolucao_prevista_entry.get()
    patio_saida = patio_saida_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Locacao (ID_Cliente, ID_Veiculo, DataRetirada, HoraRetirada, DataDevolucaoPrevista, PatioSaida, EstadoEntrega) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (cliente_id, veiculo_id, data_retirada, hora_retirada, data_devolucao_prevista, patio_saida, 'Bom')
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Início de locação registrado com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def fechar_locacao():
    locacao_id = locacao_id_entry.get()
    patio_chegada = patio_chegada_entry.get()
    estado_devolucao = estado_devolucao_entry.get()
    protecoes_adicionais = protecoes_adicionais_entry.get()
    valor_final = valor_final_entry.get()
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                UPDATE Locacao
                SET DataDevolucaoRealizada = CURDATE(), 
                    HoraDevolucao = CURTIME(), 
                    PatioChegada = %s, 
                    EstadoDevolucao = %s, 
                    ProtecoesAdicionais = %s, 
                    ValorFinal = %s
                WHERE ID = %s
                """,
                (patio_chegada, estado_devolucao, protecoes_adicionais, valor_final, locacao_id)
            )
            cursor.execute("SELECT ID_Veiculo FROM Locacao WHERE ID = %s", (locacao_id,))
            veiculo_id = cursor.fetchone()[0]
            cursor.execute(
                "UPDATE Veiculo SET EstadoConservacao = %s WHERE ID = %s",
                ("Disponível", veiculo_id)
            )
            connection.commit()
            messagebox.showinfo("Sucesso", "Locação fechada com sucesso.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

def controle_cobranca():
    locacao_id = locacao_id_cobranca_entry.get()
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT ValorFinal FROM Locacao WHERE ID = %s", (locacao_id,))
            valor_final = cursor.fetchone()[0]
            messagebox.showinfo("Cobrança", f"O valor final da locação é: R${valor_final:.2f}")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro: {err}")
        finally:
            cursor.close()
            close_connection(connection)

# Interface Gráfica com Tkinter
app = tk.Tk()
app.title("Locadora de Veículos")

# Canvas e Frame para a barra de rolagem
canvas = tk.Canvas(app)
scroll_y = tk.Scrollbar(app, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)

# Configurar a barra de rolagem
frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

# Seções de Cadastro da Frota

# Cadastro de Veículo
tk.Label(frame, text="Cadastro de Veículo").grid(row=0, column=0, columnspan=2)
tk.Label(frame, text="Placa:").grid(row=1, column=0)
placa_entry = tk.Entry(frame)
placa_entry.grid(row=1, column=1)

tk.Label(frame, text="Chassis:").grid(row=2, column=0)
chassis_entry = tk.Entry(frame)
chassis_entry.grid(row=2, column=1)

tk.Label(frame, text="Marca:").grid(row=3, column=0)
marca_entry = tk.Entry(frame)
marca_entry.grid(row=3, column=1)

tk.Label(frame, text="Modelo:").grid(row=4, column=0)
modelo_entry = tk.Entry(frame)
modelo_entry.grid(row=4, column=1)

tk.Label(frame, text="Cor:").grid(row=5, column=0)
cor_entry = tk.Entry(frame)
cor_entry.grid(row=5, column=1)

tk.Label(frame, text="Grupo:").grid(row=6, column=0)
grupo_entry = tk.Entry(frame)
grupo_entry.grid(row=6, column=1)

tk.Button(frame, text="Cadastrar Veículo", command=cadastrar_veiculo).grid(row=7, column=0, columnspan=2)

# Atualização do Prontuário do Veículo
tk.Label(frame, text="Atualização do Prontuário do Veículo").grid(row=8, column=0, columnspan=2)
tk.Label(frame, text="ID Veículo:").grid(row=9, column=0)
veiculo_id_prontuario_entry = tk.Entry(frame)
veiculo_id_prontuario_entry.grid(row=9, column=1)

tk.Label(frame, text="Descrição Registro:").grid(row=10, column=0)
descricao_registro_entry = tk.Entry(frame)
descricao_registro_entry.grid(row=10, column=1)

tk.Label(frame, text="Tipo Registro:").grid(row=11, column=0)
tipo_registro_entry = tk.Entry(frame)
tipo_registro_entry.grid(row=11, column=1)

tk.Label(frame, text="ID Funcionário:").grid(row=12, column=0)
funcionario_id_entry = tk.Entry(frame)
funcionario_id_entry.grid(row=12, column=1)

tk.Button(frame, text="Atualizar Prontuário", command=atualizar_prontuario_veiculo).grid(row=13, column=0, columnspan=2)

# Cadastro de Foto do Veículo
tk.Label(frame, text="Cadastro de Foto do Veículo").grid(row=14, column=0, columnspan=2)
tk.Label(frame, text="ID Veículo:").grid(row=15, column=0)
veiculo_id_foto_entry = tk.Entry(frame)
veiculo_id_foto_entry.grid(row=15, column=1)

tk.Label(frame, text="Caminho da Foto:").grid(row=16, column=0)
caminho_foto_entry = tk.Entry(frame)
caminho_foto_entry.grid(row=16, column=1)

tk.Button(frame, text="Cadastrar Foto", command=cadastrar_foto_veiculo).grid(row=17, column=0, columnspan=2)

# Seções de Cadastro de Clientes Locatários

# Cadastro de Cliente PF
tk.Label(frame, text="Cadastro de Cliente PF").grid(row=18, column=0, columnspan=2)
tk.Label(frame, text="Nome:").grid(row=19, column=0)
nome_entry = tk.Entry(frame)
nome_entry.grid(row=19, column=1)

tk.Label(frame, text="Endereço:").grid(row=20, column=0)
endereco_entry = tk.Entry(frame)
endereco_entry.grid(row=20, column=1)

tk.Label(frame, text="Cidade:").grid(row=21, column=0)
cidade_entry = tk.Entry(frame)
cidade_entry.grid(row=21, column=1)

tk.Label(frame, text="Estado:").grid(row=22, column=0)
estado_entry = tk.Entry(frame)
estado_entry.grid(row=22, column=1)

tk.Label(frame, text="CEP:").grid(row=23, column=0)
cep_entry = tk.Entry(frame)
cep_entry.grid(row=23, column=1)

tk.Label(frame, text="Telefone:").grid(row=24, column=0)
telefone_entry = tk.Entry(frame)
telefone_entry.grid(row=24, column=1)

tk.Label(frame, text="Email:").grid(row=25, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=25, column=1)

tk.Label(frame, text="CPF:").grid(row=26, column=0)
cpf_entry = tk.Entry(frame)
cpf_entry.grid(row=26, column=1)

tk.Button(frame, text="Cadastrar Cliente PF", command=cadastrar_cliente_pf).grid(row=27, column=0, columnspan=2)

# Cadastro de Cliente PJ
tk.Label(frame, text="Cadastro de Cliente PJ").grid(row=28, column=0, columnspan=2)
tk.Label(frame, text="Nome:").grid(row=29, column=0)
nome_entry = tk.Entry(frame)
nome_entry.grid(row=29, column=1)

tk.Label(frame, text="Endereço:").grid(row=30, column=0)
endereco_entry = tk.Entry(frame)
endereco_entry.grid(row=30, column=1)

tk.Label(frame, text="Cidade:").grid(row=31, column=0)
cidade_entry = tk.Entry(frame)
cidade_entry.grid(row=31, column=1)

tk.Label(frame, text="Estado:").grid(row=32, column=0)
estado_entry = tk.Entry(frame)
estado_entry.grid(row=32, column=1)

tk.Label(frame, text="CEP:").grid(row=33, column=0)
cep_entry = tk.Entry(frame)
cep_entry.grid(row=33, column=1)

tk.Label(frame, text="Telefone:").grid(row=34, column=0)
telefone_entry = tk.Entry(frame)
telefone_entry.grid(row=34, column=1)

tk.Label(frame, text="Email:").grid(row=35, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=35, column=1)

tk.Label(frame, text="CNPJ:").grid(row=36, column=0)
cnpj_entry = tk.Entry(frame)
cnpj_entry.grid(row=36, column=1)

tk.Label(frame, text="Nome Fantasia:").grid(row=37, column=0)
nome_fantasia_entry = tk.Entry(frame)
nome_fantasia_entry.grid(row=37, column=1)

tk.Label(frame, text="Razão Social:").grid(row=38, column=0)
razao_social_entry = tk.Entry(frame)
razao_social_entry.grid(row=38, column=1)

tk.Button(frame, text="Cadastrar Cliente PJ", command=cadastrar_cliente_pj).grid(row=39, column=0, columnspan=2)

# Cadastro de Motoristas
tk.Label(frame, text="Cadastro de Motoristas").grid(row=40, column=0, columnspan=2)
tk.Label(frame, text="Nome:").grid(row=41, column=0)
nome_entry = tk.Entry(frame)
nome_entry.grid(row=41, column=1)

tk.Label(frame, text="Endereço:").grid(row=42, column=0)
endereco_entry = tk.Entry(frame)
endereco_entry.grid(row=42, column=1)

tk.Label(frame, text="Cidade:").grid(row=43, column=0)
cidade_entry = tk.Entry(frame)
cidade_entry.grid(row=43, column=1)

tk.Label(frame, text="Estado:").grid(row=44, column=0)
estado_entry = tk.Entry(frame)
estado_entry.grid(row=44, column=1)

tk.Label(frame, text="CEP:").grid(row=45, column=0)
cep_entry = tk.Entry(frame)
cep_entry.grid(row=45, column=1)

tk.Label(frame, text="Telefone:").grid(row=46, column=0)
telefone_entry = tk.Entry(frame)
telefone_entry.grid(row=46, column=1)

tk.Label(frame, text="Email:").grid(row=47, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=47, column=1)

tk.Label(frame, text="CNH:").grid(row=48, column=0)
cnh_entry = tk.Entry(frame)
cnh_entry.grid(row=48, column=1)

tk.Label(frame, text="Data Expiração CNH:").grid(row=49, column=0)
data_expiracao_cnh_entry = tk.Entry(frame)
data_expiracao_cnh_entry.grid(row=49, column=1)

tk.Label(frame, text="ID Cliente:").grid(row=50, column=0)
cliente_id_motorista_entry = tk.Entry(frame)
cliente_id_motorista_entry.grid(row=50, column=1)

tk.Button(frame, text="Cadastrar Motorista", command=cadastrar_motorista).grid(row=51, column=0, columnspan=2)

# Seções de Relatórios
tk.Label(frame, text="Relatórios").grid(row=52, column=0, columnspan=2)
tk.Button(frame, text="Relatório de Pátio", command=gerar_relatorio_patio).grid(row=53, column=0, columnspan=2)
tk.Button(frame, text="Relatório de Locação", command=gerar_relatorio_locacao).grid(row=54, column=0, columnspan=2)
tk.Button(frame, text="Relatório de Fila de Espera", command=gerar_relatorio_fila_espera).grid(row=55, column=0, columnspan=2)

relatorio_text = tk.Text(frame, height=10, width=80)
relatorio_text.grid(row=56, column=0, columnspan=2)

# Seções de Acompanhamento de Contrato de Locação

# Início de Locação
tk.Label(frame, text="Início de Locação").grid(row=57, column=0, columnspan=2)
tk.Label(frame, text="ID Cliente:").grid(row=58, column=0)
cliente_id_entry = tk.Entry(frame)
cliente_id_entry.grid(row=58, column=1)

tk.Label(frame, text="ID Veículo:").grid(row=59, column=0)
veiculo_id_entry = tk.Entry(frame)
veiculo_id_entry.grid(row=59, column=1)

tk.Label(frame, text="Data Retirada:").grid(row=60, column=0)
data_retirada_entry = tk.Entry(frame)
data_retirada_entry.grid(row=60, column=1)

tk.Label(frame, text="Hora Retirada:").grid(row=61, column=0)
hora_retirada_entry = tk.Entry(frame)
hora_retirada_entry.grid(row=61, column=1)

tk.Label(frame, text="Data Devolução Prevista:").grid(row=62, column=0)
data_devolucao_prevista_entry = tk.Entry(frame)
data_devolucao_prevista_entry.grid(row=62, column=1)

tk.Label(frame, text="Pátio Saída:").grid(row=63, column=0)
patio_saida_entry = tk.Entry(frame)
patio_saida_entry.grid(row=63, column=1)

tk.Button(frame, text="Iniciar Locação", command=iniciar_locacao).grid(row=64, column=0, columnspan=2)

# Fechar Locação
tk.Label(frame, text="Fechar Locação").grid(row=65, column=0, columnspan=2)
tk.Label(frame, text="ID Locação:").grid(row=66, column=0)
locacao_id_entry = tk.Entry(frame)
locacao_id_entry.grid(row=66, column=1)

tk.Label(frame, text="Pátio Chegada:").grid(row=67, column=0)
patio_chegada_entry = tk.Entry(frame)
patio_chegada_entry.grid(row=67, column=1)

tk.Label(frame, text="Estado Devolução:").grid(row=68, column=0)
estado_devolucao_entry = tk.Entry(frame)
estado_devolucao_entry.grid(row=68, column=1)

tk.Label(frame, text="Proteções Adicionais:").grid(row=69, column=0)
protecoes_adicionais_entry = tk.Entry(frame)
protecoes_adicionais_entry.grid(row=69, column=1)

tk.Label(frame, text="Valor Final:").grid(row=70, column=0)
valor_final_entry = tk.Entry(frame)
valor_final_entry.grid(row=70, column=1)

tk.Button(frame, text="Fechar Locação", command=fechar_locacao).grid(row=71, column=0, columnspan=2)

# Controle de Cobrança
tk.Label(frame, text="Controle de Cobrança").grid(row=72, column=0, columnspan=2)
tk.Label(frame, text="ID Locação:").grid(row=73, column=0)
locacao_id_cobranca_entry = tk.Entry(frame)
locacao_id_cobranca_entry.grid(row=73, column=1)

tk.Button(frame, text="Controle de Cobrança", command=controle_cobranca).grid(row=74, column=0, columnspan=2)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

app.mainloop()
