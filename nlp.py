import spacy
import pytextrank


nlp = None


def load_spacy_model():
    global nlp
    if nlp:
        return nlp
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    return nlp


def get_keywords(text):
    nlp = load_spacy_model()
    doc = nlp(text)
    keywords = []
    for phrase in doc._.phrases:
        keywords.append(phrase.text)
    return keywords


def get_top_ranked_phrases(text):
    nlp = load_spacy_model()
    doc = nlp(text)
    phrases = []
    for phrase in doc._.phrases:
        phrases.append((phrase.text, phrase.rank, phrase.count))
    return phrases


if __name__ == "__main__":
    # example text
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."

    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    nlp.add_pipe("textrank")
    doc = nlp(text)

    # examine the top-ranked phrases in the document
    for phrase in doc._.phrases:
        print(phrase.text)
        print(phrase.rank, phrase.count)
        print(phrase.chunks)
