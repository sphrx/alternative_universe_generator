import random
from typing import Dict, List

class AlternativeGenerator:
    @staticmethod
    def generate_alternative(event: Dict) -> str:
        return random.choice(event['alternatives'])