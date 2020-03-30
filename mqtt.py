import paho.mqtt.client as mqtt
 
MQTT_SERVER = "192.168.1.11"
MQTT_PATH = "test_channel"

client = mqtt.Client()
client.connect(MQTT_SERVER)
client.publish("Hello World!","OFF")
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)