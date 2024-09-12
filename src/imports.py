# src/imports.py
import os
import json
import random
import logging
from pathlib import Path
from typing import List, Dict
from faker import Faker

# Импорты ваших модулей
from src.event_selector import EventSelector
from src.alternative_generator import AlternativeGenerator
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter