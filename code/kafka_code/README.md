# Confluent Kafka

Requisitos: 
1) Instalar y configurar Confluent plataform: https://docs.confluent.io/3.3.0/installation/installing_cp.html 
2) Instalar el modulo confluent-kafka-python: https://github.com/confluentinc/confluent-kafka-python *Nota: requiere el modulo: librdkafka 


Pasos:
a) Iniciar un servicio de confluent nuevo.
	* sugerencia, ejectutar " confluent destroy " para asegurarse de no tener nada anterior que pueda afectar.
	ejecutar: 
	>> confluent start 
	 para inciar una nuevo servicio de confluent.
b) Crear los topicos necesarios, en este caso "raw" y "ner". Ejecutar:
	>> sudo ./usr/bin/kafka-topics --create --zookeeper localhost:2181   \
--replication-factor 1 --partitions 1 --topic ner
 	>> sudo ./usr/bin/kafka-topics --create --zookeeper localhost:2181   \
--replication-factor 1 --partitions 1 --topic raw
c) ejecutar el archivo "toKafka.py" para mandar las noticias al kafka
d) ejecutar el archivo "setNER.py" para crear las NER 
e) *Opcional: ejecutar el archivo "toJson.py" para guardar los mensajes del consumer a json.

Ejecute:

1. confluent destroy
2. confluent start
3. sudo ./usr/bin/kafka-topics --create --zookeeper localhost:2181   \
--replication-factor 1 --partitions 1 --topic ner
4. sudo ./usr/bin/kafka-topics --create --zookeeper localhost:2181   \
--replication-factor 1 --partitions 1 --topic raw
5. sudo python3.6 toKafka.py
6. sudo python3.6 setNER.py
7. sudo python3.6 toJson.py