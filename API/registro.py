from flask import request

def registrar_rotas(app):

    @app.post("/registro")
    def registro():

        nome = request.form["nome"]
        senha = request.form["password"]

        print(nome)
        print(senha)

        return "Recebido"