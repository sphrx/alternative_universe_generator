"""Module for formatting text output of the Alternative Universe Generator."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class TextFormatter:
    """Class for formatting event and world description text."""

    @staticmethod
    def format_event(event: dict[str, str], alternative: str) -> str:
        """Format the event and its alternative scenario.

        Args:
            event (Dict[str, str]): The historical event.
            alternative (str): The alternative scenario.

        Returns:
            str: Formatted text describing the event and alternative.
        """
        logger.info("Formatting event: %s", event["title"])
        year = abs(event["year"])
        era = "CE" if event["year"] >= 0 else "BCE"

        formatted_text = "=" * 50 + "\n"
        formatted_text += "Modified Historical Event:\n"
        formatted_text += f"{event['title']} ({year} {era})\n\n"
        formatted_text += f"Original Description:\n{event['description']}\n\n"
        formatted_text += f"Alternative Scenario:\n{alternative}\n"
        formatted_text += "=" * 50 + "\n"

        return formatted_text

    @staticmethod
    def format_world_description(description: str) -> str:
        """Format the description of the alternative world.

        Args:
            description (str): The description of the alternative world.

        Returns:
            str: Formatted text describing the alternative world.
        """
        logger.info("Formatting world description")
        formatted_text = "=" * 50 + "\n"
        formatted_text += "Description of the Alternative Universe:\n\n"
        formatted_text += description
        formatted_text += "\n" + "=" * 50 + "\n"

        return formatted_text
