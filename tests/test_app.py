from app import app


def test_home_returns_200_and_message():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD Pipeline is Live" in response.data


def test_health_returns_healthy_json():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_unknown_route_returns_404():
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404
