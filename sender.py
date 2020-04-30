import time
import math
import board
import busio
from adafruit_lsm6ds import LSM6DSOX
import paho.mqtt.publish as publish
#from scipy.integrate import quad
import spidev

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

MQTT_SERVER = "192.168.1.11" #Needs to be changed based on network
MQTT_PATH = "test_channel"
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)

i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DSOX(i2c)

#Generating Angle
#Tones down sensor sensitivity
ACCELEROMETER_SENSITIVITY = 8192.0
GYROSCOPE_SENSITIVITY = 65.536
 
#Two constants
M_PI = 3.14159265359
dt = 0.01   #10 ms sample rate!

#pitch is x-axis degree turns
#roll is the y-axis degree turns
#yaw (z-axis) isn't used
pitch = 0
roll = 0

#Determining state variables
#Metastability counters
pitch_stability = 2
pitch_stability_back = 2
roll_stability = 2
roll_stability_back = 2

#If pitch/roll reaches angle_threshold for angle_stability*10ms, it is a valid turn
angle_stability = 2
angle_threshold = 130
angle_threshold_lower = 50
#5 states for proof of concept
state = ["palm_right","palm_left","palm_forward","palm_backwards","rest"]
curState = state[4] #Initial state is rest
change = True #Determine if state changed

#Determining user acceleration
#Filter Variables
count = 0
accSumX = 0
accSumY = 0
prevX = 0
prevY = 0
x_accel_data = 0
y_accel_data = 0
alpha = 0.25

#Threshold to pass to recognize movement
threshold = 1.5 #up and down
threshold_side = 1.5 #left and right

#Useful function for trig values
def signOf(num):
    if num >= 0:
        return 1
    else:
        return -1

#Data sending
send_data = ""


while True:
    #Takes initial sensor data
    accData = sensor.acceleration
    gyrData = sensor.gyro
    
    
    #Complementary filter
    # Integrate the gyroscope data -> int(angularSpeed) = angle
    pitch = pitch + (float(gyrData[0]) / GYROSCOPE_SENSITIVITY) * dt # Angle around the X-axis
    roll = roll - (float(gyrData[1]) / GYROSCOPE_SENSITIVITY) * dt  # Angle around the Y-axis
    
    #Compensate for drift with accelerometer data if !(not possible)
    #Sensitivity = -2 to 2 G at 16Bit -> 2G = 32768 && 0.5G = 8192
    forceMagnitudeApprox = abs(accData[0]) + abs(accData[1]) + abs(accData[2])
    if (forceMagnitudeApprox > 4 and forceMagnitudeApprox < 20):
        
    #Turning around the X axis results in a vector on the Y-axis
        pitchAcc = math.atan2(float(accData[1]), float(accData[2])) * 180 / M_PI
        pitch = pitch * 0.98 + pitchAcc * 0.02
 
    #Turning around the Y axis results in a vector on the X-axis
        rollAcc = math.atan2(float(accData[0]), float(accData[2])) * 180 / M_PI
        roll = roll * 0.98 + rollAcc * 0.02

    accSumX = accSumX + (accData[2]*math.cos((90-pitch)*M_PI/180) - accData[1]*math.cos(pitch* M_PI/180))
    accSumY = accSumY + (accData[2]*math.cos((90-roll)* M_PI/180) - accData[0]*math.cos(roll* M_PI/180))
    #Just for testing
    count = count + 1
    if count == 200:
        pad_value = readadc(pad_channel)
        print("---------------------------------------")
        print("Flex Sensor Value: %d" % pad_value)

        print("Roll: "+repr(pitch)+" \tPitch: "+repr(roll)+" \tCurrent State "+repr(curState))
        print()
        count = 0
        
        #Determine if the position of the glove changed
        #state = ["palm_right","palm_left","palm_forward","palm_backwards","rest"]
        state_change = False


        if roll < angle_threshold and roll > angle_threshold_lower:
            roll_stability = roll_stability + 1
            if roll_stability >= angle_stability and (curState != state[3] and curState != state[2]):
                curState = state[1] #palm_left
                
                state_change = True
        else:
            roll_stability = 0

        if roll > -1*angle_threshold and roll < angle_threshold_lower*-1:
            roll_stability_back = roll_stability_back + 1
            if roll_stability_back >= angle_stability and (curState != state[3] and curState != state[2]):
                curState = state[0] #palm_right
                
                state_change = True
        else:
            roll_stability_back = 0

        if state_change == False:
            if pitch < angle_threshold and pitch > angle_threshold_lower:
                pitch_stability = pitch_stability + 1
                if pitch_stability >= angle_stability and (curState != state[1] and curState != state[0]):   
                    curState = state[2] #palm_forward

                    state_change = True
            else:
                pitch_stability = 0


            if pitch > angle_threshold*-1 and pitch < angle_threshold_lower*-1:
                pitch_stability_back = pitch_stability_back + 1
                if pitch_stability_back >= angle_stability and (curState != state[1] and curState != state[0]):
                    curState = state[3] #palm_backwards
                    
                    state_change = True
            else:
                pitch_stability_back = 0

        if state_change == False:
            curState = state[4] #rest
        
        #Calculate the x acceleration and the y acceleration
        x_accel_data = (1-alpha)*accSumX/200+alpha*prevX
        y_accel_data = (1-alpha)*accSumY/200+alpha*prevY
        
        if curState == state[2] or curState == state[3]:
            if x_accel_data > prevX + threshold:
                print("Moving X forward")
                send_data = "forward"
            elif x_accel_data < prevX - threshold:
                print("Moving X backwards")
                send_data = "backwards"
            else:
                prevX = (1-alpha)*accSumX/200+alpha*prevX
        
        if curState == state[0] or curState == state[1]:
            if y_accel_data > prevY + threshold_side:
                print("Moving Y forward")
                send_data = "forward"
            elif y_accel_data < prevY - threshold_side:
                print("Moving Y backwards")
                send_data = "backwards"
            else:
                prevY = (1-alpha)*accSumY/200+alpha*prevY
            
        accSumX = 0
        accSumY = 0

        #If not in rest state, check for user acceleration
        if curState != state[4] and send_data != "":
            z_accel = x_accel_data
            if curState == state[0] or curState == state[1]:
                z_accel = y_accel_data
            send_data = curState + " " + send_data
            print(send_data)
            if pad_value > 700:
                publish.single(MQTT_PATH, send_data, hostname=MQTT_SERVER)
            send_data = ""