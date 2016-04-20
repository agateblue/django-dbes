#!/usr/bin/env python
import os
import sys
import signal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def sigterm_handler(signum, frame):
    sys.exit(1)

if __name__ == "__main__":
    sys.path.append(os.path.join(BASE_DIR, 'tests'))
    sys.path.append(os.path.join(BASE_DIR, 'dbes'))

    signal.signal(signal.SIGTERM, sigterm_handler)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phonealchemist.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
