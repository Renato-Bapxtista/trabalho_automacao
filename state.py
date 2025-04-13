#state.py

class State:
    def __init__(self, state):
        self.value = state
    
    def on(self):
        self.value = 1
    
    def off(self):
        self.value = 0
        
    def toggle(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0
            
    
    