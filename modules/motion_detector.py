import RPi.GPIO as GPIO


class MotionDetector:
    def __init__(self, detector_pin, sector):
        self.detector_pin = detector_pin
        self.sector = sector

        self.init_gpio()

    def init_gpio(self):
        GPIO.setup(self.detector_pin, GPIO.IN)

    def check_detection(self):
        return GPIO.input(self.detector_pin)
