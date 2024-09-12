# Use the official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install poetry and dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the project files
COPY . .

# Create directories for input and output files
RUN mkdir -p /app/files_input /app/files_output

# Run the application
CMD ["python", "main.py"]
