from flask import Flask, render_template

app = Flask(__name__)
#criação de página
# route → rota/ caminho/ www.bellini.com/...
# função → o que vai ser exibido
# template → códigos html e CSS
# criar 1ª página
@app.route("/")  # atribuir uma nova funcionalidade
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contacts():
    return render_template("contacts.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
