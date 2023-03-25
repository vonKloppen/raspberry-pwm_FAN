#!/usr/bin/env python3

from rpi_hardware_pwm import HardwarePWM
from time import sleep
from getkey import getkey

### raspi-gpio set 18 a5

fan = HardwarePWM(pwm_channel=0, hz=60)

speed = 0

fan.start(0)

while True:

  key = getkey()

  if (key == "q"):

    break

  elif (key == "w"):

    speed = speed + 10

    if speed >= 100:

      speed = 100

    fan.change_duty_cycle(speed)
    print(speed, end = "\r")

  elif (key == "s"):

    speed = speed - 10

    if speed <= 0:

      speed = 0

    fan.change_duty_cycle(speed)
    print("   ", end = "\r")
    print(speed, end = "\r")


fan.stop()
