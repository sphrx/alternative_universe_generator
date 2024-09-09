# main.py
import logging
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.consequence_engine import ConsequenceEngine
from src.world_builder import WorldBuilder
from src.exceptions import EventFileNotFoundError, EventDataError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='alternative_universe.log')

logger = logging.getLogger(__name__)

def main():
    try:
        event_selector = EventSelector('data/historical_events.json')
        alternative_generator = AlternativeGenerator()
        consequence_engine = ConsequenceEngine()
        world_builder = WorldBuilder()

        selected_event = event_selector.select_random_event()
        alternative = alternative_generator.generate_alternative(selected_event)
        consequences = consequence_engine.generate_consequences(
            selected_event,
            alternative
        )
        world_description = world_builder.build_world_description(
            selected_event,
            alternative,
            consequences
        )

        print(world_description)
        logger.info("Successfully generated alternative universe")
    except EventFileNotFoundError as e:
        logger.error(f"Event file not found: {e}")
        print("Error: Could not find the historical events file.")
    except EventDataError as e:
        logger.error(f"Event data error: {e}")
        print("Error: There was a problem with the historical event data.")
    except Exception as e:
        logger.exception("An unexpected error occurred")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()