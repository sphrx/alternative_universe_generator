import pytest
from src.world_builder import WorldBuilder

@pytest.fixture
def world_builder():
    return WorldBuilder()

@pytest.fixture
def sample_events():
    return [
        {
            "id": "1",
            "title": "Test Event",
            "consequences": ["Consequence 1", "Consequence 2"],
            "modern_impact": ["Impact 1", "Impact 2"]
        }
    ]

def test_generate_base_world(world_builder):
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
    changed_event = sample_events[0]
    alternative = "Test Alternative"
    description = world_builder.build_world_description(sample_events, changed_event, alternative)
    assert isinstance(description, str)
    assert "Доминирующей формой правления является" in description
    assert "Технологическое развитие" in description
    assert "Культура преимущественно" in description
    assert "Экономическая система основана на" in description