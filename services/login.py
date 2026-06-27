from database.database import conectar
from models.usuario import buscar_usuario


def logar(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    print("TESTE ENTROU NO SERVICE LOGIN")
    usuario = buscar_usuario(cursor, nome, senha)
    
    from services.hash import verifica_senha
    if verifica_senha(senha,usuario) == True:
        print ("Aaaaaaaaa")
        return True
    

    conexao.commit()
    conexao.close()

    return "ok"