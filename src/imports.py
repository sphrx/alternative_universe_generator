# src/imports.py
import os
import json
import random
from faker import Faker
from pathlib import Path
from typing import List, Dict

# Импорты ваших модулей
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter