import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_recommendations(emotion):
    # Setup Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Fetch playlists matching the emotion
    playlists = sp.search(q=emotion, type='playlist', limit=10)['playlists']['items']
    tracks = []
    
    if playlists:
        # Extract track information from the first playlist
        playlist_tracks = sp.playlist_items(playlists[0]['id'], additional_types=('track',))['items']
        tracks = [{"track": track['track']['name'], "artist": track['track']['artists'][0]['name']} for track in playlist_tracks]
    
    return tracks
