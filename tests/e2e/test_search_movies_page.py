# TODO: Feature 3
from app import app

def test_search(test_app):
    response = test_app.post('/movies/search', data={'title': 'Title'}, follow_redirects=True)
    response = test_app.get('/movies/search')
    result = response.data.decode()
    assert response.status_code == 200
    assert 'title' in result

def test_search_no_movie(test_app):
    response = test_app.post('/movies/search', data={'title': 'NotTitle'}, follow_redirects=True)
    response = test_app.get('/movies/search')
    result = response.data.decode()
    assert response.status_code == 200
    assert not('Title' in result)

def test_search_empty(test_app):
    response = test_app.post('/movies/search', data={'title': ''}, follow_redirects=True)
    response = test_app.get('/movies/search')
    result = response.data.decode()
    assert response.status_code == 200
    assert '' in result 