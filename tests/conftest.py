"""Configuration file for pytest.

This file sets up logging for the test suite.
"""

from __future__ import annotations

import logging
from pathlib import Path


def pytest_configure(config):
    """Configure pytest environment before starting the test run.

    This function sets up logging for the test suite, creating a
    separate log file for test execution.
    """
    # Create directory for test logs if it doesn't exist
    test_log_dir = Path(__file__).parent / "test_logs"
    test_log_dir.mkdir(exist_ok=True)

    # Configure logging for tests
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=test_log_dir / "test_run.log",
        filemode="w",
    )


def pytest_sessionstart(session):
    """Perform operations before the test session starts.

    This function logs the start of the test session.
    """
    logging.info("Starting test session")


def pytest_sessionfinish(session, exitstatus):
    """Perform operations after the test session finishes.

    This function logs the end of the test session and its exit status.
    """
    logging.info(f"Test session finished with exit status: {exitstatus}")
