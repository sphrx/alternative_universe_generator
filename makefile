# Get user id for macOS and Linux
ifeq ($(shell uname),Darwin)
    USER_ID := $(shell id -u)
else
    USER_ID := $(shell id --user)
endif

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make init-configs          - Initialize configuration files"
	@echo "  make init-dev              - Initialize development environment"
	@echo "  make run                   - Run the application"
	@echo "  make test                  - Run tests"
	@echo "  make lint                  - Run linter"
	@echo "  make format                - Format code"
	@echo "  make clean                 - Clean temporary files"
	@echo "  make docker-build          - Build Docker image"
	@echo "  make docker-run            - Run application in Docker"
	@echo "  make docker-up             - Start Docker Compose services"
	@echo "  make docker-down           - Stop Docker Compose services"
	@echo "  make docker-purge          - Remove all Docker resources"
	@echo "  make pre-commit-run        - Run pre-commit hooks"
	@echo "  make pre-commit-run-all    - Run pre-commit hooks on all files"
	@echo "  make poetry-install        - Install dependencies"
	@echo "  make poetry-update         - Update dependencies"

.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp -n .env.example .env || true
	@cp -n compose.override.dev.yaml compose.override.yaml || true
#	@mkdir -p files_input files_output logs
	@chmod 755 files_input files_output logs
	@touch logs/alternative_universe.log
	@chmod 644 logs/alternative_universe.log
	@echo "Configuration initialized. Directories and files created with appropriate permissions."

.PHONY: init-dev
# Init environment for development
init-dev: init-configs
	@make poetry-install && \
	poetry run pre-commit install

.PHONY: run
run:
	@poetry run python main.py

.PHONY: test
test:
	@pytest

.PHONY: lint
lint:
	@ruff check .

.PHONY: format
format:
	@ruff format .

.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -f logs/*.log
	@rm -f files_output/*.txt

.PHONY: docker-build
docker-build:
	@docker build -t alternative-universe .

.PHONY: docker-run
docker-run: docker-build
	@docker run alternative-universe

.PHONY: docker-up
docker-up:
	@docker-compose up -d

.PHONY: docker-down
docker-down:
	@docker-compose down

.PHONY: docker-purge
docker-purge:
	@docker-compose down -v --rmi all --remove-orphans

.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files

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
