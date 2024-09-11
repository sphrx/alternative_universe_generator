# src/alternative_generator.py
from src.imports import random, Dict

class AlternativeGenerator:
    @staticmethod
    def generate_alternative(event: Dict) -> str:
        if not event.get('alternatives'):
            return "Альтернативный сценарий не найден"
        return random.choice(event['alternatives'])