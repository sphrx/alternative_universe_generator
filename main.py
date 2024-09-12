# main.py
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
        logging.StreamHandler()
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


def main():
    try:
        # Загрузка исторических событий
        historical_events = load_historical_events()

        event_selector = EventSelector(historical_events['events'])
        alternative_generator = AlternativeGenerator()
        world_builder = WorldBuilder()
        text_formatter = TextFormatter()

        selected_event = event_selector.select_random_event()
        alternative = alternative_generator.generate_alternative(selected_event)
        world_description = world_builder.build_world_description(historical_events['events'], selected_event,
                                                                  alternative)

        formatted_output = text_formatter.format_event(selected_event, alternative)
        formatted_output += "\n\n" + text_formatter.format_world_description(world_description)

        # Генерация уникального имени файла
        output_filename = f"alternative_universe_{selected_event['id']}.txt"

        # Сохранение результата
        save_alternative_universe(formatted_output, output_filename)

        # Вывод результата в консоль
        print(formatted_output)

        # Логирование процесса генерации
        log_generation_process(len(historical_events['events']), selected_event, alternative)

    except Exception as e:
        logger.exception(f"An error occurred during generation: {str(e)}")


if __name__ == "__main__":
    main()