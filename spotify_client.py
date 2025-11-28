# spotify_client.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def create_spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id="145741a473f94b4b984a662db6994738",
            client_secret="e4fe91c199544d048b023aa7e52da7fc"
        )
    )
