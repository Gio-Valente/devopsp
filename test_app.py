from app import app, tutores, alunos


# ======================================================
# PREPARAÇÃO DOS TESTES
# ======================================================

def setup_function():
    """
    Limpa os dados antes da execução de cada teste.
    Assim, um teste não interfere no resultado do outro.
    """
    tutores.clear()
    alunos.clear()


# ======================================================
# TESTE 1 - PÁGINA INICIAL
# ======================================================

def test_pagina_inicial():
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert "Cãotinho" in resposta.get_data(as_text=True)


# ======================================================
# TESTE 2 - CADASTRO DE TUTOR
# ======================================================

def test_cadastro_tutor():
    cliente = app.test_client()

    resposta = cliente.post(
        "/cadastrar-tutor",
        data={
            "nome": "Giovanna",
            "telefone": "(41) 99999-9999",
            "email": "gio@email.com"
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert "Giovanna" in resposta.get_data(as_text=True)
    assert len(tutores) == 1


# ======================================================
# TESTE 3 - CADASTRO DE ALUNO
# ======================================================

def test_cadastro_aluno():
    cliente = app.test_client()

    tutores.append({
        "nome": "Giovanna",
        "telefone": "(41) 99999-9999",
        "email": "gio@email.com"
    })

    resposta = cliente.post(
        "/cadastrar-aluno",
        data={
            "nome_aluno": "Paçoca",
            "raca": "Shih-tzu",
            "idade": "5",
            "porte": "Pequeno",
            "tutor": "gio@email.com"
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert "Paçoca" in resposta.get_data(as_text=True)
    assert len(alunos) == 1


# ======================================================
# TESTE 4 - DADOS DO TUTOR CADASTRADO
# ======================================================

def test_dados_tutor_cadastrado():
    cliente = app.test_client()

    cliente.post(
        "/cadastrar-tutor",
        data={
            "nome": "Maria",
            "telefone": "(41) 98888-7777",
            "email": "maria@email.com"
        },
        follow_redirects=True
    )

    assert len(tutores) == 1
    assert tutores[0]["nome"] == "Maria"
    assert tutores[0]["email"] == "maria@email.com"
    assert tutores[0]["telefone"] == "(41) 98888-7777"


# ======================================================
# TESTE 5 - DADOS DO ALUNO CADASTRADO
# ======================================================

def test_dados_aluno_cadastrado():
    cliente = app.test_client()

    tutores.append({
        "nome": "Carlos",
        "telefone": "(41) 97777-6666",
        "email": "carlos@email.com"
    })

    cliente.post(
        "/cadastrar-aluno",
        data={
            "nome_aluno": "Thor",
            "raca": "Golden Retriever",
            "idade": "3",
            "porte": "Grande",
            "tutor": "carlos@email.com"
        },
        follow_redirects=True
    )

    assert len(alunos) == 1
    assert alunos[0]["nome"] == "Thor"
    assert alunos[0]["raca"] == "Golden Retriever"
    assert alunos[0]["idade"] == "3"
    assert alunos[0]["porte"] == "Grande"