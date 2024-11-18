  #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 03:09:26 2024

@author: ubuntu
"""

import RPi.GPIO as GPIO
import time
# Set up GPIO pins using BCM numbering scheme
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin numbers you want to read (replace with your standard GPIO pin numbers)
gpio_pins_up = [6,12,19,21]
gpio_pins_down = [17,25,1]
gpio_pins_high=[13,26,16,20]
# Set GPIO pins as input
GPIO.setup(gpio_pins_high, GPIO.OUT,initial=1)

GPIO.setup(gpio_pins_up, GPIO.IN,pull_up_down=GPIO.PUD_UP)


#GPIO.setup(gpio_pins_up, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(gpio_pins_down, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Loop continuously reading the GPIO pin states
while True:
    print("----------------------------------------------------------")
#    print("AMA0) "+str(GPIO.input(17)))
#    print("AMA1) "+str(GPIO.input(1))) # eeprom i2c maybe issue allways on 
#    print("AMA2) "+str(GPIO.input(25)))
    print("strat1) "+str(GPIO.input(6)))
    print("strat2) "+str(GPIO.input(12)))
    print("couleur) "+str(GPIO.input(19)))
    print("tirette) "+str(GPIO.input(21)))
    print("pinhigh) "+str(GPIO.input(13)))
    print("pinhigh) "+str(GPIO.input(26)))
    print("pinhigh) "+str(GPIO.input(16)))
    print("pinhigh) "+str(GPIO.input(20)))
#    
  # Add a delay to avoid overwhelming the CPUc
    time.sleep(0.1)

# Clean up GPIO on exit
GPIO.cleanup()