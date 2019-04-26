# Bitacora de versiones: 

v0: 

-Implementación del set de datos para NER en español CoNLL 2002.

- Accuracy: ~79

- 100 epoch / 55 min aprox   

v1:

- Se probó con diferentes implementaciones modificando el uso del español en CoNLL 2002, se probó:
   1. Remoción de caracteres especiales propios del idioma (ej: acentos). 
   2. Cambiar todas las palabras a minúsculas.
   3. Remoción de los signos de puntuación. 
  Se probaron todas las combinaciones posibles, el mejor resultado fue: Unicamente la remoción de caracteres especiales.

- Tiene un accuracy :~80 el cuál es poco mayor que la v0.

- Entrenamiento: 100 Epoch/ 1hr 

- El accuracy subió muy poco en 50 epoch. 


v2: 

- Se implementa las word embeddings en español: 
   GloVe embeddings for SWBC; #dimensions=300, #vectors=855380.

- Se probó con diferentes implementaciones utilizando como referencia los resultados obtenidos en v1. 
  1. Se implemento la remoción de caracteres especiales solo a CoNLL 2002
  2. Se implemento la remoción de caracteres especiales tanto a CoNLL 2002 como a GloVE SWBC.
  3. Se implemento sin ningún trato especial al idioma. 
  La implementación 3 fue la que tuvo mejor accuracy. 

- Se probó de igual forma el modificar el optimizer para utilizar el mismo que en (Chiu & Nichols, 2016). 
  Se cambio el "nadam" por "sgd" obteniendo resultados muy por debajo de los anteriores, con apenas un accuracy de 20 se descarta. 

- Se modifico y mejoró el preprocesamiento de los datos de entrada para predicción. Ahora puede predecir las etiquetas I-(PER/LOC/ORG/MISC)

- v2.1 : Corrección de error en el output. 

-Para 50 epoch:
  + Tiene un accuracy :~80 
  + Tiempo: 38 min aprox.  

-Para 100 epoch: 
  + Tiene un accuracy :~84
  + Tiempo: 1 hr 20 min aprox. 
- Para 150 epoch:
  + accuracy ~85.1
<<<<<<< HEAD
  + Tiempo: 2 hrs 


- v2.2 : 
	Se implementa el set de noticias Milenio para el entrenamiento. El set fue obteniendo 
	ulizando el corpus de noticias proveido por Rich It. El set fue etiquetado utilizando 
	spaCy (es_core_news_md https://spacy.io/models/es ).
	El set Milenio puede ser encontrado en el share drive de la empresa dentro de la carpeta tidy_data. 
	Se elimino la puntuación 
	
	Utlizando : 1% del dataset:
	
	+Tiempo: 1 hr 
	+Test-Data: Prec: 0.461, Rec: 0.501, F1: 0.480
	+Dev-Data: Prec: 0.445, Rec: 0.486, F1: 0.464
	
	Utilizando : 5% del dataset:
	Test-Data: Prec: 0.471, Rec: 0.496, F1: 0.483
	Dev-Data: Prec: 0.477, Rec: 0.506, F1: 0.491
	
-Sobre los sets de datos utlizados para español-

Word embeddings:

GloVe embeddings from SBWC
Embeddings
Links to the embeddings (#dimensions=300, #vectors=855380):

Vector format (.vec.gz) (906 MB)
Binary format (.bin) (3.9 GB)
Algorithm
Implementation: GloVe
Parameters:
vector-size = 300
iter = 25
min-count = 5
all other parameters set as default
Corpus
Spanish Billion Word Corpus (see above)

https://github.com/uchile-nlp/spanish-word-embeddings

Dataset (training/test/dev): 

CoNLL 2002

https://github.com/teropa/nlp/tree/master/resources/corpora/conll2002 