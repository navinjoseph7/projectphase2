import pytest
from lib.trackmusic import*

def test_trackmusic():
    trackmusic = TrackMusic()
    trackmusic.add_music("Waka Waka")
    assert trackmusic.display_list() == ["Waka Waka"]

def test_trackmusic_empty_list():
    trackmusic = TrackMusic()
    with pytest.raises(Exception) as e: # <-- New code
        trackmusic.display_list()
    error_message = str(e.value) # <-- New code
    assert error_message == "No tracks listened"