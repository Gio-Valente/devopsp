from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Cãotinho</h1>
    <p>Sistema básico de gestão para creche de cães.</p>

    <h2>Funcionalidades</h2>

    <ul>
        <li>Cadastro de au-lunos</li>
        <li>Cadastro de tutores</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)