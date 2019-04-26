# Named-Entity-Recognition-with-Bidirectional-LSTM-CNNs

Jupyter Notebook based on: **Kamal Raj** NER with Bidirectional LSTM-CNNs implementation available on Github. https://github.com/kamalkraj/Named-Entity-Recognition-with-Bidirectional-LSTM-CNNs.

Training done in:

    DESKTOP-0UQLV13
    Processor: Intel Core i7-6700HQ CPU 2.6GHz 
    RAM: 16GB
    OS: Windows 10 Home Single x64
    Memory type: SSD
	Python: 3.6.8


NER task can be formulated as: 

_Given a sequence of tokens (words, and may be punctuation symbols) provide a tag from predefined set of tags for each token in the sequence._

For NER task there are some common types of entities which essentially are tags:
- Persons
- Locations
- Organizations
- Expressions of time
- Quantities
- Monetary values 

Furthermore, to distinguish consequent entities with the same tags BIO tagging scheme is used. "B" stands for beginning, 
"I" stands for the continuation of an entity and "O" means the absence of entity. Example with dropped punctuation:

    Bernhard        B-PER
    Riemann         I-PER
    Carl            B-PER
    Friedrich       I-PER
    Gauss           I-PER
    and             O
    Leonhard        B-PER
    Euler           I-PER

In the example above PER means person tag, and "B-" and "I-" are prefixes identifying beginnings and continuations of the entities. Without such prefixes, it is impossible to separate Bernhard Riemann from Carl Friedrich Gauss.

