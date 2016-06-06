"""The python implementation of movie service server"""

import movie_service_pb2
import movie_service_resources
import threadpool
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_movie(movie_db, id):
    for movie in movie_db:
        if movie.id == id:
            return movie
    return None


class MovieServiceServicer(movie_service_pb2.BetaMovieServiceServicer):
    """Provides methods that implement functionality of movie service server"""

    def __init__(self):
        self.db = movie_service_resources.read_movie_service_database()

    def GetMovieDetails(self, request, context):
        pass

    """ Simple RPC - UNARY Call"""
    def ListAllMovies(self, request, context):
        response = movie_service_pb2.MoviesInTheaterResponse(movies=self.db)
        return response

    """ Server to Client Streaming RPC"""
    def ListAllMoviesServerStreaming(self, request, context):
        for movie in self.db:
            yield movie

    def ListMoviesClientToServerStreaming(self, request_iterator, context):
        pass

    def ListMoviesServerToClientStreaming(self, request, context):
        pass

    def ListMoviesBidirectionalStreaming(self, request_iterator, context):
        pass


def serve():
    server = movie_service_pb2.beta_create_MovieService_server(MovieServiceServicer())
    server.add_insecure_port('[::]:8980')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


def serve_with_thread_pool():
    server = movie_service_pb2.beta_create_MovieService_server(MovieServiceServicer(), ThreadPoolExecutor(100), 100)
    # server = movie_service_pb2.beta_create_MovieService_server(MovieServiceServicer())
    server.add_insecure_port('[::]:8980')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve_with_thread_pool()