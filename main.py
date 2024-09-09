# main.py
import logging
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter
from src.exceptions import EventFileNotFoundError, EventDataError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='alternative_universe.log')

logger = logging.getLogger(__name__)

def main():
    try:
        event_selector = EventSelector('data/historical_events.json')
        alternative_generator = AlternativeGenerator()
        world_builder = WorldBuilder()
        text_formatter = TextFormatter()

        all_events = event_selector.get_all_events()
        selected_event = event_selector.select_random_event()
        alternative = alternative_generator.generate_alternative(selected_event)

        world_description = world_builder.build_world_description(all_events, selected_event, alternative)

        print("Генератор альтернативных вселенных\n")
        print(text_formatter.format_event(selected_event, alternative))
        print(text_formatter.format_world_description(world_description))

        logger.info("Successfully generated alternative universe")
    except EventFileNotFoundError as e:
        logger.error(f"Event file not found: {e}")
        print("Ошибка: Файл с историческими событиями не найден.")
    except EventDataError as e:
        logger.error(f"Event data error: {e}")
        print("Ошибка: Проблема с данными исторических событий.")
    except Exception as e:
        logger.exception("An unexpected error occurred")
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()