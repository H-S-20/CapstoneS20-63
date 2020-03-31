import time
import board
import busio
from adafruit_lsm6ds import LSM6DSOX
import paho.mqtt.publish as publish

i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DSOX(i2c)
 
MQTT_SERVER = "192.168.1.11" #Needs to be changed based on network
MQTT_PATH = "test_channel"
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)

x_count = 0
x_count_back = 0
y_count = 0
y_count_back = 0
z_count = 0
z_count_back = 0

x_accel_start,y_accel_start,z_accel_start = sensor.acceleration
x_gyro_start,y_gyro_start,z_gyro_start = sensor.gyro
threshold = 3

while True:
    x_accel,y_accel,z_accel = sensor.acceleration
    x_gyro,y_gyro,z_gyro = sensor.gyro
    #print(f"Acceleration: X:{x_accel:.2f}, Y:{y_accel:.2f}, Z:{z_accel:.2f} m/s^2")
    #print(f"Gyro: X:{x_gyro:.2f}, Y:{y_gyro:.2f}, Z:{z_gyro:.2f} degrees/s")
    
    if(x_accel > threshold+x_accel_start):
        x_count = x_count + 1
        if(x_count > 3):
            change = True
            print(f"Moving x positive {x_count}")
            publish.single(MQTT_PATH, "Forward", hostname=MQTT_SERVER)
            x_count = 0
    else:
        x_count = 0

    if(x_accel < x_accel_start-threshold):
        x_count_back = x_count_back + 1
        if(x_count_back > 3):
            change = True
            print(f"Moving x negative {x_count_back}")
            publish.single(MQTT_PATH, "Backwards", hostname=MQTT_SERVER)
            x_count_back = 0
    else:
        x_count_back = 0

    if(y_accel > y_accel_start+threshold):
        y_count = y_count + 1
        if(y_count > 3):
            change = True
            print(f"Moving y positive {y_count_back}")
            publish.single(MQTT_PATH, "Left", hostname=MQTT_SERVER)
            y_count = 0
    else:
        y_count = 0

    if(y_accel < y_accel_start-threshold):
        y_count_back = y_count_back + 1
        if(y_count_back > 3):
            change = True
            print(f"Moving y negative {y_count}")
            publish.single(MQTT_PATH, "Right", hostname=MQTT_SERVER)
            y_count_back = 0
    else:
        y_count_back = 0
        
    if(z_accel > threshold+z_accel_start):
        z_count = z_count + 1
        if(z_count > 3):
            change = True
            print(f"Moving z positive {z_count}")
            z_count = 0
            #publish.single(MQTT_PATH, "I don't know", hostname=MQTT_SERVER)
    else:
        z_count = 0
        
    if(z_accel < z_accel_start-threshold):
        z_count_back = z_count_back + 1
        if(z_count_back > 3):
            change = True
            print(f"Moving z negative {z_count_back}")
            z_count_back = 0
            #publish.single(MQTT_PATH, "I don't know", hostname=MQTT_SERVER)
    else:
        z_count_back = 0
        
    time.sleep(0.2)
