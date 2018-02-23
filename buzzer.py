import machine
import time

# Freq - the maximum frequency of PWM is currently 1000Hz, so you can’t play any notes higher than that.
# Duty - duty cycle is between 0 (all off) and 1023 (all on), with 512 being a 50% duty
# beeper.deinit() - stop buzzer

# Pin(14) - D5
beeper = machine.PWM(machine.Pin(14), freq=440, duty=1)
time.sleep(0.5)
beeper.deinit()