import time
import board
import busio
from adafruit_lsm6ds import LSM6DSOX
import web
 
i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DSOX(i2c)
 
#urls = ('/','index')
        

x_count = 0
x_count_back = 0
y_count = 0
y_count_back = 0
z_count = 0
z_count_back = 0

x_accel_start,y_accel_start,z_accel_start = sensor.acceleration
x_gyro_start,y_gyro_start,z_gyro_start = sensor.gyro
change = False

#app = web.application(urls,globals())
#app.run()
#class index:
#    def GET(self):
while True:
    x_accel,y_accel,z_accel = sensor.acceleration
    x_gyro,y_gyro,z_gyro = sensor.gyro
    #print(f"Acceleration: X:{x_accel:.2f}, Y:{y_accel:.2f}, Z:{z_accel:.2f} m/s^2")
    #print(f"Gyro: X:{x_gyro:.2f}, Y:{y_gyro:.2f}, Z:{z_gyro:.2f} degrees/s")
    
    if(x_accel > 1+x_accel_start):
        x_count = x_count + 1
        if(x_count > 3):
            change = True
            print(f"Moving x left {x_count}")
#                    return "Left"
    else:
        x_count = 0

    if(x_accel < x_accel_start-1):
        x_count_back = x_count_back + 1
        if(x_count_back > 3):
            change = True
            print(f"Moving x right {x_count_back}")
#                    return "Right"
    else:
        x_count_back = 0

    if(y_accel < -1+y_accel_start):
        y_count = y_count + 1
        if(y_count > 3):
            change = True
            print(f"Moving y forward {y_count}")
#                    return "Forward"
    else:
        y_count = 0
        
    if(y_accel > y_accel_start+1):
        y_count_back = y_count_back + 1
        if(y_count_back > 3):
            change = True
            print(f"Moving y backwards {y_count_back}")
#                    return "Backwards"
    else:
        y_count_back = 0
        
    if(z_accel > 1+z_accel_start):
        z_count = z_count + 1
        if(z_count > 3):
            change = True
            print(f"Moving z down {z_count}")
#                    return "I don't know"
    else:
        z_count = 0
        
    if(z_accel < z_accel_start-1):
        z_count_back = z_count_back + 1
        if(z_count_back > 3):
            change = True
            print(f"Moving z up {z_count_back}")
#                    return "I don't know"
    else:
        z_count_back = 0
        
    if change:
        print("")
    time.sleep(0.2)
#        return "Hello, world! I am calling from imutest.py"
