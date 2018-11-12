from sense_hat import SenseHat
sense = SenseHat()
sense.clear

temp = sense.get_temperature()
intTemp = int(temp)
stringTemp = str(intTemp)

humidity = sense.get_humidity()
intHumid = int(humidity)
stringHumid = str(intHumid)

pressure = sense.get_pressure()
intPressure = int(pressure)
stringPressure = str(intPressure)


green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

def ShowTemp():
	sense.show_message(stringTemp,0.2,green)
def ShowHumid():
	sense.show_message(stringHumid,0.2,blue)
def ShowPressure():
	sense.show_message(stringPressure,0.2,red)
def EasterEgg():
	

while True:
	sense.stick.direction_up = ShowTemp
	sense.stick.direction_middle = sense.clear
	sense.stick.direction_down = ShowHumid
	sense.stick.direction_right = ShowPressure
	sense.stick.direction_left = EasterEgg
