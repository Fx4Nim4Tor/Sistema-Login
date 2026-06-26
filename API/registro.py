from flask import request
from services.registro import registrar

def registrar_rotas(app):

    @app.post("/registro")
    def registro():

        nome = request.form["nome"]
        senha = request.form["password"]

        print(nome)
        print(senha)

        registrar(nome, senha)

        return "ok"
    
    # @app.post("/teste")
    # def teste():
    #     print ("aaaaaa")

    #     return "Recebido"