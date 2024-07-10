# tests/test_app.py


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Welcome to ChattyPaws Backend API!"


def test_user_register(client, db):
    response = client.post(
        "/user/register",
        json={"email": "test@example.com", "password": "securepassword"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User registered successfully"
    assert "user_id" in data


def test_user_login(client, db):
    client.post(
        "/user/register",
        json={"email": "test@example.com", "password": "securepassword"},
    )
    response = client.post(
        "/user/login", json={"email": "test@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Login successful"


def test_notification_get_notification_history(client, db):
    response = client.get("/notification/1/stream/1")
    assert response.status_code == 200
    data = response.get_json()
    assert "notifications" in data


# Add more tests for other routes
