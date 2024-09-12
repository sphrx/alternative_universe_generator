"""Module for generating alternative scenarios for historical events."""

import logging
import secrets  # Using secrets for cryptographically strong random choices

logger = logging.getLogger(__name__)


class AlternativeGenerator:
    """Class for generating alternative scenarios for historical events."""

    @staticmethod
    def generate_alternative(event: dict[str, str]) -> str:
        """Generate an alternative scenario for a given historical event.

        Args:
            event (Dict[str, str]): A dictionary representing a historical event.

        Returns:
            str: An alternative scenario for the event.
        """
        if not event.get("alternatives"):
            logger.warning("No alternatives found for event: %s", event["title"])
            return "No alternative scenario found"

        alternative = secrets.choice(event["alternatives"])
        logger.info("Generated alternative for event '%s': %s", event["title"], alternative)
        return alternative
