# iMuzic - Spotify Music Recommendation System

Welcome to iMuzic, a Streamlit application that leverages the Spotify API to provide music recommendations based on your favorite songs or artists. 

## Preview
![Homepage](preview_images/home_page.png)
![Recommendations](preview_images/recommendations_page.png)

## App Structure

1. **recommendations.py:**
    - Contains the core functionality for fetching music recommendations using the Spotify API based on a seed song or artist. It leverages Spotify's content-based and collaborative filtering algorithms for recommendations.

2. **requirements.txt:**
    - Lists the required Python packages. Install them using `pip install -r requirements.txt`.

3. **tests/test_recommendations.py:**
    - Contains unit tests for the `get_recommendations` function. Use `pytest` to run the tests.

4. **app.py:**
    - The main application file that uses Streamlit to create a user interface.
    - Applies custom styling, sets up the page, and integrates the recommendation functionality.

5. **config.ini:**
    - Configuration file to store Spotify API credentials. This was not added to GitHub. 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RkayG/iMuzic.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.ini` file in the root directory and add Replace `"your_client_id"` and `"your_client_secret"` with your actual Spotify API credentials:
    ```ini
    [SPOTIPY]
    CLIENT_ID = "your_client_id"
    CLIENT_SECRET = "your_client_secret"
    ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Visit http://localhost:8501 in your browser to interact with the app.


