# light_switch.py

from machine import Pin
from time import sleep
from state import State

class Light_switch:
    def __init__(self, pin, callback=None, pull=Pin.PULL_UP):
        self.switch = Pin(pin, Pin.IN, pull)
        self.callback = callback
        self.last_state =State(self.switch.value())

        if callback:
            #usa interrução para capturar o click do interruptor
            self.switch.irq(trigger=Pin.IRQ_FALLING, handler=self._handle_interrupt)

    def _handle_interrupt(self, pin):
        sleep(0.01)  # debounce
        if not (self.switch.value() == self.last_state.value):
            self.last_state.toggle()            
            self.callback()
           
