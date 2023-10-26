# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository
import pytest
from pytest_flask import client
from app import app

movie_repository = get_movie_repository()

def test_app():
    return app

def test_get_single_movie_id(test_app,client):
    movie = movie_repository.create_movie("test title","test dir",4)
    response = client.get(f'/movies/{movie.id}')
    
    assert response.status_code == 200
    
    assert movie.title.encode() in response.data
    
    assert movie.director.encode() in response.data
    
    assert str(movie.rating).encode() in response.data

def test_get_movie_not_exist(test_app,client):
    response = client.get('/movies/999')
    assert response.status_code == 404
    assert "Movie not found".encode() in response.data

    