import pytest
from src.alternative_generator import AlternativeGenerator

@pytest.fixture
def sample_event():
    return {
        "id": "1",
        "title": "Test Event",
        "alternatives": ["Alternative 1", "Alternative 2", "Alternative 3"]
    }

def test_generate_alternative(sample_event):
    generator = AlternativeGenerator()
    alternative = generator.generate_alternative(sample_event)
    assert alternative in sample_event['alternatives']

def test_generate_alternative_no_alternatives():
    generator = AlternativeGenerator()
    event_without_alternatives = {"id": "2", "title": "No Alternatives"}
    alternative = generator.generate_alternative(event_without_alternatives)
    assert alternative == "Альтернативный сценарий не найден"