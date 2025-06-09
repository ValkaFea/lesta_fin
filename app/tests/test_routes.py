import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_ping(client):
    rv = client.get('/ping')
    assert rv.status_code == 200
    assert rv.get_json() == {"status": "ok"}


def test_submit_and_results(client):
    rv = client.post('/submit', json={"name": "Test", "score": 90})
    assert rv.status_code == 201

    rv = client.get('/results')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['results'][0]['name'] == "Test"
    assert data['results'][0]['score'] == 90