"""Module for generating consequences of alternative historical scenarios."""

from __future__ import annotations

import logging
import secrets
from typing import ClassVar

logger = logging.getLogger(__name__)


class ConsequenceEngine:
    """Engine for generating consequences of alternative historical scenarios."""

    generic_consequences: ClassVar[list[str]] = [
        "Change in the balance of power in the region",
        "Impact on technological development",
        "Formation of new cultural traditions",
        "Change in economic relations",
        "Influence on the political structure of society",
    ]

    @classmethod
    def generate_consequences(
        cls,
        event: dict[str, list[str]],
        alternative: str,
    ) -> list[str]:
        """Generate consequences for an alternative historical scenario.

        Args:
            event (Dict[str, List[str]]): The historical event with its original consequences.
            alternative (str): The alternative scenario.

        Returns:
            List[str]: A list of consequences for the alternative scenario.
        """
        short_term_consequences = event.get("consequences", [])
        long_term_consequences = event.get("modern_impact", [])

        all_consequences = (
            short_term_consequences + long_term_consequences + cls.generic_consequences
        )

        # Use the alternative to create a specific consequence
        specific_consequence = f"As a result of '{alternative}': {secrets.choice(cls.generic_consequences).lower()}"

        num_consequences = min(4, len(all_consequences))
        selected_consequences = secrets.SystemRandom().sample(
            all_consequences,
            k=num_consequences - 1,
        )
        selected_consequences.append(specific_consequence)

        logger.info(
            "Generated %d consequences for the alternative scenario",
            num_consequences,
        )
        return selected_consequences
