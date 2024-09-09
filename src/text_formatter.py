# src/text_formatter.py

class TextFormatter:
    @staticmethod
    def format_event(event: dict, alternative: str) -> str:
        year = abs(event['year'])
        era = "н.э." if event['year'] >= 0 else "до н.э."

        formatted_text = f"{'=' * 50}\n"
        formatted_text += f"Измененное историческое событие:\n"
        formatted_text += f"{event['title']} ({year} {era})\n\n"
        formatted_text += f"Оригинальное описание:\n{event['description']}\n\n"
        formatted_text += f"Альтернативный сценарий:\n{alternative}\n"
        formatted_text += f"{'=' * 50}\n"

        return formatted_text

    @staticmethod
    def format_world_description(description: str) -> str:
        formatted_text = f"{'=' * 50}\n"
        formatted_text += "Описание альтернативной вселенной:\n\n"
        formatted_text += description
        formatted_text += f"\n{'=' * 50}\n"

        return formatted_text