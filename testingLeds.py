#Author: Rohan Keenoy
#Playing with the adafruit breadboard kit for the pico
#focusing on making the leds animate to the song
from machine import Pin, PWM
import time

def buzz(i,hrtz):
    buzzr.duty_u16(40000)
    #buzzr.freq(hrtz)
    if ( i =="A4"):
        buzzr.freq(hrtz)
        led2.value(1)
    elif (i == "F4"):
        buzzr.freq(hrtz)
        led.value(1)
    elif (i == "AS4"):
        buzzr.freq(hrtz)
        led3.value(1)
    else:
        buzzr.freq(hrtz)
        led4.value(1)

def rest():
    buzzr.duty_u16(0)
    time.sleep(0.05)
    
    
def rocknRoll(blink182):
    for i in range(len(blink182)):
        if (blink182[i] == "QR"):
            rest()
        else:
            buzz(blink182[i],notes[blink182[i]])
        time.sleep(0.25)
        rest()
        led.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
#LEDS, buzzer, and Button 
led = Pin(0, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
buzzr = PWM(Pin(6))
btn = Pin(7, Pin.IN, Pin.PULL_UP)
#dictonary of notes we will use
notes = {"A4" : 440,
         "F4" : 349,
         "E4" : 330,
         "C4" : 262,
         "AS4" : 466,
         "G4" : 392}
blink182= ["A4","F4","QR", "E4", "F4", "QR", "A4","F4","QR", "E4", "F4", "QR", "A4","A4","AS4","A4","G4","F4","E4","QR","F4","E4","E4","E4","E4","E4", "F4"]

while True:
    if btn.value() == 0:
        print("BTN 1 is Pressed!")
        rocknRoll(blink182)
        buzzr.duty_u16(0)
        led.value(1)
        time.sleep(0.05)
    else:
        led.value(0)