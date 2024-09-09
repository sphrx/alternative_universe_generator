from src.imports import random, Dict

class AlternativeGenerator:
    @staticmethod
    def generate_alternative(event: Dict) -> str:
        return random.choice(event['alternatives'])