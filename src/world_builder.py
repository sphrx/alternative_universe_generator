"""Module for building alternative world descriptions."""

from __future__ import annotations

import logging
import secrets

from faker import Faker

logger = logging.getLogger(__name__)


class WorldBuilder:
    """Class for building alternative world descriptions."""

    def __init__(self):
        """Initialize the WorldBuilder with predefined world characteristics."""
        self.faker = Faker()
        self.power_structures = [
            "empire",
            "federation",
            "confederation",
            "republic",
            "theocracy",
            "anarchist society",
        ]
        self.technological_levels = [
            "centuries behind our reality",
            "roughly equivalent to our reality",
            "significantly ahead of our reality",
            "developing along a completely different path",
        ]
        self.cultural_paradigms = [
            "individualistic",
            "collectivist",
            "technocratic",
            "ecological",
            "spiritual",
        ]
        self.economic_systems = {
            "capitalism": "capitalism",
            "socialism": "socialism",
            "mixed economy": "mixed economy",
            "post-scarcity economy": "post-scarcity economy",
            "feudalism": "feudalism",
        }
        logger.info("WorldBuilder initialized")

    def build_world_description(
        self,
        events: list[dict],
        changed_event: dict,
        alternative: str,
    ) -> str:
        """Build a description of the alternative world.

        Args:
            events (List[Dict]): List of all historical events.
            changed_event (Dict): The event that was changed.
            alternative (str): The alternative scenario.

        Returns:
            str: A description of the alternative world.
        """
        logger.info(
            "Building world description for changed event: %s",
            changed_event["title"],
        )
        world = self._generate_base_world()
        for event in events:
            if event["id"] == changed_event["id"]:
                self._apply_alternative_impact(world, changed_event, alternative)
            else:
                self._apply_normal_impact(world, event)

        return self._format_world_description(world)

    def _generate_base_world(self) -> dict:
        """Generate a base world with random characteristics."""
        world = {
            "dominant_power": secrets.choice(self.power_structures),
            "tech_level": secrets.choice(self.technological_levels),
            "culture": secrets.choice(self.cultural_paradigms),
            "economy": secrets.choice(list(self.economic_systems.keys())),
            "key_differences": [],
            "notable_figures": [self.faker.name() for _ in range(3)],
            "major_cities": [self.faker.city() for _ in range(3)],
            "dominant_religion": self.faker.word(
                ext_word_list=[
                    "Neo-Paganism",
                    "Techno-Cult",
                    "Cosmic Pantheism",
                    "Digital Buddhism",
                    "Eco-Theism",
                ],
            ),
        }
        logger.info(
            "Generated base world: %s with %s technology",
            world["dominant_power"],
            world["tech_level"],
        )
        return world

    def _apply_alternative_impact(self, world: dict, event: dict, alternative: str):
        """Apply the impact of the alternative scenario to the world."""
        impact = secrets.choice(event["modern_impact"])
        world["key_differences"].append(
            f"Due to the change in the event '{event['title']}': {impact}",
        )
        logger.info("Applied alternative impact: %s", impact)

        if "religion" in alternative.lower():
            world["culture"] = "spiritual"
            world["dominant_religion"] = self.faker.word(
                ext_word_list=[
                    "Neo-Paganism",
                    "Techno-Cult",
                    "Cosmic Pantheism",
                    "Digital Buddhism",
                    "Eco-Theism",
                ],
            )
        elif "technology" in alternative.lower():
            world["tech_level"] = secrets.choice(self.technological_levels[1:])
        elif "empire" in alternative.lower() or "state" in alternative.lower():
            world["dominant_power"] = secrets.choice(self.power_structures[:3])

    def _apply_normal_impact(self, world: dict, event: dict):
        """Apply the impact of a normal (unchanged) event to the world."""
        if secrets.randbelow(10) < 3:  # 30% chance
            impact = secrets.choice(event["consequences"])
            world["key_differences"].append(
                f"Impact of the event '{event['title']}': {impact}",
            )
            logger.info("Applied normal impact: %s", impact)

    def _format_world_description(self, world: dict) -> str:
        """Format the world description into a readable string."""
        description = (
            f"The dominant form of government is {world['dominant_power']}.\n"
            f"Technological development is {world['tech_level']}.\n"
            f"The culture is predominantly {world['culture']}.\n"
            f"The economic system is based on {self.economic_systems[world['economy']]}.\n"
            f"The dominant religion is {world['dominant_religion']}.\n\n"
            'Major cities:\n'
        )
        description += "\n".join(f"- {city}" for city in world["major_cities"])
        description += "\n\nNotable figures:\n"
        description += "\n".join(f"- {figure}" for figure in world["notable_figures"])
        description += "\n\nKey differences from our reality:\n"
        description += "\n".join(f"- {diff}" for diff in world["key_differences"])
        logger.info("World description formatted")
        return description
