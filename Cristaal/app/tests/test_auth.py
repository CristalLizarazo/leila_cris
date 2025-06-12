import json
from app import db, create_app
from app.models import User
from werkzeug.security import generate_password_hash

def test_register_user(test_client):
    response = test_client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 201
    assert b"User created" in response.data

def test_register_existing_user(test_client):
    response = test_client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 400

def test_login_valid(test_client):
    response = test_client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_login_invalid(test_client):
    response = test_client.post("/api/auth/login", json={
        "username": "wronguser",
        "password": "wrongpass"
    })
    assert response.status_code == 401
