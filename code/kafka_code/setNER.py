#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Based on "setSentiment": Created on Wed Jan  2 13:36:41 2019  @author: Daniel Molinari Hernández

setNER v1:

Created on Jan 25 2019 
@author Federico Montes de Oca R.
"""

import repustate
import os
import json
import sys
from confluent_kafka import Producer
from confluent_kafka import Consumer, KafkaException, KafkaError
import paralleldots
from paralleldots import sentiment
import time
import numpy as np
import unidecode

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import logging #Logging is a means of tracking events that happen when some software runs. 

#Config Logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='entidades_nombradas.log',level=logging.INFO) # logging to a file (store in a file the logs)

#client = repustate.Client(api_key='892c9ecdfa01cd3ede441a0b230c99c048d5ab09')

#paralleldots.set_api_key('hEY9UtdhxyOavixDFcAGPbOQn5x4rwo3GnMaEvUUw8I') 

#Call NER model 
from ner_test_parser import Parser
from nltk import sent_tokenize
p_a=Parser()
p_a.load_models("model_data/")

#broker = 'kafka:29092'
broker = 'localhost:9092' # definir , el broker será al que el producer enviara y de donde el consumer "consumira" 
#consumer toppic
consumer_topic = ['raw']  
#producer topic 
producer_topic = 'ner' 
#consumer group 
groupid = 'ner' 

# define the consumer configuration
confProducer = {
    'bootstrap.servers': broker,
    'queue.buffering.max.messages': 10000,
    'queue.buffering.max.ms': 500,
    'batch.num.messages': 100,
    'default.topic.config': {'acks': 1} # acknowledment from the leader only, may result in data loss if the leader is down 
}

# define the producer configuration
confConsumer = {
    'bootstrap.servers': broker,
    'group.id': groupid, 'session.timeout.ms': 6000,
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
}

#define producer
p = Producer(confProducer)
# define consumer
c = Consumer(confConsumer)
# start consumer to subscribe to a topic
c.subscribe(consumer_topic)

def entidades(textoa):
    token_sent = sent_tokenize(textoa)
    outlist=[]
    for t in token_sent:
        t = unidecode.unidecode(t)
        outlist.append(p_a.predict(t))
    to_out =[]
    for s in outlist:
        for w in s:
            if ('O') not in w:
                to_out.append(w)
    return to_out        

# Kafka Reports
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def main():
    # Read messages from Kafka
    logging.info('Inicio  de  reconocimiento de entidades nombradas (NER) .')
    i = 1
    try:
        while True:
            msg = c.poll(10)
            if msg is None:
                logging.info('No messages.... yet')
                continue
            if msg.error():
                try:
                    logging.error('Raise error.')
                except:
                    continue
                    #raise KafkaException(msg.error())
            else:
                # Proper message

                message = json.loads(msg.value().decode('UTF-8')) #read message from c
               
                logging.info('envio:') # guardar el mensaje enviado (solo el body) en los logs 
                mensaje_n = message['body']
                logging.info(mensaje_n)


                if(i>20):
                    i = 1
                    print('-- Sleeeping --')
                    time.sleep(55)
                i += 1
                res_ner = entidades(mensaje_n)
                logging.info('ner obtenido: ')
                logging.info(res_ner)
                message['ner'] = res_ner
                jd = json.dumps(message)  
				# eg: 
				#   >>> a = {'foo': 3}
				#	>>> json.dumps(a)
				#	   '{"foo": 3}'

                try:
                    p.poll(0)
                    p.produce(producer_topic, value=jd, key=msg.key(),callback=delivery_report) # produce the messege with the "sentiment", the messege will be store in the broker under the producer_topic
                    # producer.produce(producer_topic, message.value, callback=delivery_report)
                except BufferError:
                    print('ERROR')

    except KafkaException as e:
        logging.error(e)
        logging.error('Kafka interrupt.')

    except KeyboardInterrupt:
        logging.error('Keyboard interrupt.')
        print('ERROR')

    finally:
        logging.info('Cerrando los procesos')

        c.close()
        p.flush()

if __name__ == "__main__":
    main()
