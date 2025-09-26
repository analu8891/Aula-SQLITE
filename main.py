# Criar um banco de dados SQLite e uma tabela
import sqlite3

# Criar a conexão com o banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor" que será usado para executar os comando sql
cursor = conexao.cursor()

#Criar uma tabela no banco
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER  PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT                
#    )               
# """)
# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite aideia do aluno: "))
# curso = input("Digite o curso do aluno: ")
# # Inseror um dado na tabela 
# cursor.execute("""
# INSERT INTO alunos (nome,idade,curso)
# VALUES (?,?,?)               
# """,
# (nome,idade,curso)
# )

# #Confirmar as alterações no banco 
# conexao.commit()


#Inserir varios alunos de uma só vez
# alunos = [
#     ("Yago",28,"Direito"),
#     ("Jessica",24,"computação"),
#     ("Breno",52,"Computação"),
# ]
# # executemany permite inserir multiplas linhas de uma so vez
# cursor.executemany("""
# INSERT INTO alunos (nome,idade,curso)
# VALUES (?,?,?)                   
#  """,
# (alunos)
# )
# conexao.commit()


#Atualizar dados no banco
# cursor.execute("""
# UPDATE alunos
# SET idade = ?, curso = ?
# WHERE id = ?           
# """,
#     (61,"Medicina", 2)
# )
# conexao.commit()

#função listar dados no banco 
#Consultar os dados no banco
cursor.execute("SELECT * FROM alunos")
#fetchall traz todas as linhas da consulta 
for linha in cursor.fetchall():
    print(f"ID: {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]} | CURSO: {linha[3]}")
print("-"*60)
pesquisar = input("digite o curso que deseja pesquisar os alunos:")
cursor.execute("SELECT nome,idade FROM alunos WHERE curso = ?", (pesquisar,))
print(f"Alunos do curso de {pesquisar}")
for linha in cursor.fetchall():
    print(f"NOME: {linha[0]} | IDADE: {linha[1]}")