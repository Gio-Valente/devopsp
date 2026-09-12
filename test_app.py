from app import app, tutores, alunos


def setup_function():
    tutores.clear()
    alunos.clear()


def test_pagina_inicial():
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert "Cãotinho" in resposta.get_data(as_text=True)


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