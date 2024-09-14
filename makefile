# Check for required tools
POETRY := $(shell command -v poetry 2> /dev/null)
DOCKER := $(shell command -v docker 2> /dev/null)

# Get user id for macOS and Linux
ifeq ($(shell uname),Darwin)
    USER_ID := $(shell id -u)
else
    USER_ID := $(shell id --user)
endif

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make check-requirements   - Check if all required tools are installed"
	@echo "  make init-configs         - Initialize configuration files"
	@echo "  make init-dev             - Initialize development environment"
	@echo "  make run                  - Run the application"
	@echo "  make test                 - Run tests"
	@echo "  make lint                 - Run linter"
	@echo "  make format               - Format code"
	@echo "  make clean                - Clean temporary files"
	@echo "  make docker-build         - Build Docker image"
	@echo "  make docker-up            - Start Docker Compose services"
	@echo "  make docker-down          - Stop Docker Compose services"
	@echo "  make docker-purge         - Remove all Docker resources"

.PHONY: check-requirements
check-requirements:
	@echo "Checking required tools..."
	@if [ -z "$(POETRY)" ]; then \
		echo "Poetry is not installed. Please install it using:"; \
		echo "pip install poetry"; \
		exit 1; \
	fi
	@if [ -z "$(DOCKER)" ]; then \
		echo "Docker is not installed. Please install Docker and Docker Compose."; \
		exit 1; \
	fi
	@echo "All required tools are installed."

.PHONY: init-configs
init-configs:
	@cp -n .env.example .env || true
	@cp -n compose.override.dev.yaml compose.override.yaml || true
	@mkdir -p files_input files_output logs
	@touch logs/alternative_universe.log
	@echo "Configuration initialized. Directories and files created."

.PHONY: init-dev
init-dev: check-requirements init-configs
	@if [ -n "$(POETRY)" ]; then \
		poetry install --no-root --sync && \
		poetry run pre-commit install; \
	else \
		echo "Poetry is not installed. Please install it and run 'make init-dev' again."; \
	fi

.PHONY: run
run: check-requirements
	@if [ -n "$(POETRY)" ]; then \
		poetry run python main.py; \
	else \
		echo "Poetry is not installed. Please install it and run 'make init-dev' first."; \
	fi

.PHONY: test
test: check-requirements
	@if [ -n "$(POETRY)" ]; then \
		poetry run pytest; \
	else \
		echo "Poetry is not installed. Please install it and run 'make init-dev' first."; \
	fi

.PHONY: lint
lint: check-requirements
	@if [ -n "$(POETRY)" ]; then \
		poetry run ruff check .; \
	else \
		echo "Poetry is not installed. Please install it and run 'make init-dev' first."; \
	fi

.PHONY: format
format: check-requirements
	@if [ -n "$(POETRY)" ]; then \
		poetry run ruff format .; \
	else \
		echo "Poetry is not installed. Please install it and run 'make init-dev' first."; \
	fi

.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -f logs/*.log
	@rm -f files_output/*.txt

.PHONY: docker-build docker-up docker-down docker-purge

docker-build: check-requirements
	@if [ -n "$(DOCKER)" ]; then \
		docker compose build; \
	else \
		echo "Docker is not installed. Please install Docker and Docker Compose."; \
	fi

docker-up: check-requirements
	@if [ -n "$(DOCKER)" ]; then \
		docker compose up -d; \
	else \
		echo "Docker is not installed. Please install Docker and Docker Compose."; \
	fi

docker-down: check-requirements
	@if [ -n "$(DOCKER)" ]; then \
		docker compose down; \
	else \
		echo "Docker is not installed. Please install Docker and Docker Compose."; \
	fi

docker-purge: check-requirements
	@if [ -n "$(DOCKER)" ]; then \
		docker compose down -v --rmi all --remove-orphans; \
	else \
		echo "Docker is not installed. Please install Docker and Docker Compose."; \
	fi

.PHONY: pre-commit-run
pre-commit-run:
	poetry run pre-commit run

.PHONY: pre-commit-run-all
pre-commit-run-all:
	poetry run pre-commit run --all-files

.PHONY: poetry-install
poetry-install:
	@poetry install --no-root --sync

.PHONY: poetry-update
poetry-update:
	@poetry update

# [poetry]-[BEGIN]
.PHONY: poetry-up-latest
# Update all packages to the latest version allowed by the current constraints.
poetry-up-latest:
	@poetry up --latest

.PHONY: poetry-up-latest-no-install
# Update all packages to the latest version allowed by the current constraints.
poetry-up-latest-no-install:
	@poetry up --latest --no-install

.PHONY: poetry-lock
# Lock the current dependencies.
poetry-lock:
	@poetry lock

.PHONY: poetry-export-requirements
# Export the current dependencies to requirements.txt.
poetry-export-requirements:
	@poetry export --format requirements.txt --output requirements.txt --without-hashes
# [poetry]-[END]

# [extra_python]-[BEGIN]
.PHONY: install-pipx
# Install pipx.
# Note: Reloading shell is needed after this action.
# Note: Make not from virtual environment.
install-pipx:
	@python3.12 -m ensurepip &&\
	python3.12 -m pip install --upgrade pip &&\
	python3.12 -m pip install --user pipx &&\
	python3.12 -m pipx ensurepath

.PHONY: install-poetry
# Install poetry.
# Note: Reloading shell is needed after this action.
install-poetry:
	@pipx install poetry &&\
	pipx upgrade poetry &&\
	poetry self add poetry-plugin-export ;\
	poetry self add poetry-plugin-up

.PHONY: install-pre-commit
# Install pre-commit.
install-pre-commit:
	@pipx install pre-commit &&\
	pipx upgrade pre-commit

.PHONY: install-ruff
# Install ruff.
install-ruff:
	@pipx install ruff &&\
	pipx upgrade ruff
# [extra_python]-[END]
