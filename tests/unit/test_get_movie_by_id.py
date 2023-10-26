from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    repo = get_movie_repository()

    #populate repo
    testmov1 = Movie(1, 'test title 1', 'test dir 1', 8)
    testmov2 = Movie(2, 'test title 2', 'test dir 2', 4)
    repo._db = {1: testmov1, 2: testmov2}

    #get real movie
    movie = repo.get_movie_by_id(1)
    assert movie == testmov1
    #get fake movie
    movie = repo.get_movie_by_id(3)
    assert movie is None