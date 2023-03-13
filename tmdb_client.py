import requests
from flask import Flask

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTIwMmUwYTRhZDU3YmI5M2MwNzI0ZmM4YjBkYWEwMyIsInN1YiI6IjYzZmU3M2FlOWYxYmU3MDA3Y2E2MzQ1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jjodlyaFWOKrrjV4aaYrprLUmukeTttd_4gRMyUURIQ"

app = Flask(__name__)


#@app.route('/lista/')
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization" : f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization" : f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers={
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers={
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers={
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)