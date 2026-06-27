from flask import request
from fastapi import HTTPException

from services.login import logar

def rota_login(app):
    @app.post("/login")
    def login():
        nome = request.form["nome"]
        senha = request.form["password"]

        if not nome:
            raise HTTPException(status_code=400, detail="nome nao informado")
        if not senha:
            raise HTTPException(status_code=400, detail="senha nao informada")
        
        print("ENTROU NA API")
        logar(nome, senha)

        return "ok"