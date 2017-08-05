import paho.mqtt.client as mqtt

broker_address = '172.16.123.84'

client = mqtt.Client("P1")
client.connect(broker_address)
client.publish('station', 'OFF')
