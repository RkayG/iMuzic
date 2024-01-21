import pytest
from unittest.mock import patch
from recommendations import get_recommendations

@pytest.mark.parametrize("seed_name", [
    "asake",  # Replace with an actual song or artist name
    "Nonexistent Seed",  # Replace with a non-existing song or artist name
    "Error Seed",  # Replace with a song or artist name that would trigger an error
    "twe twe",  # Replace with another actual song or artist name
])
def test_get_recommendations_actual_data(seed_name):
    seed_song, seed_artist, _, _, _ = get_recommendations(seed_name)

    assert seed_song is not None, f"Expected non-None value for seed_song, got None"
    assert seed_artist is not None, f"Expected non-None value for seed_artist, got None"
