"""Tests for the AlternativeGenerator class.

This module contains unit tests for the AlternativeGenerator class,
which is responsible for generating alternative scenarios for historical events.
"""

from __future__ import annotations

import pytest

from src.alternative_generator import AlternativeGenerator


@pytest.fixture()
def sample_event():
    """Fixture that provides a sample event with alternatives.

    Returns:
        dict: A dictionary representing a sample historical event with alternatives.
    """
    return {
        "id": "1",
        "title": "Test Event",
        "alternatives": ["Alternative 1", "Alternative 2", "Alternative 3"],
    }


def test_generate_alternative(sample_event):
    """Test the generation of an alternative scenario from a given event.

    This test ensures that the generated alternative is one of the
    predefined alternatives for the event.

    Args:
        sample_event (dict): A sample event fixture.
    """
    generator = AlternativeGenerator()
    alternative = generator.generate_alternative(sample_event)
    assert alternative in sample_event["alternatives"]


def test_generate_alternative_no_alternatives():
    """Test the behavior when an event has no alternatives.

    This test checks if the generator returns the default message
    when no alternatives are available for an event.
    """
    generator = AlternativeGenerator()
    event_without_alternatives = {"id": "2", "title": "No Alternatives"}
    alternative = generator.generate_alternative(event_without_alternatives)
    assert alternative == "No alternative scenario found"
