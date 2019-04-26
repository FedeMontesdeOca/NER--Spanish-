toKafka v1.0:
 	- Manda noticias en formato json del set de noticias a kafka.
	- producer topic: 'ner' 


setNER v1.0: 
	-  Agarra las noticias enviadas por toKafka y aplica una tarea de reconocimento de entidades. 
	- Utiliza el modelo previamente entrenado. Se modifico el archivo ner_test_parser (en la lectura de word2Index y idx2Label) para poder ser utlizado dentro de kafka.
	-  producer topic: 'ner' ; consumer topic: 'raw'; groupid: 'ner'

toJson v1.0:
	- Las noticias que son consumidas por el consumer son almacenadas dentro de un json. 

ner_test_parser v2.0
	- Se modifico la lectura del word2Index y idx2Label, se añade la allow_pickle=True.