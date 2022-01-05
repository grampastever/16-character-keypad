# the following program interfaces a 4x4 button keypad
#with the Rpi Pico using micropython running in Thonny

from machine import Pin
from utime import sleep

for i in range(4,8):
    Pin(i, Pin.IN, Pin.PULL_DOWN)

for i in range(4):
    Pin(i, Pin.OUT, Pin.PULL_DOWN, value=0)

key_pad = [['1', '2', '3', 'A'],
           ['4', '5', '6', 'B'],
           ['7', '8', '9', 'C'],
           ['*', '0', '#', 'D']]

while True:
    for i in range(4):
        Pin(i, value=1)
        
        for j in range(4,8):
            if Pin(j).value() == 1:
                print(key_pad[i][j-4])
                counter = 0
                #press and hold function. Waits until count = 20 then rapidly scrolls
                while Pin(j).value() == 1:
                    if counter < 20:
                        counter = counter + 1
                        sleep(0.1)
                    else:
                        print(key_pad[i][j-4])
                        sleep(0.1)
                         
        Pin(i, value=0)
