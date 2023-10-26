import pytest
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
    movie_repository = get_movie_repository()

    movie = movie_repository.create_movie("Test Movie", "Test Director", 5)

    retrieved_movie = movie_repository.get_movie_by_title("Test Movie")

    assert retrieved_movie is not None
    assert retrieved_movie.title == movie.title
    assert retrieved_movie.director == movie.director
    assert retrieved_movie.rating == movie.rating