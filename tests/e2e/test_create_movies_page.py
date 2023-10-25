# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_create_movie(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': 'Star Wars',
        'director': 'George Lucas',
        'rating': '5'
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert 'Star Wars</td>' in data
    assert 'George Lucas</td>' in data
    assert '5</td>' in data
    movie_repository.clear_db()


def test_create_todo_bad_request(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={}, follow_redirects=True)
    assert response.status_code == 400

def test_empty_title(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': '',
        'director': 'George Lucas',
        'rating': '5'
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 400

def test_empty_director(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': 'Star Wars',
        'director': '',
        'rating': '5'
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 400

def test_empty_rating(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': 'Star Wars',
        'director': 'George Lucas',
        'rating': ''
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 400

def test_rating_range(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': 'Star Wars',
        'director': 'George Lucas',
        'rating': '0'
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 400

def test_invalid_rating(test_app: FlaskClient) -> None:
    response = test_app.post('/movies', data={
        'title': 'Star Wars',
        'director': 'George Lucas',
        'rating': 'l'
    }, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 400