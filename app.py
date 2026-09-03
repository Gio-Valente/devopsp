from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tutores = []


@app.route("/")
def home():
    return render_template("index.html", tutores=tutores)


@app.route("/cadastrar-tutor", methods=["POST"])
def cadastrar_tutor():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form["email"]

    tutor = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    tutores.append(tutor)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)