#!/usr/bin/env python3

from rpi_hardware_pwm import HardwarePWM
from getkey import getkey

### raspi-gpio set 18 a5

fan = HardwarePWM(pwm_channel=0, hz=60)

speed = 0

fan.start(0)

print("Use 'w' and 's' to control speed, 'q' to exit.")
print("Speed: 0", end = "\r")

while True:

  key = getkey()

  if (key == "q"):

    break

  elif (key == "w"):

    speed = speed + 10

    if speed >= 100:

      speed = 100

    fan.change_duty_cycle(speed)
    print("Speed:", speed, end = "\r")

  elif (key == "s"):

    speed = speed - 10

    if speed <= 0:

      speed = 0

    fan.change_duty_cycle(speed)
    print("          ", end = "\r")
    print("Speed:" , speed, end = "\r")


fan.stop()
