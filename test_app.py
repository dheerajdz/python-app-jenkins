import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'message' in data

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello, World!'
    assert data['author'] == 'DevOps CI/CD'

def test_info_endpoint(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app_name'] == 'DevOps Sample App'
    assert data['version'] == '1.0.0'
    assert '/health' in data['endpoints']
    assert '/hello' in data['endpoints']
    assert '/api/info' in data['endpoints']