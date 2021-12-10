# Latin Case predictor

This repository contains a character-based LSTM language model used to see how well the model can generate Latin case endings, depending on several factors. The data is formatted in a column where the first word is a preposition and the second word is a noun. Latin prepositions select for nouns in certain cases, and the form of the case is dependent on the declension of the noun, so ideally the model would be able to learn two primary aspects about the data:

- The selected case given a particular preposition (some prepositions select multiple cases)
- the correct suffix form given a particular case and declension

Much of the model was taken directly from [Aladdin Persson's](https://github.com/aladdinpersson) [Github repository](https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Projects/text_generation_babynames) for generating baby names.

The data came from the [CLTK Tesserae Latin Corpus](https://github.com/cltk/lat_text_tesserae), and was parsed with [CLTK](https://github.com/cltk/cltk) to find examples of adjacent preposition and noun pairs.

## Architecture

This model has two layers of LSTMs with 256 hidden nodes and is trained with Adam.

## Methods

The neural network can be accessed with the Generator class of model.py. There is a pretrained model in the repo, `case_predictor.pt`, which can be loaded with the `Generator.load_model` function. To test the model, there are the following methods:

- `Generator.generate`: this will produce strings of *n* length, including whitespace. It emulates the `data/data.txt` file.
- `Generator.complete_string`: this function will replicate one line from the `data/data.txt` file. For probing the current research question, it works best for the input to the function to be a string that has a latin preposition followed by a noun stem, e.g., *in insul*, for the word *in insula* 'on the island.'
- `Generator.estimate_prob_dist`: This runs `Generator.complete_string` 1000 times, counting each form that is produced and returning a `collections.Counter` object. This allows us to estimate the probability distribution of what forms will be outputted by the network.
- `Generator.random_prediction`: This function randomly chooses a preposition and feeds it into the `Generator.complete_string` function. This could be used to learn about frequencies of which nouns will be output.
