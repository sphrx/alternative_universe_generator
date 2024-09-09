# src/consequence_engine.py
from src.imports import Dict, List, random, logging

logger = logging.getLogger(__name__)

class ConsequenceEngine:
    @staticmethod
    def generate_consequences(event: Dict, alternative: str) -> List[str]:
        all_consequences = event.get('consequences', []) + [
            "Изменение баланса сил в регионе",
            "Влияние на развитие технологий",
            "Формирование новых культурных традиций"
        ]
        num_consequences = min(3, len(all_consequences))
        logger.info(f"Generating {num_consequences} consequences for event {event.get('id', 'Unknown')}")
        return random.sample(all_consequences, k=num_consequences)