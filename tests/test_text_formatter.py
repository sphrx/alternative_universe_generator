"""Tests for the TextFormatter class.

This module contains unit tests for the TextFormatter class,
which is responsible for formatting event and world descriptions.
"""

from __future__ import annotations

import pytest

from src.text_formatter import TextFormatter


@pytest.fixture()
def text_formatter():
    """Fixture that provides an instance of TextFormatter.

    Returns:
        TextFormatter: An instance of the TextFormatter class.
    """
    return TextFormatter()


@pytest.fixture()
def sample_event():
    """Fixture that provides a sample historical event.

    Returns:
        dict: A dictionary representing a sample historical event.
    """
    return {
        "id": "1",
        "title": "Test Event",
        "year": -500,
        "description": "Test Description",
    }


def test_format_event(text_formatter, sample_event):
    """Test the formatting of an event.

    This test ensures that the event formatting includes all necessary
    information and is properly formatted.

    Args:
        text_formatter (TextFormatter): An instance of TextFormatter.
        sample_event (dict): A sample event fixture.
    """
    alternative = "Test Alternative"
    formatted_text = text_formatter.format_event(sample_event, alternative)
    assert "Test Event" in formatted_text
    assert "500 BCE" in formatted_text  # Changed from "до н.э." to "BCE"
    assert "Test Description" in formatted_text
    assert "Test Alternative" in formatted_text


def test_format_world_description(text_formatter):
    """Test the formatting of a world description.

    This test checks if the world description is properly formatted
    and includes the necessary introductory text.

    Args:
        text_formatter (TextFormatter): An instance of TextFormatter.
    """
    description = "Test World Description"
    formatted_text = text_formatter.format_world_description(description)
    assert (
        "Description of the alternative universe:" in formatted_text
    )  # Translated from Russian
    assert "Test World Description" in formatted_text
