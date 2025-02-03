import pytest
from app import create_app


@pytest.fixture
def client():
    """Set up a test client for the Flask app."""
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    return client


def test_valid_number(client):
    """Test API with a valid number."""
    response = client.get("/api/classify-number?number=371")
    data = response.get_json()

    assert response.status_code == 200
    assert data["number"] == 371
    assert isinstance(data["is_prime"], bool)
    assert isinstance(data["is_perfect"], bool)
    assert isinstance(data["properties"], list)
    assert isinstance(data["digit_sum"], int)
    assert "fun_fact" in data


def test_invalid_number(client):
    """Test API with an invalid number (string input)."""
    response = client.get("/api/classify-number?number=abc")
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] is True


def test_zero(client):
    """Test API with zero."""
    response = client.get("/api/classify-number?number=0")
    data = response.get_json()

    assert response.status_code == 200
    assert data["number"] == 0
    assert isinstance(data["is_prime"], bool)
    assert isinstance(data["is_perfect"], bool)
    assert isinstance(data["properties"], list)
    assert isinstance(data["digit_sum"], int)
    assert "fun_fact" in data


def test_negative_number(client):
    """Test API with a negative number."""
    response = client.get("/api/classify-number?number=-28")
    data = response.get_json()

    # If negative numbers are rejected, status code should be 400
    assert response.status_code == 400
    assert data["error"] is True
