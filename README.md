# PWM control for Raspberry Pi
It uses rpi-hardware-pwm

https://pypi.org/project/rpi-hardware-pwm/

## Config:

***echo "dtoverlay=pwm-2chan" >> /boot/config.txt***

***reboot***

***sudo pip3 install rpi-hardware-pwm***

## Seems to be needed on Raspberry Pi 1

***raspi-gpio set 18 a5***


