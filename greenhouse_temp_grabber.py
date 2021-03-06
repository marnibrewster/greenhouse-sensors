GNU nano 2.2.6        File: temperature_sensor_code.py

import os
import glob
import time
import requests
import json

firebase_url = "YOUR URL HERE"


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      temp_f = temp_c * 9.0 / 5.0 + 32.0
     # return temp_c, temp_f
      time_hhmmss = time.strftime('%H:%M:%S')
      date_mmddyyyy = time.strftime('%m/%d/%Y')
      temperature_location = 'Greenhouse1'

      data = {'data':date_mmddyyyy,'time':time_hhmmss, 'value':temp_f}
      result = requests.post(firebase_url + '/' + temperature_location + '/'

      print 'Record inserted. result code = ' + str(result.status_code) + ','
      return temp_f

while True:
      #print(read_temp()
      read_temp()
      time.sleep(1800)
