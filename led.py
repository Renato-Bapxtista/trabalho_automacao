#led.py

from machine import Pin, ADC
from time import sleep

class Led:
    def __init__(self, pin):
        """     
        Classe para gerenciar um LED em MicroPython.

        :param pin: Número do pino GPIO onde o LED está conectado.
        """
        self.led = Pin(pin, Pin.OUT)
        self.state = 0
        self.led.value(self.state)  

    def on(self):        
        self.state = 1
        self.led.value(self.state)

    def off(self):
        self.state = 0
        self.led.value(self.state)
        
    def toggle(self):
        self.state = not self.state
        self.led.value(self.state)
    def blink(self):
        self.toggle()
        sleep(0.3)

