# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_create_movie():
    movie_repository.clear_db()
    movie = movie_repository.create_movie('Star Wars', 'George Lucas', '5')
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == '5'
    assert movie_repository.get_movie_by_id(movie.movie_id)
    movie_repository.clear_db()