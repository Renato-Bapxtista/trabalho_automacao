#main.py

from machine import Pin
import time

from webServer import WebServer
from light_switch import Light_switch
from lamp import Lamp
from ambient import Ambient
from home import Home
from time import sleep

#instanciando as lampadas
lamp1 = Lamp(25,26)
lamp2 = Lamp(14,27)
lamp3 = Lamp(13,12)

#instanciando os interruptores
switch1 = Light_switch(18,lamp1.toggle)
switch2 = Light_switch(19,lamp2.toggle)
switch3 = Light_switch(21,lamp3.toggle)


#instanciando o home 
home = Home(cozinha=Ambient(lamp1, switch1), quarto=Ambient(lamp2,switch2), sala=Ambient(lamp3,switch3))

#instanciando o servidor
server = WebServer(home, 'index.html')
server.connect_wifi('Fernanda', 'cocorico')
server.start()


while True:   
    sleep(0.3)