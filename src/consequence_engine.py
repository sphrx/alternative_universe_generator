# src/consequence_engine.py
from src.imports import Dict, List, random, logging

logger = logging.getLogger(__name__)


class ConsequenceEngine:
    @staticmethod
    def generate_consequences(event: Dict, alternative: str) -> List[str]:
        short_term_consequences = event.get('consequences', [])
        long_term_consequences = event.get('modern_impact', [])

        generic_consequences = [
            "Изменение баланса сил в регионе",
            "Влияние на развитие технологий",
            "Формирование новых культурных традиций",
            "Изменение экономических отношений",
            "Влияние на политическую структуру общества"
        ]

        all_consequences = short_term_consequences + long_term_consequences + generic_consequences

        # Используем альтернативу для создания специфического последствия
        specific_consequence = f"В результате '{alternative}': " + random.choice(generic_consequences).lower()

        num_consequences = min(4, len(all_consequences))
        selected_consequences = random.sample(all_consequences, k=num_consequences - 1)
        selected_consequences.append(specific_consequence)

        logger.info(f"Generated {num_consequences} consequences for event {event.get('id', 'Unknown')}")
        return selected_consequences