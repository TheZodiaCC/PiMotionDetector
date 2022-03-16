class AppConfig:
    CHECK_RATIO_TIME = 0.5

    DISCORD_BOT_TOKEN = ""
    DISCORD_TARGET_GUILD = ""
    DISCORD_TARGET_CHANNEL = ""

    BOT_COMMAND_PREFIX = "!"

    LOG_FILE_PATH = "logs.txt"


class DetectorsConfig:
    SECTOR_KEY_NAME = "sector"
    PIN_KEY_NAME = "pin"

    DETECTORS = [
        {
            SECTOR_KEY_NAME: "living room",
            PIN_KEY_NAME: 23
        }
    ]
