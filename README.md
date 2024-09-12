# Alternative Universe Generator

This project is a Python application that generates alternative historical scenarios based on key events in world history.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12 or higher
- Poetry (for dependency management)
- Docker (optional, for containerized usage)

## Installation

To install the Alternative Universe Generator, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/alternative-universe-generator.git
cd alternative_universe_generator
```

2. Initialize configuration files:

```
make init-configs
```

This command will create a `.env` file from `.env.example` and a `compose.override.yaml` file from `compose.override.dev.yaml`.


3. Initialize the development environment:

```
make init-dev
```

This command will install all necessary dependencies, set up pre-commit hooks, and perform any other required initialization steps.

## Usage

To run the application:

```
make run
```

This will generate an alternative historical scenario and output it to the console.

## Development

For development purposes, you can use the following commands:

- Format the code:

```
make format
```

- Run the linter:

```
- make lint
```

- Clean temporary files:
-
```
make clean
```

## Testing

To run the tests:
```
make test
```

## Docker

The application can be run in a Docker container. Here are the available Docker-related commands:

- Build the Docker image:

```
make docker-build
```

- Run the application in a Docker container:

```
make docker-run
```

- Start the application using Docker Compose:

```
make docker-up
```

- Stop the Docker Compose services:

```
make docker-down
```

- Remove all Docker-related resources (volumes, images, orphaned containers):

```
make docker-purge

```

These commands provide a full lifecycle management for Docker-based deployment of the application.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request.

Before submitting a pull request, please ensure that your code passes all tests and linting checks:

```
make pre-commit-run-all
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
