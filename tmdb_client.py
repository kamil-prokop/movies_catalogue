import requests
from flask import Flask

app = Flask(__name__)

#@app.route('/lista/')
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTIwMmUwYTRhZDU3YmI5M2MwNzI0ZmM4YjBkYWEwMyIsInN1YiI6IjYzZmU3M2FlOWYxYmU3MDA3Y2E2MzQ1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jjodlyaFWOKrrjV4aaYrprLUmukeTttd_4gRMyUURIQ"
    headers = {
        "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


if __name__ == "__main__":
    app.run(debug=True)