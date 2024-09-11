# main.py
from src.imports import *

# Определение путей
DATA_DIR = Path("data")
INPUT_DIR = Path("files_input")
OUTPUT_DIR = Path("files_output")


def load_historical_events():
    with open(DATA_DIR / "historical_events.json", "r") as file:
        return json.load(file)


def save_alternative_universe(universe_description, filename):
    output_file = OUTPUT_DIR / filename
    with open(output_file, "w") as file:
        file.write(universe_description)
    print(f"Alternative universe saved to {output_file}")


def main():
    # Убедимся, что выходная директория существует
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Загрузка исторических событий
    historical_events = load_historical_events()

    event_selector = EventSelector(historical_events['events'])
    alternative_generator = AlternativeGenerator()
    world_builder = WorldBuilder()
    text_formatter = TextFormatter()

    selected_event = event_selector.select_random_event()
    alternative = alternative_generator.generate_alternative(selected_event)
    world_description = world_builder.build_world_description(historical_events['events'], selected_event, alternative)

    formatted_output = text_formatter.format_event(selected_event, alternative)
    formatted_output += "\n\n" + text_formatter.format_world_description(world_description)

    # Генерация уникального имени файла
    output_filename = f"alternative_universe_{selected_event['id']}.txt"

    # Сохранение результата
    save_alternative_universe(formatted_output, output_filename)

    # Вывод результата в консоль
    print(formatted_output)


if __name__ == "__main__":
    main()