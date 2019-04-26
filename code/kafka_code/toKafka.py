# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:36:41 2019

@author: Daniel Molinari Hernández
"""

import json
import sys
from confluent_kafka import Producer

file_path = 'noticias/data1.jsonl' # path de los archivos json 
producer_topic = 'raw' # nombre del topico de kafka 
# Kafka Settings
p = Producer({'bootstrap.servers': 'localhost:9092'})

def array2string(texto):
	t1 = texto
	t3 = ''
	for t2 in t1:
		t3 = t3 + ' ' + t2
	return t3

def leejson(contenido):
	json1 = contenido
	json2 = {}
	if 'body' in json1:
		text1 = array2string(json1["body"])
		json2["body"] = text1.replace('\xa0', ' ')
	if 'description' in json1:
	 	json2["description"] = array2string(json1["description"])
	if 'author' in json1:
	 	json2["author"] = array2string(json1["author"])
	if 'url' in json1:
	 	json2["url"] = array2string(json1["url"])
	if 'section' in json1:
	 	json2["section"] = array2string(json1["section"])
	if 'title' in json1:
	 	json2["title"] = array2string(json1["title"])
	if 'datetime' in json1:
	 	json2["datetime"] = json1["datetime"]
	if 'source' in json1:
	 	json2["source"] = array2string(json1["source"])
	if 'remarks' in json1:
	 	json2["remarks"] = array2string(json1["remarks"])
	if 'location' in json1:
	 	json2["location"] = array2string(json1["location"])
	if 'keywords' in json1:
	 	json2["keywords"] = array2string(json1["keywords"])
	return json2

def delivery_callback(err, msg):
	if err:
		sys.stderr.write('%% Message failed delivery: %s\n' % err)
	else:
		sys.stderr.write('%% Message delivered to %s [%d] @ %o\n' % (msg.topic(), msg.partition(), msg.offset()))

# Kafka Reports
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def main():


	i = 1
	with open(file_path) as f:
	    for line in f:
	    	if(i > 20):
		        j_content = json.loads(line)
		        contenido = leejson(j_content)
		        jd = json.dumps(contenido)

		        try:
		        	p.poll(0)
		        	p.produce(producer_topic, jd, callback=delivery_report)
		        	print(str(i),".- contenido --> ", contenido)
		        except BufferError:
		        	print('Valio M---')

	    	i = i + 1
	    	if(i > 30):
	    		break
	p.flush()
if __name__ == "__main__":
   main()
