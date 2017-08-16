import paho.mqtt.client as mqtt

broker_address = '172.18.0.1'

client = mqtt.Client("P1")
client.connect(broker_address)
client.publish('station', 'OFF')
