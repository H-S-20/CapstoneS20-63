import paho.mqtt.client as mqtt
from pynput.keyboard import Key, Controller

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
    #msg.topic+" "+
    print(str(msg.payload))
    if str(msg.payload) == "b'Left'":
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    
    if str(msg.payload) == "b'Right'":
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    
    if str(msg.payload) == "b'Backwards'":
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

    if str(msg.payload) == "b'Forward'":
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
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
client.loop_forever()