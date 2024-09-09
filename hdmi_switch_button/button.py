import time
import RPi.GPIO as GPIO
import struct
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 17

KEY_ASTERISK = 0x55
KEY_PAGE_DOWN = 0x4E

GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

def send_switch():
    keycodes = (KEY_ASTERISK, KEY_PAGE_DOWN)
    report = struct.pack('BBBBBBBB', 0, 0, *keycodes[:6], *(0,) * (6 - len(keycodes)))
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)
        time.sleep(0.1)
        fd.write(b'\x00' * 8)
        time.sleep(0.1)

while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
      send_switch()
    time.sleep(0.1)

