# Alternative Universe Generator

## Description
The Alternative Universe Generator is a Python-based application that creates fascinating "what-if" scenarios by altering key historical events. It generates descriptions of alternative universes based on changed historical outcomes, providing users with intriguing glimpses into possible alternate realities.

## Features
- Random selection of historical events from a curated database
- Generation of alternative scenarios for selected events
- Creation of comprehensive alternative universe descriptions
- Consideration of short-term and long-term consequences of historical changes
- Logging of generated scenarios for future reference

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/alternative-universe-generator.git
```

2. Navigate to the project directory:

```
cd alternative-universe-generator
```

3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the main script to generate an alternative universe:
```
python main.py
```

The program will output:
1. The changed historical event
2. An alternative scenario
3. A description of the resulting alternative universe

## Project Structure

- `main.py`: The entry point of the application
- `src/`:
  - `event_selector.py`: Handles the selection of historical events
  - `alternative_generator.py`: Generates alternative scenarios
  - `world_builder.py`: Creates descriptions of alternative universes
  - `consequence_engine.py`: Generates consequences of historical changes
  - `text_formatter.py`: Formats the output text
  - `exceptions.py`: Custom exception classes
- `data/`:
  - `historical_events.json`: Database of historical events

## Contributing

Contributions to the Alternative Universe Generator are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all the history enthusiasts and alternate history writers who inspire projects like this.
- Special thanks to the Python community for providing the tools and libraries that make this project possible.