import json
from app import app

def test_home():
    """Prueba que la página cargue y tenga el formulario"""
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Analizador Lucas" in res.data
    assert b"1.0.5" in res.data
    assert b"textarea" in res.data

def test_predict_get():
    """Prueba el endpoint GET (Query Params)"""
    client = app.test_client()
    res = client.get("/predict?text=hola")
    data = res.get_json()
    assert res.status_code == 200
    assert data["score"] == 4
    assert data["input"] == "hola"
    assert data["version"] == "1.0.5"

def test_predict_post():
    """Prueba el endpoint POST (JSON)"""
    client = app.test_client()
    res = client.post("/predict", json={"text": "prueba"})
    data = res.get_json()
    assert res.status_code == 200
    assert data["score"] == 6
    assert data["input"] == "prueba"