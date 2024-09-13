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
```
```
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
make lint
```
- Clean temporary files:
```
make clean
```
## Testing

To run the tests:
```
make test
```

## Docker

The application can be run using Docker Compose, which simplifies the process of building and running the containerized application. Here are the available Docker Compose commands:

- Build and start the application:
```
make docker-up
```
This command builds the Docker image if it doesn't exist and starts the container.

- Stop the application:
```
- make docker-down
```
This stops and removes the containers defined in the Docker Compose file.

- Rebuild and restart the application:
```
- make docker-rebuild
```
Use this when you've made changes to the application and need to rebuild the Docker image.

- View logs of the running application:
```
- make docker-logs
```
This shows the logs from the running container.

- Remove all Docker-related resources:
```
- make docker-purge
```
This removes containers, volumes, and images created by Docker Compose for this project.

These commands provide full lifecycle management for Docker-based deployment of the application using Docker Compose.

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

