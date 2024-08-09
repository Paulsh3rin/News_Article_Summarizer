import pytest
from app import app
from model import perform_summarization

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<!DOCTYPE html>' in rv.data  # Assuming your index.html contains this

def test_summarize_success(client):
    """Test the summarize route with valid data."""
    rv = client.post('/summarize', json={'article': 'This is a sample article for testing.'})
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'summary' in data
    assert 'keywords' in data

def test_summarize_no_data(client):
    """Test the summarize route with no data."""
    rv = client.post('/summarize', json={})
    assert rv.status_code == 400
    data = rv.get_json()
    assert 'error' in data

def test_perform_summarization():
    """Test the perform_summarization function directly."""
    text = "This is a sample article. It contains multiple sentences. It is used for testing summarization."
    summary, keywords = perform_summarization(text)
    assert isinstance(summary, str)
    assert isinstance(keywords, list)
    assert len(keywords) > 0

def test_flask_installed():
    try:
        import flask
    except ImportError:
        pytest.fail("Flask is not installed")