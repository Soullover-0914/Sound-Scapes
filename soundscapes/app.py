from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

API_KEY = "87ae95dcab0da113f7803a3b93b8a7d8"
API_URL = "http://ws.audioscrobbler.com/2.0/"

def get_top_tracks():
    params = {
        "method": "chart.gettoptracks",
        "api_key": API_KEY,
        "format": "json"
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        tracks = data["tracks"]["track"]
        return [{"title": track["name"], "artist": track["artist"]["name"]} for track in tracks]
    return []

@app.route('/top-songs', methods=['GET'])
def top_songs():
    return jsonify({"top_songs": get_top_tracks()})

if __name__ == '__main__':
    app.run(debug=True)
