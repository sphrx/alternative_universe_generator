"""Custom exceptions for the Alternative Universe Generator."""

from __future__ import annotations


class EventFileNotFoundError(Exception):
    """Raised when the file with historical events is not found."""


class EventDataError(Exception):
    """Raised when there are problems with historical event data."""
