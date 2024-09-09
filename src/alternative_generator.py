# src/alternative_generator.py
from src.imports import random, Dict, logging

logger = logging.getLogger(__name__)

class AlternativeGenerator:
    @staticmethod
    def generate_alternative(event: Dict) -> str:
        if not event.get('alternatives'):
            logger.warning(f"No alternatives for event: {event.get('id', 'Unknown')}")
            return "Альтернативный сценарий не найден"
        return random.choice(event['alternatives'])