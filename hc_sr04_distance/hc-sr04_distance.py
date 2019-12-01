#!/usr/bin/python

# import libraries
import RPi.GPIO as GPIO
import time

# GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# set GPIO pins
PIN_TRIGGER = 7
PIN_ECHO = 11

# set GPIO IN/OUT direction
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

# allow sensor to settle for more accurate readings
GPIO.output(PIN_TRIGGER, GPIO.LOW)
print "waiting for sensor to settle"
time.sleep(2)

# calculates distance
def distance():
    # trigger sensor, sending out pulse for 1ns
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)

    # deactivate sensor
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # calculate times for pulse to be sent and receivec
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    # find duration of pulse
    pulse_duration = pulse_end_time - pulse_start_time

    # find distance rounded to 2 decimal places and return value
    distance = round(pulse_duration * 17150, 2)
    return distance

if __name__ == "__main__":
    # continuously run distance calculation every second
    try:
        while True:
            dist = distance()
            print "Distance:", dist, "cm"

            time.sleep(1)
        
    # end program upon keyboard interrupt (ctrl+c)
    except KeyboardInterrupt:
        print "stopping measurement"
        GPIO.cleanup()