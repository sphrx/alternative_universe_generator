import random
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class EventSelector:
    def __init__(self, events: List[Dict]):
        self.events = events
        logger.info(f"EventSelector initialized with {len(events)} events")

    def select_random_event(self) -> Dict:
        if not self.events:
            logger.error("No events available to select from")
            raise ValueError("No events available to select from")
        selected_event = random.choice(self.events)
        logger.info(f"Selected event: {selected_event['title']}")
        return selected_event

    def get_all_events(self) -> List[Dict]:
        return self.events
