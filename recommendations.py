import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

# Spotify API credentials
CLIENT_ID = "c18a4ee6c6a34de6941e5ccb6f6cdf5d"
CLIENT_SECRET = "a77a3b4d50d3400987b9403176322ed1"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@st.cache_data()
def get_recommendations(seed_name):
    try:
        # Convert search input to lowercase
        seed_name_lower = seed_name.lower()

        # Search for the seed song or artist
        results = sp.search(q=seed_name_lower, type="track,artist", limit=1)

        if results and results["tracks"]["items"]:
            seed_artist = results["tracks"]["items"][0]["artists"][0]["name"]
            seed_song = results["tracks"]["items"][0]["name"]

            # Get recommendations based on the seed artist or song
            recommendations = sp.recommendations(seed_tracks=[results["tracks"]["items"][0]["id"]], limit=8)

            recommended_music_names = []
            recommended_music_posters = []
            recommended_audio_urls = []

            for track in recommendations["tracks"]:
                name = track["name"]
                poster_url = track["album"]["images"][0]["url"]
                audio_url = track["preview_url"]

                # Check if both poster_url and audio_url are available
                if poster_url and audio_url:
                    recommended_music_names.append(name)
                    recommended_music_posters.append(poster_url)
                    recommended_audio_urls.append(audio_url)

            return seed_song, seed_artist, recommended_music_names, recommended_music_posters, recommended_audio_urls
    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")
        return None, None, [], [], []