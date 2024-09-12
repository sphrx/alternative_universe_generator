"""Tests for the EventSelector class.

This module contains unit tests for the EventSelector class,
which is responsible for selecting events from a given list.
"""

from __future__ import annotations

import pytest

from src.event_selector import EventSelector


@pytest.fixture()
def sample_events():
    """Fixture that provides a sample list of events.

    Returns:
        list: A list of dictionaries representing sample events.
    """
    return [
        {"id": "1", "title": "Event 1"},
        {"id": "2", "title": "Event 2"},
        {"id": "3", "title": "Event 3"},
    ]


def test_event_selector_initialization(sample_events):
    """Test the initialization of the EventSelector.

    This test ensures that the EventSelector is correctly initialized
    with the given list of events.

    Args:
        sample_events (list): A fixture containing sample events.
    """
    selector = EventSelector(sample_events)
    assert len(selector.events) == 3


def test_select_random_event(sample_events):
    """Test the random event selection.

    This test checks if the selected event is one of the sample events.

    Args:
        sample_events (list): A fixture containing sample events.
    """
    selector = EventSelector(sample_events)
    event = selector.select_random_event()
    assert event in sample_events


def test_empty_events_list():
    """Test the behavior when the events list is empty.

    This test ensures that a ValueError is raised when trying to select
    an event from an empty list.
    """
    selector = EventSelector([])
    with pytest.raises(ValueError):
        selector.select_random_event()


def test_get_all_events(sample_events):
    """Test the retrieval of all events.

    This test checks if the get_all_events method returns all the events
    that were used to initialize the EventSelector.

    Args:
        sample_events (list): A fixture containing sample events.
    """
    selector = EventSelector(sample_events)
    assert selector.get_all_events() == sample_events
