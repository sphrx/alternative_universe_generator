"""Module for selecting historical events."""

from __future__ import annotations

import logging
import secrets
from typing import Any

logger = logging.getLogger(__name__)


class EventSelector:
    """Class for selecting historical events."""

    def __init__(self, events: list[dict[str, Any]]):
        """Initialize the EventSelector with a list of events.

        Args:
            events (List[Dict[str, Any]]): List of historical events.
        """
        self.events = events
        logger.info("EventSelector initialized with %d events", len(events))

    def select_random_event(self) -> dict[str, Any]:
        """Select a random event from the list of events.

        Returns:
            Dict[str, Any]: A randomly selected event.

        Raises:
            ValueError: If there are no events to select from.
        """
        if not self.events:
            logger.error("No events available to select from")
            raise ValueError("No events available to select from")

        selected_event = secrets.choice(self.events)
        logger.info("Selected event: %s", selected_event["title"])
        return selected_event

    def get_all_events(self) -> list[dict[str, Any]]:
        """Get all events.

        Returns:
            List[Dict[str, Any]]: All available events.
        """
        return self.events
