# src/alternative_generator.py
from typing import Dict
import random
import logging

logger = logging.getLogger(__name__)

class AlternativeGenerator:
    @staticmethod
    def generate_alternative(event: Dict) -> str:
        if not event.get('alternatives'):
            logger.warning(f"No alternatives found for event: {event['title']}")
            return "Альтернативный сценарий не найден"
        alternative = random.choice(event['alternatives'])
        logger.info(f"Generated alternative for event '{event['title']}': {alternative}")
        return alternative