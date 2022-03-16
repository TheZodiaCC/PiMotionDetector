import RPi.GPIO as GPIO
from config import DetectorsConfig, AppConfig
from modules.motion_detector import MotionDetector
from modules.bot import RPiMotionDetectorBOT
import threading
import time
from datetime import datetime
import asyncio


class App:
    def __init__(self):
        self.bot = None
        self.bot_process = None

        self.detectors = []

        self.is_running = False

        self.init()

    def init(self):
        self.setup_gpio()
        self.init_detectors()
        self.start_bot_process()

    def start_bot_process(self):
        asyncio.get_child_watcher()

        bot_loop = asyncio.get_event_loop()
        bot_loop.create_task(self.run_bot())

        self.bot_process = threading.Thread(target=self.run_bot_loop, args=(bot_loop,))
        self.bot_process.start()

    async def run_bot(self):
        self.bot = RPiMotionDetectorBOT()
        await self.bot.start(AppConfig.DISCORD_BOT_TOKEN)

    def run_bot_loop(self, bot_loop):
        bot_loop.run_forever()

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

                message = f"[{datetime.now()}] {detector.sector}"

                # if self.bot is not None:
                #     self.bot.send_message(message)

                print(message)

    def start_mainloop(self):
        self.is_running = True

        self.mainloop()

    def mainloop(self):
        while self.is_running:
            self.check_detectors()

            time.sleep(AppConfig.CHECK_RATIO_TIME)
