import RPi.GPIO as GPIO
from config import DetectorsConfig, AppConfig
from modules.motion_detector import MotionDetector
import time
from datetime import datetime


class App:
    def __init__(self):
        self.detectors = []

        self.is_running = False

        self.setup_gpio()
        self.init_detectors()

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
