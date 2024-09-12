"""Tests for the WorldBuilder class.

This module contains unit tests for the WorldBuilder class,
which is responsible for generating descriptions of alternative worlds.
"""

from __future__ import annotations

import pytest

from src.world_builder import WorldBuilder


@pytest.fixture()
def world_builder():
    """Fixture that provides an instance of WorldBuilder.

    Returns:
        WorldBuilder: An instance of the WorldBuilder class.
    """
    return WorldBuilder()


@pytest.fixture()
def sample_events():
    """Fixture that provides a sample list of events.

    Returns:
        list: A list containing a sample historical event.
    """
    return [
        {
            "id": "1",
            "title": "Test Event",
            "consequences": ["Consequence 1", "Consequence 2"],
            "modern_impact": ["Impact 1", "Impact 2"],
        },
    ]


def test_generate_base_world(world_builder):
    """Test the generation of a base world.

    This test ensures that the generated base world contains all
    necessary attributes.

    Args:
        world_builder (WorldBuilder): An instance of WorldBuilder.
    """
    world = world_builder._generate_base_world()
    assert "dominant_power" in world
    assert "tech_level" in world
    assert "culture" in world
    assert "economy" in world
    assert "key_differences" in world
    assert "notable_figures" in world
    assert "major_cities" in world
    assert "dominant_religion" in world


def test_build_world_description(world_builder, sample_events):
    """Test the building of a world description.

    This test checks if the built world description contains all
    necessary elements and is properly formatted.

    Args:
        world_builder (WorldBuilder): An instance of WorldBuilder.
        sample_events (list): A list of sample events.
    """
    changed_event = sample_events[0]
    alternative = "Test Alternative"
    description = world_builder.build_world_description(
        sample_events,
        changed_event,
        alternative,
    )
    assert isinstance(description, str)
    assert "The dominant form of government is" in description
    assert "Technological development" in description
    assert "The culture is predominantly" in description
    assert "The economic system is based on" in description
