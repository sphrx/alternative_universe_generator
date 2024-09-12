import pytest
from src.event_selector import EventSelector

@pytest.fixture
def sample_events():
    return [
        {"id": "1", "title": "Event 1"},
        {"id": "2", "title": "Event 2"},
        {"id": "3", "title": "Event 3"},
    ]

def test_event_selector_initialization(sample_events):
    selector = EventSelector(sample_events)
    assert len(selector.events) == 3

def test_select_random_event(sample_events):
    selector = EventSelector(sample_events)
    event = selector.select_random_event()
    assert event in sample_events

def test_empty_events_list():
    selector = EventSelector([])
    with pytest.raises(ValueError):
        selector.select_random_event()

def test_get_all_events(sample_events):
    selector = EventSelector(sample_events)
    assert selector.get_all_events() == sample_events