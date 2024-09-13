"""Main module for the Alternative Universe Generator."""

from __future__ import annotations

import argparse
import json
import logging
import random
from typing import Any
from pathlib import Path

from dotenv import load_dotenv
from faker import Faker

from src.alternative_generator import AlternativeGenerator
from src.event_selector import EventSelector
from src.text_formatter import TextFormatter
from src.world_builder import WorldBuilder

load_dotenv()

# Define paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = BASE_DIR / "files_input"
OUTPUT_DIR = BASE_DIR / "files_output"
LOG_DIR = BASE_DIR / "logs"

# Setup logging
LOG_DIR.mkdir(exist_ok=True)
log_file = LOG_DIR / "alternative_universe.log"
try:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
        ],
    )
except PermissionError:
    print(f"Warning: Unable to write to log file {log_file}. Logging to console only.")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )

logger = logging.getLogger(__name__)


def load_historical_events() -> dict[str, list[dict[str, Any]]]:
    """Load historical events from JSON file."""
    try:
        with open(DATA_DIR / "historical_events.json") as file:
            events = json.load(file)
    except FileNotFoundError:
        logger.exception("Historical events file not found")
        raise
    except json.JSONDecodeError:
        logger.exception("Error decoding JSON from historical events file")
        raise
    else:
        return events


def save_alternative_universe(universe_description: str, filename: str) -> None:
    """Save the generated alternative universe to a file."""
    output_file = OUTPUT_DIR / filename
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(universe_description)
        logger.info(f"Alternative universe saved to {output_file}")
    except IOError as e:
        logger.error(f"Error writing to file {output_file}: {e}")
        print(
            f"Error: Could not save output to {output_file}. Check permissions and try again."
        )


def log_generation_process(
    events_count: int,
    selected_event: dict[str, Any],
    alternative: str,
) -> None:
    """Log the alternative universe generation process."""
    logger.info("Starting alternative universe generation")
    logger.info(f"Successfully loaded {events_count} historical events")
    logger.info(f"Selected event: {selected_event['title']}")
    logger.info(f"Generated alternative: {alternative}")
    logger.info("Alternative universe generation completed successfully")
    print("Log updated: see 'logs/alternative_universe.log' for details")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate alternative universes based on historical events.",
    )
    parser.add_argument(
        "--event",
        type=str,
        help="Specify a particular event ID to use",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="console",
        choices=["console", "file", "both"],
        help="Specify where to output the result (default: console)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Set a random seed for reproducible results",
    )
    return parser.parse_args()


def main() -> None:
    """Main function to run the Alternative Universe Generator."""
    args = parse_arguments()

    if args.seed is not None:
        random.seed(args.seed)
        Faker.seed(args.seed)

    try:
        historical_events = load_historical_events()

        event_selector = EventSelector(historical_events["events"])
        alternative_generator = AlternativeGenerator()
        world_builder = WorldBuilder()
        text_formatter = TextFormatter()

        if args.event:
            selected_event = next(
                (
                    event
                    for event in historical_events["events"]
                    if event["id"] == args.event
                ),
                None,
            )
            if not selected_event:
                raise ValueError(f"Event with ID {args.event} not found")
        else:
            selected_event = event_selector.select_random_event()

        alternative = alternative_generator.generate_alternative(selected_event)
        world_description = world_builder.build_world_description(
            historical_events["events"], selected_event, alternative
        )

        formatted_output = text_formatter.format_event(selected_event, alternative)
        formatted_output += "\n\n" + text_formatter.format_world_description(
            world_description
        )

        output_filename = f"alternative_universe_{selected_event['id']}.txt"

        # Always save the output to a file
        save_alternative_universe(formatted_output, output_filename)

        if args.output in ["console", "both"]:
            print(formatted_output)

        log_generation_process(
            len(historical_events["events"]), selected_event, alternative
        )

    except Exception as e:
        logger.exception(f"An error occurred during generation: {str(e)}")
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
