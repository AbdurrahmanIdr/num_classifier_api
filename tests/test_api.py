"""
This module contains tests for the Flask API endpoints.

It includes tests for valid numbers, invalid numbers, zero, and negative numbers.
"""

import pytest
from app import create_app


@pytest.fixture
def test_client():
    """Set up a test client for the Flask app."""
    app = create_app()
    app.config["TESTING"] = True
    client_fix = app.test_client()
    return client_fix


def test_valid_number(test_client):
    """Test API with a valid number."""
    response = test_client.get("/api/classify-number?number=371")
    data = response.get_json()

    assert response.status_code == 200
    assert data["number"] == 371
    assert isinstance(data["is_prime"], bool)
    assert isinstance(data["is_perfect"], bool)
    assert isinstance(data["properties"], list)
    assert isinstance(data["digit_sum"], int)
    assert "fun_fact" in data


def test_invalid_number(test_client):
    """Test API with an invalid number (string input)."""
    response = test_client.get("/api/classify-number?number=abc")
    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] is True


def test_zero(test_client):
    """Test API with zero."""
    response = test_client.get("/api/classify-number?number=0")
    data = response.get_json()

    assert response.status_code == 200
    assert data["number"] == 0
    assert isinstance(data["is_prime"], bool)
    assert isinstance(data["is_perfect"], bool)
    assert isinstance(data["properties"], list)
    assert isinstance(data["digit_sum"], int)
    assert "fun_fact" in data


def test_negative_number(test_client):
    """Test API with a negative number."""
    response = test_client.get("/api/classify-number?number=-28")
    data = response.get_json()

    # If negative numbers are rejected, status code should be 400
    assert response.status_code == 400
    assert data["error"] is True
