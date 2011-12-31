import os

from datetime import datetime


PROJECT_NAME = "Status"
PROJECT_URL = "#"
TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "templates")
CONTEXT = {
    "CURRENT_DATE": datetime.now(),
}
MACHINES = {
    "www.google.com": {
        "name": "Google",
        "address": "www.google.com",
        "services": [
            {
                "name": "Google",
                "address": "http://www.google.com",
            },
        ],
    },
}
DEBUG = True

try:
    from local_settings import MACHINES, PROJECT_NAME, PROJECT_URL, DEBUG
except:
    pass

CONTEXT["PROJECT_NAME"] = PROJECT_NAME
