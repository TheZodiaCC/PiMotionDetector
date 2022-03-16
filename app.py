import RPi.GPIO as GPIO
from config import DetectorsConfig, AppConfig
from modules.motion_detector import MotionDetector
from modules.bot import RPiMotionDetectorBOT
import multiprocessing
import time
from datetime import datetime


class App:
    def __init__(self):
        self.bot = None
        self.bot_process = multiprocessing.Process(target=self.run_bot)

        self.detectors = []

        self.is_running = False

        self.init()

    def init(self):
        self.setup_gpio()
        self.init_detectors()
        self.start_bot_process()

    def start_bot_process(self):
        self.bot_process.start()

    def run_bot(self):
        self.bot = RPiMotionDetectorBOT()
        self.bot.run(AppConfig.DISCORD_BOT_TOKEN)

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)

    def init_detectors(self):
        for detector_config in DetectorsConfig.DETECTORS:
            detector = MotionDetector(detector_config[DetectorsConfig.PIN_KEY_NAME],
                                       detector_config[DetectorsConfig.SECTOR_KEY_NAME])

            self.detectors.append(detector)

    def check_detectors(self):
        for detector in self.detectors:
            if detector.check_detection():
                print(f"[{datetime.now()}] {detector.sector}")

    def start_mainloop(self):
        self.is_running = True

        self.mainloop()

    def mainloop(self):
        while self.is_running:
            self.check_detectors()

            time.sleep(AppConfig.CHECK_RATIO_TIME)
