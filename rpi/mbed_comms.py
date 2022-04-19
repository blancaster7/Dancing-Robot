#https://www.engineersgarage.com/articles-raspberry-pi-serial-communication-uart-protocol-ttl-port-usb-serial-boards/
import time
from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial
import os
os.system("spotify_client.py")

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while 1:
    rx_data = ser.read() #read serial data
    sleep(0.03)    
    data_left = ser.inWaiting()
    rx_data += ser.data(data_left)
    if ser.inWaiting != 0:
        get_current_song(sp)
        toggle_playback(sp)

#mbed controlling all physical components
