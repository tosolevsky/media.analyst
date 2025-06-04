import os

def is_testing_mode() -> bool:
    return os.environ.get("TESTING") == "1"
