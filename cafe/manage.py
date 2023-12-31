#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import threading
from app.telegram_bot import start_bot

 # Запускаем бота в отдельном потоке
bot_thread = threading.Thread(target=start_bot)
bot_thread.daemon = True
bot_thread.start()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafe.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    


if __name__ == '__main__':
    main()
    

