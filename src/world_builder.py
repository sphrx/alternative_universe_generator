# src/world_builder.py
from src.imports import Dict, List, random


class WorldBuilder:
    @staticmethod
    def build_world_description(
            event: Dict,
            alternative: str,
            consequences: List[str]
    ) -> str:
        universe_number = random.randint(1, 9999)
        year = abs(event['year'])
        era = "н.э." if event['year'] > 0 else "до н.э."

        description = f"Альтернативная вселенная #{universe_number}:\n\n"
        description += f"Ключевое изменение: В {year} году {era} {alternative}\n\n"
        description += "Последствия:\n"
        for consequence in consequences:
            description += f"- {consequence}\n"

        description += f"\nСовременный мир:\n{WorldBuilder._generate_modern_world(event, alternative)}"

        return description

    @staticmethod
    def _generate_modern_world(event: Dict, alternative: str) -> str:
        # Это упрощенная версия. В реальном приложении здесь была бы более сложная логика
        dominant_powers = ["Новоперсидская империя", "Римская федерация", "Китайская глобальная держава",
                           "Индийский союз"]
        religions = ["зороастризм", "политеизм", "буддизм", "синкретическая мировая религия"]
        tech_levels = ["отстает от нашей реальности на 200-300 лет",
                       "опережает нашу реальность на несколько десятилетий", "развивается по совершенно иному пути"]

        return (f"Доминирующей мировой державой является {random.choice(dominant_powers)}. "
                f"Основные религии - {random.choice(religions)}. "
                f"Технологическое развитие {random.choice(tech_levels)} из-за изменившегося хода истории.")