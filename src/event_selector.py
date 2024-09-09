# src/event_selector.py
from src.imports import json, random, Dict, List, Path, logging
from src.exceptions import EventFileNotFoundError, EventDataError

logger = logging.getLogger(__name__)


class EventSelector:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.events = self._load_events()

    def _load_events(self) -> List[Dict]:
        try:
            if not self.file_path.exists():
                raise EventFileNotFoundError(f"File not found: {self.file_path}")

            with open(self.file_path, 'r') as file:
                data = json.load(file)

            if 'events' not in data or not isinstance(data['events'], list):
                raise EventDataError("Invalid event data structure")

            return data['events']
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            raise EventDataError("Invalid JSON in event file") from e

    def select_random_event(self) -> Dict:
        if not self.events:
            logger.warning("No events available to select from")
            raise EventDataError("No events available")
        return random.choice(self.events)

    def get_all_events(self) -> List[Dict]:
        return self.events