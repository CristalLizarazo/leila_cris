def test_create_book_with_token(test_client):
    # Crear usuario primero
    test_client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass"
    })

    # Hacer login
    login = test_client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })

    # Obtener token
    token = login.get_json().get("access_token")

    # Ahora sí crear el libro
    response = test_client.post("/api/books/", 
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Test Book", "author": "Test Author"}
    )

    assert response.status_code == 201


def test_create_book_without_token(test_client):
    response = test_client.post("/api/books/", json={
        "title": "Sin token",
        "author": "Nadie"
    })
    assert response.status_code == 401
