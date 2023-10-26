import pytest
from flask import Flask
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_get_single_movie_exists(client):
    movie_repository = get_movie_repository()
    movie = movie_repository.create_movie("test title","test dir",5)

    response = client.get(f'/movies/{movie.id}')
    assert response.status_code == 200
    assert movie.title.encode() in response.data
    assert movie.director.encode() in response.data
    assert str(movie.rating).encode() in response.data


def test_get_movie_not_exist(client):
    response = client.get('movies/900')
    assert response.status_code == 404
    assert "Movie not found".encode() in response.data
