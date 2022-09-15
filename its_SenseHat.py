#!/usr/bin/python3
# -*- coding: utf-8 -*-


import time



try:
  from sense_hat import SenseHat
except ModuleNotFoundError:
  print("can not fint sense-hat try;")
  print("\tsudo apt install sense-hat")
  exit()

# senseHat 2 added color sensor
# Folllowing block supresses error
# WARNING:root:Failed to initialise TCS34725 colour sensor. (sensor not present)
# comment out if for V2
import logging
logging.getLogger().setLevel(logging.ERROR)
# end block

sense = SenseHat()
sense.set_rotation(270)

curr_time = list([0]) 
curr_temprature = list([0])  
curr_humidity = list([0])  
curr_pressure = list([0]) 

low_temprature = list([200])  
low_humidity = list([100])  
low_pressure = list([100000]) 

high_temprature = list([0])  
high_humidity = list([0])  
high_pressure = list([0]) 

zz = (0,0,0)
aa = (255,0,0)
bb = (0,255,0)
cc = (0,0,255)
dd = (100,100,0)

main_display = list([list(),list(),list(),list()])

main_display[3] = [
dd, zz, zz, zz, zz, zz, zz, dd,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
dd, zz, zz, zz, zz, zz, zz, dd
]
main_display[0] = [
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, aa, aa, zz, zz, zz,
zz, zz, zz, aa, aa, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz
]
main_display[1] = [
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, bb, zz, zz, bb, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, bb, zz, zz, bb, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz
]
main_display[2] = [
zz, zz, zz, zz, zz, zz, zz, zz,
zz, cc, zz, zz, zz, zz, cc, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, zz, zz, zz, zz, zz, zz, zz,
zz, cc, zz, zz, zz, zz, cc, zz,
zz, zz, zz, zz, zz, zz, zz, zz
]

while True:
  try:
    celcius = int(round(sense.get_temperature()))
    fahrenheit = int(round(1.8 * celcius + 32))
    samples = 3 
    F = sense.temp * 1.8 + 32
    low_mesure = [curr_time , low_temprature, low_humidity, low_pressure ]
    high_mesure = [curr_time , high_temprature, high_humidity, high_pressure ]
    mesure = [curr_time , curr_temprature, curr_humidity, curr_pressure ]
    sensers = [time.time(), fahrenheit, round(sense.humidity, 0), round(sense.pressure ,1) ]
    
    for x in range(len(mesure)) :
      sense.set_pixels(main_display[x])
      time.sleep(.25)
      
      mesure[x].append(round(sensers[x], 1))    
      if len(mesure[x]) > samples:
        mesure[x].pop(0) 
      if mesure[x] <= low_mesure[x]:
        low_mesure[x] = mesure[x]
      
      print(sensers)
                       
  except KeyboardInterrupt:
    sense.clear()
    exit()
