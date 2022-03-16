from datetime import datetime
from config import AppConfig


def log_message(message):
    with open(AppConfig.LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"[{datetime.now()}]{message}\n")


def read_log_file():
    with open(AppConfig.LOG_FILE_PATH, "r") as log_file:
        return log_file.readlines()
