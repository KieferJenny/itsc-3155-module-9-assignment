# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository


def test_get_all_movies_with_movie():
    movie_repository = get_movie_repository()
    
    # Mock data
    movie_repository.create_movie("Test Movie", "Test Director", 5)
    
    movies = movie_repository.get_all_movies()
    
    # Clean up mock data
    movie_repository.clear_db()
    
    assert movies != None
    assert len(movies) > 0

    assert movies[next(iter(movies))].title == "Test Movie"

def test_get_all_movies_no_movies():
    movie_repository = get_movie_repository()
    
    # Mock data
    movies = movie_repository.get_all_movies()
    
    # Clean up mock data
    assert movies != None
    assert len(movies) == 0