import os


def _get_env(name: str, default):
    """
    Универсальный хелпер для чтения переменных окружения
    с дефолтным значением.
    """
    return os.getenv(name, default)


# ===== ОСНОВНЫЕ ПАРАМЕТРЫ ЗАПУСКА =====

# Какой браузер использовать: chrome / firefox
BROWSER = _get_env("BROWSER", "chrome")

# Запускать ли браузер в headless-режиме
HEADLESS = _get_env("HEADLESS", "false").lower() == "true"

# Таймаут ожиданий (секунды)
TIMEOUT = int(_get_env("TIMEOUT", 10))

# Оставлять ли браузер открытым после теста
KEEP_BROWSER = _get_env("KEEP_BROWSER", "false").lower() == "true"

# Уровень логирования: DEBUG / INFO / WARNING / ERROR
LOG_LEVEL = _get_env("LOG_LEVEL", "INFO")