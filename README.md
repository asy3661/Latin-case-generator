# Latin Case predictor

This repository contains a character-based LSTM language model used to see how well the model can predict Latin case endings. The data is formatted in a column where the first word is a preposition and the second word is a noun. Latin prepositions select for nouns in certain cases, and the form of the case is dependent on the declension of the noun, so ideally the model would be able to learn two primary aspects about the data:

- The selected case given a particular preposition (some prepositions select multiple cases)
- the correct case form given a particular case and declension

Much of the model was taken directly from [Aladdin Persson's](https://github.com/aladdinpersson) [Github repository](https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Projects/text_generation_babynames) for generating baby names.

The data came from the [CLTK Tesserae Latin Corpus](https://github.com/cltk/lat_text_tesserae), and was parsed with [CLTK](https://github.com/cltk/cltk) to find examples of adjacent preposition and noun pairs.
