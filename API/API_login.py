from flask import request

from services.login import logar

def rota_login(app):
    @app.post("/login")
    def login():
        nome = request.form.get("nome")
        senha = request.form.get("password")

        if not nome:
            return "Nome não informado", 400
        if not senha:
            return "Senha não informada", 400
        
        print("ENTROU NA API")

        if logar(nome, senha):
            return "", 200

        return "Usuário ou senha inválidos", 401