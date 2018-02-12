# D1 - led - 2k - G

import machine
import time

led = machine.Pin(5, machine.Pin.OUT)

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)