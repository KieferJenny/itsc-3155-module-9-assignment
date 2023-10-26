from src.models.movie import Movie
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_view_movie_page(client):
    repo = get_movie_repository()
    movie = Movie(1,'Test title', 'test dir', 12)
    repo._db = {1: movie}

    response = client.get('/movies/1')
    assert response.status_code == 200
    assert movie.title.encode() in response.data

    response = client.get('/movies/2')
    assert response.status_code == 404
    assert "Movie not found".encode() in response.data

    return True