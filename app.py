from flask import Flask, render_template,redirect,session

app = Flask(__name__)

#Vou deixar no no git mas o certo seria fazer isso:

#pip install python-dotenv
#criar secret key no .env
#SECRET_KEY=chave_secreta
#
# import os
# from dotenv import load_dotenv
# load_dotenv()

# app.secret_key = os.getenv("SECRET_KEY")

app.secret_key = "uma-chave-secreta-bem-grande"


#TELAS
@app.get("/")
def registro_tela():
    return render_template("registro.html")
    
@app.get("/login")
def login_tela():
    return render_template("login.html")

@app.get("/home")
def home_tela():
    #redireciona se nao tiver logado
    if "usuario" not in session:
        return redirect("/login")

    return render_template("home.html")

#APIs
from API.API_registro import rota_registro
from API.API_login import rota_login
rota_registro(app)
rota_login(app)

if __name__ == "__main__":
    app.run(debug=True)