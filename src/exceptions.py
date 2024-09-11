from src.imports import Exception

class EventFileNotFoundError(Exception):
    """Вызывается, когда файл с историческими событиями не найден."""
    pass

class EventDataError(Exception):
    """Вызывается при проблемах с данными исторических событий."""
    pass