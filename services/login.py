from database.database import conectar
from models.usuario import buscar_usuario
from services.hash import verifica_senha

def logar(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    print("TESTE ENTROU NO SERVICE LOGIN")
    usuario = buscar_usuario(cursor, nome, senha)
    
    if usuario is None:
        conexao.close()
        return False

    if verifica_senha(senha,usuario) == True:
        return True
    

    conexao.commit()
    conexao.close()

    return "Usuário ou senha inválidos", 401