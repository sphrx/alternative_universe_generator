from src.imports import Dict, logging

logger = logging.getLogger(__name__)


class TextFormatter:
    @staticmethod
    def format_event(event: Dict, alternative: str) -> str:
        logger.info(f"Formatting event: {event['title']}")
        year = abs(event['year'])
        era = "н.э." if event['year'] >= 0 else "до н.э."

        formatted_text = f"{'=' * 50}\n"
        formatted_text += f"Измененное историческое событие:\n"
        formatted_text += f"{event['title']} ({year} {era})\n\n"
        formatted_text += f"Оригинальное описание:\n{event['description']}\n\n"
        formatted_text += f"Альтернативный сценарий:\n{alternative}\n"

        return formatted_text

    @staticmethod
    def format_world_description(description: str) -> str:
        logger.info("Formatting world description")
        formatted_text = f"{'=' * 50}\n"
        formatted_text += "Описание альтернативной вселенной:\n\n"
        formatted_text += description
        formatted_text += f"\n{'=' * 50}\n"

        return formatted_text
