from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator

def main():
    event_selector = EventSelector('data/historical_events.json')
    alternative_generator = AlternativeGenerator()

    selected_event = event_selector.select_random_event()
    alternative = alternative_generator.generate_alternative(selected_event)

    print(
        f"Оригинальное событие: {selected_event['title']} "
        f"({selected_event['year']})"
    )
    print(f"Альтернативный сценарий: {alternative}")

if __name__ == "__main__":
    main()