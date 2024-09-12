import pytest
from src.text_formatter import TextFormatter

@pytest.fixture
def text_formatter():
    return TextFormatter()

@pytest.fixture
def sample_event():
    return {
        "id": "1",
        "title": "Test Event",
        "year": -500,
        "description": "Test Description"
    }

def test_format_event(text_formatter, sample_event):
    alternative = "Test Alternative"
    formatted_text = text_formatter.format_event(sample_event, alternative)
    assert "Test Event" in formatted_text
    assert "500 до н.э." in formatted_text
    assert "Test Description" in formatted_text
    assert "Test Alternative" in formatted_text

def test_format_world_description(text_formatter):
    description = "Test World Description"
    formatted_text = text_formatter.format_world_description(description)
    assert "Описание альтернативной вселенной:" in formatted_text
    assert "Test World Description" in formatted_text