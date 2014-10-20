# -*- coding: utf-8 -*-
import os
import sys

PROJECT_NAME = 'upload'

BASE_DIR = os.path.join(os.path.dirname(__file__),PROJECT_NAME)
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings"%PROJECT_NAME)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

