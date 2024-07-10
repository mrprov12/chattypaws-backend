# tests/test_routes.py


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


def test_user_get_current_user(client, db):
    # Assuming a session or token mechanism is used to get the current user
    # Adjust the test based on your authentication mechanism
    response = client.get("/user")
    assert response.status_code == 200
    data = response.get_json()
    assert "user" in data


def test_notification_get_notification_history(client, db):
    response = client.get("/notification/1/stream/1")
    assert response.status_code == 200
    data = response.get_json()
    assert "notifications" in data


def test_image_processing_process_video(client, db):
    response = client.post("/image_processing/process_video")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Video processed successfully"


def test_image_processing_integrate_stream(client, db):
    response = client.post(
        "/image_processing/integrate_stream",
        json={"stream_url": "http://example.com/stream"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Stream integrated successfully"


def test_image_processing_store_results(client, db):
    processing_results = {
        "timestamp": "2024-06-30T12:34:56",
        "button_press": True,
        "additional_data": {},
    }
    response = client.post(
        "/image_processing/store_results",
        json={"processing_results": processing_results},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Results stored successfully"
    assert "result_id" in data


# Add more tests for other routes as needed
