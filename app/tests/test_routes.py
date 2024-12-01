import sys
import os
import pytest

# Ensure the root directory is in the sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now, you can import from the app package
from app.routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_crawl_valid_url(client):
    response = client.post('/crawl', json={"url": "http://example.com"})
    assert response.status_code == 200
    assert isinstance(response.json, dict), "Response should be a JSON dictionary"

def test_crawl_invalid_url(client):
    response = client.post('/crawl', json={"url": "http://invalid-url"})
    assert response.status_code == 200
    assert response.json == {}, "Invalid URLs should return an empty sitemap"

def test_crawl_missing_url(client):
    response = client.post('/crawl', json={})
    assert response.status_code == 400
    assert response.json == {"error": "URL is required"}
