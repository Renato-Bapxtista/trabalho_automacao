#webServer

import network
import socket
from led import Led

class WebServer:
    def __init__(self, Home, html_path, pin_led = 2):
        self.home = Home
        self.html_path = html_path
        self.led = Led(pin_led)

    def connect_wifi(self, ssid, password):
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.sta_if.connect(ssid, password)
        while not self.sta_if.isconnected():
            #led no esp32 fica piscando
            self.led.blink()
        print('Connected on', self.sta_if.ifconfig())
        #led no esp32 fica piscando
        self.led.on()
    def load_html(self):
        with open(self.html_path, 'r') as f:
            return f.read()

    def start(self):
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print('Listening on', addr)

        while True:
            cl, addr = s.accept()
            print('Client connected from', addr)
            request = cl.recv(1024).decode()
            print('Request:', request)

            if 'GET /home' in request:
                params = request.split(' ')[1]
                try:
                    action = params.split('action=')[1].split(' ')[0]
                    ambient = params.split('ambient=')[1].split('&')[0]
                    if ambient == 'quarto' and action == 'on':
                        self.home.quarto.lamp.on()
                    if ambient == 'quarto' and action == 'off':
                        self.home.quarto.lamp.off()
                    
                    if ambient == 'sala' and action == 'on':
                        self.home.sala.lamp.on()
                    if ambient == 'sala' and action == 'off':
                        self.home.sala.lamp.off()
                    
                    if ambient == 'cozinha' and action == 'on':
                        self.home.cozinha.lamp.on()
                    if ambient == 'cozinha' and action == 'off':
                        self.home.cozinha.lamp.off()
                    
                except Exception as e:
                    print('Error parsing params:', e)

            response = self.load_html()
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()

