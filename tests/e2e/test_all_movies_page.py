# TODO: Feature 1
import pytest
from app import app, get_repository

@pytest.fixture 
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_list_all_movies_api_call(client):
    response = client.get('/movies')
    assert response.status_code == 200


def test_list_all_movies_with_movie(client):
    movie_repository = get_repository()
    movie_repository.create_movie("Test Movie", "Test Director", 5)

    response = client.get('/movies')

    movie_repository.clear_db()

    assert response.status_code == 200
    assert b'<td>Test Movie</td>' in response.data

def test_list_all_movies_no_movie(client):
    response = client.get('/movies')
    
    assert response.status_code == 200
    assert b'<td>Test Movie</td>' not in response.data
