from cltk import NLP

def get_prep_n_pairs(text, language):
    """ This gets pairs of adjacent prepositions and nouns in a document, and
    gives both the form of the noun found in the document as well as the lemma
    form. This takes a text as a string, and outputs a tab separated string of
    preposition and noun pairs, where the lemma form is on the left of the tab
    and the attested form is on the right."""

    document = analyze_document(text, language)
    prep_noun_pairs = []
    i = 1
    while i < len(document.tokens):
        # The parts of speech have a particular POS type, so it's necessary to
        # cast them to a string for easy comparison
        if str(document[i-1].pos) == 'adposition' and str(document[i].pos) == 'noun':
            prep_noun_pairs.append(f'{document[i-1].lemma} {document[i].lemma}\t{document[i-1].string} {document[i].string}')
        i += 1
    return "\n".join(prep_noun_pairs)

def analyze_document(text, language):
    cltk_nlp = NLP(language=language)
    document = cltk_nlp.analyze(text=text)
    return document

