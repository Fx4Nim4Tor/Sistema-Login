from database.database import conectar

def logar(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    print("TESTE ENTROU NO SERVICE LOGIN")

    conexao.commit()
    conexao.close()

    return "ABRACADABRA"