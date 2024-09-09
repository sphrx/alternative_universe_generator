from src.imports import json, random, Dict

class EventSelector:
    def __init__(self, file_path: str):
        with open(file_path, 'r') as file:
            self.events = json.load(file)['events']

    def select_random_event(self) -> Dict:
        return random.choice(self.events)