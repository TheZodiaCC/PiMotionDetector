import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)

    while True:
        if GPIO.input(23):
            print("Motion detected")

        else:
            print("Motion not detected")

        time.sleep(0.5)


if __name__ == "__main__":
    main()
