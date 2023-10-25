from random import randint

from src.models.movie import Movie

_movie_repo = None

def get_movie_repository():
    global _movie_repo

    class MovieRepository:
        """In memory database which is a simple dict of movies"""

        def __init__(self) -> None:
            self._db: dict[int, Movie] = {}

        def get_all_movies(self) -> dict[int, Movie]:
            """Simply return all movies from the in-memory database"""
            return {**self._db}  # Use the splat operator to make a clone of the dict

        def get_movie_by_id(self, movie_id: int) -> Movie | None:
            """Get a single movie by its ID or None if it does not exist"""
            return self._db.get(movie_id)

        def get_movie_by_title(self, title: str) -> Movie | None:
            """Get a single movie by its title or None if it does not exist"""
            # Perform a linear search through the in-memory database
            for movie in self._db.values():
                # If the movie title matches, return the movie
                if movie.title == title:
                    return movie
            # If we made it this far, no movies matched, so return None
            return None

        def create_movie(self, title: str, director: str, rating: int) -> Movie:
            """Create a new movie and return it"""
            # Create the movie instance
            new_id = randint(0, 100_000)  # Sufficiently unique ID for our purposes
            movie = Movie(new_id, title, director, rating)
            # Save the instance in our in-memory database
            self._db[new_id] = movie
            # Return the movie instance
            return movie

        def update_movie(self, movie_id: int, title: str, director: str, rating: int) -> Movie:
            """Update a movie and return it"""
            # Get a reference to the movie in the dict
            movie = self._db.get(movie_id)
            # Complain if we did not find the movie
            if not movie:
                raise ValueError(f'movie with id {movie_id} not found')
            # Update the movie, which is the same object that is in the dict, so the changes stick
            movie.title = title
            movie.director = director
            movie.rating = rating
            return movie

        def delete_movie(self, movie_id: int) -> Movie:
            """Delete a movie and return it"""
            # Make sure the movie exists
            old_movie = self._db.get(movie_id)
            # Complain if we did not find the movie
            if not old_movie:
                raise ValueError(f'movie with id {movie_id} not found')
            # Remove the movie from the dict
            del self._db[movie_id]
            return old_movie

        def clear_db(self) -> None:
            """Clears all movies out of the database, only to be used in tests"""
            self._db = {}

    # Singleton to be used in other modules
    if _movie_repo is None:
        _movie_repo = MovieRepository()

    return _movie_repo
