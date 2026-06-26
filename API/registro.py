from flask import request
from fastapi import HTTPException

from services.registro import registrar

def rota_registro(app):

    @app.post("/registro")
    def registro():

        nome = request.form["nome"]
        senha = request.form["password"]

        if not nome:
            raise HTTPException(status_code=400, detail="nome nao informado")
        if not senha:
            raise HTTPException(status_code=400, detail="senha nao informada")

        

        registrar(nome, senha)

        return "ok"
    
    # @app.post("/teste")
    # def teste():
    #     print ("aaaaaa")

    #     return "Recebido"