import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    CHECK_RATIO_TIME = 0.5

    LOG_FILES_DIR_PATH = os.path.join(CURRENT_DIR, "logs")

    BOT_LOGS_FILE = "bot.txt"


class DiscordConfig:
    BOT_COMMAND_PREFIX = "!"

    DISCORD_WEBHOOK_URL = ""

    DISCORD_BOT_TOKEN = ""
    DISCORD_TARGET_GUILD = ""
    DISCORD_TARGET_CHANNEL = ""


class BotConfig:
    MESSAGE_TYPE_KEY_NAME = "type"
    MESSAGE_CONTENT_KEY_NAME = "content"

    MESSAGE_TYPE_MESSAGE_KEY_NAME = "message"
    FILE_TYPE_MESSAGE_KEY_NAME = "file"


class DetectorsConfig:
    SECTOR_KEY_NAME = "sector"
    PIN_KEY_NAME = "pin"

    DETECTORS = [
        {
            SECTOR_KEY_NAME: "living room",
            PIN_KEY_NAME: 23
        }
    ]
