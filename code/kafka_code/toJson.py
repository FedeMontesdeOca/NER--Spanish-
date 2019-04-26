from confluent_kafka import Consumer, KafkaError
import json
import sys
broker = 'localhost:9092' # definir , el broker será al que el producer enviara y de donde el consumer "consumira"
#consumer toppic
consumer_topic = ['ner']
#consumer group
groupid = 'ner'


c = Consumer({
    'bootstrap.servers': broker,
    'group.id': groupid,
    'auto.offset.reset': 'earliest'
})

c.subscribe(consumer_topic)

while True:
    msg = c.poll(10)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    with open('out_put_noticia.json','w') as json_file:
        json.dump(msg.value().decode('utf-8'),json_file)
    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()
