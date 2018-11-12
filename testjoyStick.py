from sense_hat import SenseHat

sense = SenseHat()

def red():
	sense.clear(255,0,0)

def blue():
	sense.clear(0,0,255)

def green():
	sense.clear(51,255,51)

def purple():
	sense.clear(128,0,128)

sense.stick.direction_up = red
sense.stick.direction_down = blue 
sense.stick.direction_left = green
sense.stick.direction_right = purple
sense.stick.direction_middle = sense.clear

while True:
	pass

