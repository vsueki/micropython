import machine
import time

green_led = machine.Pin(16, machine.Pin.OUT)
red_led = machine.Pin(5, machine.Pin.OUT)

count = 100

for i in range(count):
 if i % 2 == 1:
  print("Prime: %s" % i)
  red_led.off()
  green_led.on()
  time.sleep(2)
 else:
  print("Non Prime: %s" % i)
  green_led.off()
  red_led.on()
  time.sleep(2))
