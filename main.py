# main.py
from src.imports import *
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('alternative_universe.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Определение путей
DATA_DIR = Path("data")
INPUT_DIR = Path("files_input")
OUTPUT_DIR = Path("files_output")


def load_historical_events():
    try:
        with open(DATA_DIR / "historical_events.json", "r") as file:
            events = json.load(file)
        logger.info(f"Successfully loaded {len(events['events'])} historical events")
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
        logger.info(f"Alternative universe saved to {output_file}")
    except IOError:
        logger.error(f"Error writing to file {output_file}")
        raise


def main():
    logger.info("Starting alternative universe generation")

    # Убедимся, что выходная директория существует
    OUTPUT_DIR.mkdir(exist_ok=True)

    try:
        # Загрузка исторических событий
        historical_events = load_historical_events()

        event_selector = EventSelector(historical_events['events'])
        alternative_generator = AlternativeGenerator()
        world_builder = WorldBuilder()
        text_formatter = TextFormatter()

        selected_event = event_selector.select_random_event()
        logger.info(f"Selected event: {selected_event['title']}")

        alternative = alternative_generator.generate_alternative(selected_event)
        logger.info(f"Generated alternative: {alternative}")

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

        logger.info("Alternative universe generation completed successfully")
    except Exception as e:
        logger.exception(f"An error occurred during generation: {str(e)}")


if __name__ == "__main__":
    main()