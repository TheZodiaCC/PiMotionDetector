import RPi.GPIO as GPIO
from config import DetectorsConfig, AppConfig, DiscordConfig
from modules.motion_detector import MotionDetector
from modules.bot import RPiMotionDetectorBOT
from modules.motion_notifier import MotionDetectionNotifier
import multiprocessing
import time
from datetime import datetime
import log_utils


class App:
    def __init__(self):
        self.bot = None
        self.bot_process = None

        self.notifier_webhook = None

        self.detectors = []

        self.is_running = False

        self.init()

    def init(self):
        self.setup_gpio()
        self.init_detectors()
        self.start_bot_process()
        self.init_notifier()

    def start_bot_process(self):
        self.bot_process = multiprocessing.Process(target=self.run_bot)
        self.bot_process.start()

    def run_bot(self):
        self.bot = RPiMotionDetectorBOT()
        self.bot.run(DiscordConfig.DISCORD_BOT_TOKEN)

    def init_notifier(self):
        try:
            self.notifier_webhook = MotionDetectionNotifier()

        except Exception as e:
            log_utils.log_bot(f"Error while initializing notifier webhook {e}")

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
                log_utils.log_message(detector.sector)

                if self.notifier_webhook is not None:
                    self.notifier_webhook.send_message(f"[{datetime.now()}] {detector.sector}")

    def start_mainloop(self):
        self.is_running = True

        self.mainloop()

    def mainloop(self):
        while self.is_running:
            self.check_detectors()

            time.sleep(AppConfig.CHECK_RATIO_TIME)
