import paho.mqtt.client as mqtt
from pynput.keyboard import Key, Controller, Listener

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
keyboard = Controller()

leftKey = Key.left
rightKey = Key.right
forwardKey = Key.media_volume_up
backwardsKey = Key.media_volume_down

def on_press(key):
    return(key)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #msg.topic+" "+
    print(str(msg.payload))
    if str(msg.payload) == "b'Left'":
        keyboard.press(leftKey)
        keyboard.release(leftKey)
    
    if str(msg.payload) == "b'Right'":
        keyboard.press(rightKey)
        keyboard.release(rightKey)
    
    if str(msg.payload) == "b'Backwards'":
        keyboard.press(backwardsKey)
        keyboard.release(backwardsKey)

    if str(msg.payload) == "b'Forward'":
        keyboard.press(forwardKey)
        keyboard.release(forwardKey)
        #keyboard.release(Key.menu)
        #keyboard.release(Key.up)
    # more callbacks, etc
    
answer = input("Do you wish to change the default key bindings? y/n :")
if answer = 'y':
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        print("Input the key to press when moving the controller left.\n")
        leftKey = on_press(key)
        print("Input the key to press when moving the controller right.\n")
        rightKey = on_press(key)
        print("Input the key to press when moving the controller forward.\n")
        forwardKey = on_press(key)
        print("Input the key to press when moving the controller back.\n")
        backwardsKey = on_press(key)
        listener.stop()
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
