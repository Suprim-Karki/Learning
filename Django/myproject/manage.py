#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
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

'''
To setup virtual environment
   pip install virtualenv
   python -m venv env
   env\scripts\activate     or .\env\Scripts\Activate.ps1    
   pip install django
   django-admin startproject myproject
   python manage.py startapp myapp
   
To run
   python manage.py runserver
'''