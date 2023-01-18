from flask import Flask, render_template

app = Flask(__name__)


# criação de página
# route → rota/ caminho/ www.bellini.com/...
# função → o que vai ser exibido
# template → códigos html e CSS
# criar 1ª página
@app.route("/")  # atribuir uma nova funcionalidade
def homepage():
    return render_template("home.html")

@app.route("/contatos")
def contatos():
    return render_template("contato.html")

@app.route("/lazer")
def lazer():
    return render_template("lazer.html")

@app.route("/reservas")
def reservas():
    return render_template("reservas.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/acomodacoes")
def acomodacoes():
    return render_template("acomodacoes.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# deploy do site servidor oracle;
