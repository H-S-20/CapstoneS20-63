import spidev
import time

#Define Variables, delay returns values every 0.5 seconds
delay = 0.5
pad_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    # gets value from the channel and returns the value
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        #calls read function with channel as the parameter
        pad_value = readadc(pad_channel)
        print("---------------------------------------")
        print("Flex Sensor Value: %d" % pad_value)
        time.sleep(delay)
except KeyboardInterrupt:
    pass

#From here, I would make an if statement that opens the slide file when the flex sensor resistance value is over a set threshold.
#This is more easier done by trial and error
