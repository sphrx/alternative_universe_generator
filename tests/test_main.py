import pytest
from unittest.mock import patch, mock_open, ANY
from main import load_historical_events, save_alternative_universe
from pathlib import Path

def test_load_historical_events():
    mock_json = '{"events": [{"id": "1", "title": "Test Event"}]}'
    with patch("builtins.open", mock_open(read_data=mock_json)):
        events = load_historical_events()
        assert len(events['events']) == 1
        assert events['events'][0]['title'] == "Test Event"

def test_load_historical_events_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_historical_events()

def test_save_alternative_universe():
    with patch("builtins.open", mock_open()) as mock_file:
        save_alternative_universe("Test Universe", "test_output.txt")
        mock_file.assert_called_once_with(ANY, "w")
        mock_file().write.assert_called_once_with("Test Universe")

def test_save_alternative_universe_io_error():
    with patch("builtins.open", side_effect=IOError):
        with pytest.raises(IOError):
            save_alternative_universe("Test Universe", "test_output.txt")
