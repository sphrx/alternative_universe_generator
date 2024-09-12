"""Tests for the main module of the Alternative Universe Generator.

This module contains unit tests for the core functions of the main script,
including loading historical events and saving generated universes.
"""

from __future__ import annotations

from unittest.mock import ANY
from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from main import load_historical_events
from main import save_alternative_universe


def test_load_historical_events():
    """Test the successful loading of historical events from a JSON file.

    This test mocks the file open operation and checks if the events
    are correctly parsed from the JSON data.
    """
    mock_json = '{"events": [{"id": "1", "title": "Test Event"}]}'
    with patch("builtins.open", mock_open(read_data=mock_json)):
        events = load_historical_events()
        assert len(events["events"]) == 1
        assert events["events"][0]["title"] == "Test Event"


def test_load_historical_events_file_not_found():
    """Test the behavior when the historical events file is not found.

    This test ensures that a FileNotFoundError is raised when the
    events file doesn't exist.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_historical_events()


def test_save_alternative_universe():
    """Test the saving of an alternative universe description to a file.

    This test mocks the file open operation and checks if the content
    is correctly written to the file.
    """
    with patch("builtins.open", mock_open()) as mock_file:
        save_alternative_universe("Test Universe", "test_output.txt")
        mock_file.assert_called_once_with(ANY, "w")
        mock_file().write.assert_called_once_with("Test Universe")


def test_save_alternative_universe_io_error():
    """Test the behavior when an IO error occurs during saving.

    This test ensures that an IOError is raised when there's an issue
    with writing to the file.
    """
    with patch("builtins.open", side_effect=IOError):
        with pytest.raises(IOError):
            save_alternative_universe("Test Universe", "test_output.txt")
