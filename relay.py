# relay.py
from state import State
from machine import Pin

class Relay:
    def __init__(self, pin):
        self.relay = Pin(pin, Pin.OUT)
        self.state = State(0)
        self.relay.value(self.state.value)

    def on(self):
        self.state.toggle()
        self.relay.value(self.state.value)

    def off(self):
        self.state.toggle()
        self.relay.value(self.state.value)

    def toggle(self):
        self.state.toggle()
        self.relay.value(self.state)
