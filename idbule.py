import time
import machine
import mfrc522

# RFID - Buzzer - Led

def runn():
	rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	valids = [
		"0x4ab20f0a"
	]

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		while True:
			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:
				(stat, raw_uid) = rdr.anticoll()

				uid_string = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

				if uid_string in valids:
					print("Pass")

					# Pin(12) - D6
					beeper = machine.PWM(machine.Pin(12), freq=440, duty=1)
					time.sleep(0.2)
					beeper.deinit()
				else:
					print("Block")

					# Pin(12) - D6
					beeper = machine.PWM(machine.Pin(12), freq=440, duty=1)
					time.sleep(0.2)
					beeper.deinit()
					beeper = machine.PWM(machine.Pin(12), freq=440, duty=1)
					time.sleep(0.2)
					beeper.deinit()
				
	except KeyboardInterrupt:
		print("Bye")