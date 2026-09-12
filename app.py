from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tutores = []
alunos = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        tutores=tutores,
        alunos=alunos
    )


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


@app.route("/cadastrar-aluno", methods=["POST"])
def cadastrar_aluno():
    nome = request.form["nome_aluno"]
    raca = request.form["raca"]
    idade = request.form["idade"]
    porte = request.form["porte"]
    tutor_email = request.form["tutor"]

    aluno = {
        "nome": nome,
        "raca": raca,
        "idade": idade,
        "porte": porte,
        "tutor": tutor_email
    }

    alunos.append(aluno)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)