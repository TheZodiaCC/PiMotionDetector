class AppConfig:
    CHECK_RATIO_TIME = 0.5


class DetectorsConfig:
    SECTOR_KEY_NAME = "sector"
    PIN_KEY_NAME = "pin"

    DETECTORS = [
        {
            SECTOR_KEY_NAME: "living room",
            PIN_KEY_NAME: 23
        }
    ]
