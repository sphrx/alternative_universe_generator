# main.py
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.consequence_engine import ConsequenceEngine
from src.world_builder import WorldBuilder

def main():
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

if __name__ == "__main__":
    main()