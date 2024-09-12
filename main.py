from src.imports import *
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter

# Определение путей
DATA_DIR = Path("data")
INPUT_DIR = Path("files_input")
OUTPUT_DIR = Path("files_output")
LOG_DIR = Path("logs")

# Настройка логирования
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / 'alternative_universe.log'),
    ]
)

logger = logging.getLogger(__name__)


def load_historical_events():
    try:
        with open(DATA_DIR / "historical_events.json", "r") as file:
            events = json.load(file)
        return events
    except FileNotFoundError:
        logger.error("Historical events file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Error decoding JSON from historical events file")
        raise


def save_alternative_universe(universe_description, filename):
    output_file = OUTPUT_DIR / filename
    try:
        with open(output_file, "w") as file:
            file.write(universe_description)
    except IOError:
        logger.error(f"Error writing to file {output_file}")
        raise


def log_generation_process(events_count, selected_event, alternative):
    logger.info("Starting alternative universe generation")
    logger.info(f"Successfully loaded {events_count} historical events")
    logger.info(f"Selected event: {selected_event['title']}")
    logger.info(f"Generated alternative: {alternative}")
    logger.info("Alternative universe generation completed successfully")
    print("Log updated: see 'logs/alternative_universe.log' for details")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate alternative universes based on historical events.")
    parser.add_argument("--event", type=str, help="Specify a particular event ID to use")
    parser.add_argument("--output", type=str, default="console", choices=["console", "file", "both"],
                        help="Specify where to output the result (default: console)")
    parser.add_argument("--seed", type=int, help="Set a random seed for reproducible results")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.seed is not None:
        random.seed(args.seed)
        Faker.seed(args.seed)

    try:
        historical_events = load_historical_events()

        event_selector = EventSelector(historical_events['events'])
        alternative_generator = AlternativeGenerator()
        world_builder = WorldBuilder()
        text_formatter = TextFormatter()

        if args.event:
            selected_event = next((event for event in historical_events['events'] if event['id'] == args.event), None)
            if not selected_event:
                raise ValueError(f"Event with ID {args.event} not found")
        else:
            selected_event = event_selector.select_random_event()

        alternative = alternative_generator.generate_alternative(selected_event)
        world_description = world_builder.build_world_description(historical_events['events'], selected_event,
                                                                  alternative)

        formatted_output = text_formatter.format_event(selected_event, alternative)
        formatted_output += "\n\n" + text_formatter.format_world_description(world_description)

        output_filename = f"alternative_universe_{selected_event['id']}.txt"

        if args.output in ["file", "both"]:
            save_alternative_universe(formatted_output, output_filename)

        if args.output in ["console", "both"]:
            print(formatted_output)

        log_generation_process(len(historical_events['events']), selected_event, alternative)

    except Exception as e:
        logger.exception(f"An error occurred during generation: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()