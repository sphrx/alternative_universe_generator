from src.imports import random, List, Dict

class EventSelector:
    def __init__(self, events: List[Dict]):
        self.events = events

    def select_random_event(self) -> Dict:
        if not self.events:
            raise ValueError("No events available to select from")
        return random.choice(self.events)

    def get_all_events(self) -> List[Dict]:
        return self.events