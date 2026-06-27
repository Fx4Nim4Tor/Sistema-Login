from flask import Flask, render_template

app = Flask(__name__)

#TELAS
@app.get("/")
def registro_tela():
    return render_template("registro.html")
    
@app.get("/login")
def login_tela():
    return render_template("login.html")

@app.get("/home")
def home_tela():
    return render_template("home.html")

#APIs
from API.API_registro import rota_registro
from API.API_login import rota_login
rota_registro(app)
rota_login(app)

if __name__ == "__main__":
    app.run(debug=True)