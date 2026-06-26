from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("registro.html")
    



from API.registro import rota_registro
rota_registro(app)

if __name__ == "__main__":
    app.run(debug=True)