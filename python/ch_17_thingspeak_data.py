import time, os
import requests
from gpiozero import CPUTemperature


PERIOD = 60 # seconds
BASE_URL = 'https://api.thingspeak.com/update.json'
KEY = '6R1H2RF39T5FWJIU'

def send_data(temp):
    data = {'api_key' : KEY, 'field1' : temp}
    response = requests.post(BASE_URL, json=data)

def cpu_temp():
    cpu_temp = CPUTemperature()
    return cpu_temp.temperature


while True:
    temp = cpu_temp()
    print("CPU Temp (C): " + str(temp))
    send_data(temp)
    time.sleep(PERIOD)

