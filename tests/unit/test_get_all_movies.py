# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

def test_get_all_movies():
    movie_repository = get_movie_repository()
    
    # Mock data
    movie_repository.create_movie("Test Movie", "Test Director", 5)
    
    movies = movie_repository.get_all_movies()
    
    # Clean up mock data
    movie_repository.clear_db()
    
    assert movies != None
    assert len(movies) > 0

    assert movies[next(iter(movies))].title == "Test Movie"

@pytest.fixture 
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_list_all_movies(client):
    response = client.get('/movies')
    assert response.status_code == 200
    assert b'<th>Movie Name</th>' in response.data






