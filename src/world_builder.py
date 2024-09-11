from src.imports import Dict, List, random


class WorldBuilder:
    def __init__(self):
        self.power_structures = ["империя", "федерация", "конфедерация", "республика", "теократия",
                                 "анархическое общество"]
        self.technological_levels = ["отстает от нашей реальности на столетия",
                                     "примерно соответствует нашей реальности", "значительно опережает нашу реальность",
                                     "развивается по совершенно иному пути"]
        self.cultural_paradigms = ["индивидуалистическая", "коллективистская", "технократическая", "экологическая",
                                   "духовная"]
        self.economic_systems = {
            "капитализм": "капитализме",
            "социализм": "социализме",
            "смешанная экономика": "смешанной экономике",
            "постдефицитная экономика": "постдефицитной экономике",
            "феодализм": "феодализме"
        }

    def build_world_description(self, events: List[Dict], changed_event: Dict, alternative: str) -> str:
        world = self._generate_base_world()
        for event in events:
            if event['id'] == changed_event['id']:
                self._apply_alternative_impact(world, changed_event, alternative)
            else:
                self._apply_normal_impact(world, event)

        return self._format_world_description(world)

    def _generate_base_world(self) -> Dict:
        return {
            "dominant_power": random.choice(self.power_structures),
            "tech_level": random.choice(self.technological_levels),
            "culture": random.choice(self.cultural_paradigms),
            "economy": random.choice(list(self.economic_systems.keys())),
            "key_differences": []
        }

    def _apply_alternative_impact(self, world: Dict, event: Dict, alternative: str):
        impact = random.choice(event['modern_impact'])
        world['key_differences'].append(f"Из-за изменения в событии '{event['title']}': {impact}")

        if "религия" in alternative.lower():
            world['culture'] = "духовная"
        elif "технология" in alternative.lower():
            world['tech_level'] = random.choice(self.technological_levels[1:])
        elif "империя" in alternative.lower() or "государство" in alternative.lower():
            world['dominant_power'] = random.choice(self.power_structures[:3])

    def _apply_normal_impact(self, world: Dict, event: Dict):
        if random.random() < 0.3:  # 30% шанс
            impact = random.choice(event['consequences'])
            world['key_differences'].append(f"Влияние события '{event['title']}': {impact}")

    def _format_world_description(self, world: Dict) -> str:
        description = ""
        description += f"Доминирующей формой правления является {world['dominant_power']}.\n"
        description += f"Технологическое развитие {world['tech_level']}.\n"
        description += f"Культура преимущественно {world['culture']}.\n"
        description += f"Экономическая система основана на {self.economic_systems[world['economy']]}.\n\n"
        description += "Ключевые отличия от нашей реальности:\n"
        for diff in world['key_differences']:
            description += f"- {diff}\n"
        return description