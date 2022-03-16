import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    CHECK_RATIO_TIME = 0.5

    DISCORD_BOT_TOKEN = ""
    DISCORD_TARGET_GUILD = ""
    DISCORD_TARGET_CHANNEL = ""

    BOT_COMMAND_PREFIX = "!"

    LOG_FILES_DIR_PATH = os.path.join(CURRENT_DIR, "logs")

    BOT_LOGS_FILE = "bot.txt"


class DetectorsConfig:
    SECTOR_KEY_NAME = "sector"
    PIN_KEY_NAME = "pin"

    DETECTORS = [
        {
            SECTOR_KEY_NAME: "living room",
            PIN_KEY_NAME: 23
        }
    ]
