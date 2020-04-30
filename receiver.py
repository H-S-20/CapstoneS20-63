import paho.mqtt.client as mqtt
from tkinter import *
#import time
from pynput.keyboard import Key, Controller

pref1 = None
pref2 = None
pref3 = None
pref4 = None
pref5 = None
pref6 = None

def update_preferences():
    global pref1
    global pref2
    global pref3
    global pref4
    global pref5
    global pref6
#updates preference input number 1
    if options1.get() == "default":
        pref1 = Key.media_volume_up
    elif options1.get() == "left":
        pref1 = Key.left
    elif options1.get() == "right":
        pref1 = Key.right
    elif options1.get() == "b":
        pref1 = 'b'
    elif options1.get() == "w":
        pref1 = 'w'
    elif options1.get() == "a":
        pref1 = 'a'
    elif options1.get() == "s":
        pref1 = 's'
    elif options1.get() == "volume up":
        pref1 = Key.media_volume_up
    elif options1.get() == "volume down":
        pref1 = Key.media_volume_down
#updates preference input number 2
    if options2.get() == "default":
        pref2 = Key.media_volume_down
    elif options2.get() == "left":
        pref2 = Key.left
    elif options2.get() == "right":
        pref2 = Key.right
    elif options2.get() == "b":
        pref2 = 'b'
    elif options2.get() == "w":
        pref2 = 'w'
    elif options2.get() == "a":
        pref2 = 'a'
    elif options2.get() == "s":
        pref2 = 's'
    elif options2.get() == "volume up":
        pref2 = Key.media_volume_up
    elif options2.get() == "volume down":
        pref2 = Key.media_volume_down
#updates prefernce input number 3
    if options3.get() == "default":
        pref3 = "0"
    elif options3.get() == "left":
        pref3 = "1"
    elif options3.get() == "right":
        pref3 = "2"
    elif options3.get() == "b":
        pref3 = "3"
    elif options3.get() == "w":
        pref3 = "4"
    elif options3.get() == "a":
        pref3 = "5"
    elif options3.get() == "s":
        pref3 = "6"
    elif options3.get() == "volume up":
        pref3 = "7"
    elif options3.get() == "volume down":
        pref3 = "8"
#updates preference input number 4
    if options4.get() == "default":
        pref4 = "0"
    elif options4.get() == "left":
        pref4 = "1"
    elif options4.get() == "right":
        pref4 = "2"
    elif options4.get() == "b":
        pref4 = "3"
    elif options4.get() == "w":
        pref4 = "4"
    elif options4.get() == "a":
        pref4 = "5"
    elif options4.get() == "s":
        pref4 = "6"
    elif options4.get() == "volume up":
        pref4 = "7"
    elif options4.get() == "volume down":
        pref4 = "8"
#updates preference input number 5
    if options5.get() == "default":
        pref5 = Key.left
    elif options5.get() == "left":
        pref5 = Key.left
    elif options5.get() == "right":
        pref5 = Key.right
    elif options5.get() == "b":
        pref5 = 'b'
    elif options5.get() == "w":
        pref5 = 'w'
    elif options5.get() == "a":
        pref5 = 'a'
    elif options5.get() == "s":
        pref5 = 's'
    elif options5.get() == "volume up":
        pref5 = Key.media_volume_up
    elif options5.get() == "volume down":
        pref5 = Key.media_volume_down
#updates preference input number 6
    if options6.get() == "default":
        pref6 = Key.right
    elif options6.get() == "left":
        pref6 = Key.left
    elif options6.get() == "right":
        pref6 = Key.right
    elif options6.get() == "b":
        pref6 = 'b'
    elif options6.get() == "w":
        pref6 = 'w'
    elif options6.get() == "a":
        pref6 = 'a'
    elif options6.get() == "s":
        pref6 = 's'
    elif options6.get() == "volume up":
        pref6 = Key.media_volume_up
    elif options6.get() == "volume down":
        pref6 = Key.media_volume_down
    


root = Tk()
root.title("H. A. N. D.")
root.geometry("400x500")

#This section is for all of the text and desired bindings

text1 = Label(root, text = "Palm Forward - Moving Forward")
text1.pack()
options1 = StringVar()
options1.set("default")
binding1 = OptionMenu(root, options1, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding1.pack()

text2 = Label(root, text = "Palm Forward - Moving Backwards")
text2.pack()
options2 = StringVar()
options2.set("default")
binding2 = OptionMenu(root, options2, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding2.pack()

text3 = Label(root, text = "Palm Left - Moving Forward")
text3.pack()
options3 = StringVar()
options3.set("default")
binding3 = OptionMenu(root, options3, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding3.pack()

text4 = Label(root, text = "Palm Left - Moving Backwards")
text4.pack()
options4 = StringVar()
options4.set("default")
binding4 = OptionMenu(root, options4, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding4.pack()

text5 = Label(root, text = "Palm Right - Moving Forward")
text5.pack()
options5 = StringVar()
options5.set("default")
binding5 = OptionMenu(root, options5, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding5.pack()

text6 = Label(root, text = "Palm Right - Moving Backwards")
text6.pack()
options6 = StringVar()
options6.set("default")
binding6 = OptionMenu(root, options6, "default", "left", "right", "b", "w", "a", "s", "volume up", "volume down")
binding6.pack()

setBindings = Button(root, text = "Apply Changes", command = update_preferences)
setBindings.pack()

startButton = Button(root, text = "Start")
startButton.pack()

stopButton = Button(root, text = "Stop")
stopButton.pack()



MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
keyboard = Controller()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    update_preferences()
    #msg.topic+" "+
    print(str(msg.payload))
    print(options6.get())
    print(pref6)
    print()
    if str(msg.payload) == "b'palm_right backwards'":
        keyboard.press(pref6)
        keyboard.release(pref6)

    if str(msg.payload) == "b'palm_right forward'":
        keyboard.press(pref5)
        keyboard.release(pref5)

    if str(msg.payload) == "b'palm_forwards backwards'":
        keyboard.press(pref2)
        keyboard.release(pref2)

    if str(msg.payload) == "b'palm_forwards forward'":
        keyboard.press(pref1)
        keyboard.release(pref1)
        #keyboard.release(Key.menu)
        #keyboard.release(Key.up)
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()
root.mainloop()