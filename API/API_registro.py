from flask import request

from services.registro import registrar

def rota_registro(app):

    @app.post("/registro")
    def registro():

        nome = request.form.get("nome")
        senha = request.form.get("password")

        if not nome:
            return "Nome não informado", 400
        if not senha:
            return "Senha não informada", 400

        
        registrar(nome, senha)

        return "ok"
    
    # @app.post("/teste")
    # def teste():
    #     print ("aaaaaa")

    #     return "Recebido"