from database.database import conectar
from models.usuario import criar_tabela_usuario,inserir_usuario,buscar_usuario

def registrar(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    # tem que testar as coisas necessarias para senha tipo se tem maiusculo essas coisas
    criar_tabela_usuario(cursor)
    inserir_usuario(cursor,nome,senha)

    conexao.commit()
    conexao.close()