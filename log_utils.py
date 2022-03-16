from datetime import datetime
from config import AppConfig
import os


def log_message(message):
    log_file_name = f"{datetime.today().strftime('%Y-%m-%d')}.txt"

    log(message, log_file_name)


def log_bot(message):
    log(message, AppConfig.BOT_LOGS_FILE)


def log(message, log_file_name):
    log_file_path = os.path.join(AppConfig.LOG_FILES_DIR_PATH, log_file_name)

    with open(log_file_path, "a") as file:
        file.write(f"[{datetime.now()}]{message}\n")


def read_log_file(file):
    with open(os.path.join(AppConfig.LOG_FILES_DIR_PATH, file), "r") as log_file:
        return log_file.readlines()
