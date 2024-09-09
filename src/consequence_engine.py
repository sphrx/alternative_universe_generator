from src.imports import Dict, List, random

class ConsequenceEngine:
    @staticmethod
    def generate_consequences(event: Dict, alternative: str) -> List[str]:
        # В реальном приложении здесь была бы более сложная логика
        # Сейчас мы просто выберем случайные последствия из списка
        all_consequences = event['consequences'] + [
            "Изменение баланса сил в регионе",
            "Влияние на развитие технологий",
            "Формирование новых культурных традиций"
        ]
        return random.sample(all_consequences, k=min(3, len(all_consequences)))