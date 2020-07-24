import paho.mqtt.publish as publish

def send(data,clientId,deviceId):
    topic = clientId + "/" + deviceId
    publish.single(topic, data, hostname="34.87.144.83")
    return("Succes")
