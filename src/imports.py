# src/imports.py
import os
import json
import random
import logging
import argparse
from pathlib import Path
from typing import List, Dict
from faker import Faker
from dotenv import load_dotenv

# Импорты ваших модулей
from src.event_selector import EventSelector
from src.world_builder import WorldBuilder
from src.text_formatter import TextFormatter