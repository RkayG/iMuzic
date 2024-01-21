import streamlit as st
from recommendations import get_recommendations

# Set page configuration
st.set_page_config(layout="wide")

# Page background styling
page_bg_img = f"""
<style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Define custom CSS for the button
button_style = """
    <style>
        button {
            transition: background-color 0.3s ease; /* Add smooth transition */
        }
        button:hover {
            background-color: rgba(234, 214, 217, 0.571); /* Change background color on hover */
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

st.title("iMuzic")
st.header('Spotify Music Recommendation System')

# User input
search_input = st.text_input("Search for an artist or song:")

if st.button('Get Recommendations'):
    seed_song, seed_artist, recommended_music_names, recommended_music_posters, recommended_audio_urls = get_recommendations(search_input)
    
    if seed_song and seed_artist:
        st.write(f"Recommendations based on {seed_song} by {seed_artist}:")
    else:
        st.warning(f"No results found for '{search_input}'.")

    # Display recommended music using a loop
    num_recommendations = len(recommended_music_names)
    cols_per_row = 4

    for i in range(0, num_recommendations, cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            index = i + j
            if index < num_recommendations:
                with cols[j]:
                    st.text(recommended_music_names[index])
                    st.image(recommended_music_posters[index])

                    # Get audio URL for the selected song
                    audio_url = recommended_audio_urls[index]

                    # Embed an HTML audio player
                    st.audio(audio_url, format='audio/mp3', start_time=0)

                    st.empty()  # Add horizontal space

    st.markdown("---")
