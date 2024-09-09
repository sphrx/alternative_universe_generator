# src/world_builder.py
from src.imports import Dict, List


class WorldBuilder:
    @staticmethod
    def build_world_description(
            event: Dict,
            alternative: str,
            consequences: List[str]
    ) -> str:
        year = "н.э." if event['year'] > 0 else "до н.э."
        abs_year = abs(event['year'])

        description = (
            f"В {abs_year} году {year} история пошла по другому пути.\n"
            f"Вместо '{event['title']}' произошло следующее:\n"
            f"{alternative}\n\n"
            f"Это привело к следующим последствиям:\n"
        )

        for consequence in consequences:
            description += f"- {consequence}\n"

        return description