import MQTTKeywords


mqtt = MQTTKeywords.MQTTKeywords()
mqtt.connect('127.0.0.1')
print(mqtt.subscribe('test', qos=0, timeout=0))

messages = mqtt.listen('test', timeout=30, limit=5)
print(messages)
mqtt.disconnect()