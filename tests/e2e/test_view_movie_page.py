import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client    

def test_call_page(client):
    response = client.get('/movies')
    assert response.status_code == 200

def test_get_single_movie(client):
    repo = get_movie_repository()
    movie = Movie(1,'test title','test dir',4)
    repo._db = {1: movie}
    movie.movie_id = 1

    response = client.get('/movies/1')
    assert response.status_code == 200
    assert movie.title.encode() in response.data
    assert movie.director.encode() in response.data
    assert str(movie.rating).encode() in response.data

def test_movie_not_exist(client):
    repo = get_movie_repository()
    movie = Movie(1,'test title','test dir',5)
    repo._db = {1: movie}

    response = client.get('movies/2')
    assert response.status_code == 404
    assert 'Movie not found'.encode() in response.data