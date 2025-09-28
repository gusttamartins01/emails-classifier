import spacy

nlp = spacy.load("pt_core_news_sm")

def preprocess_text(texto: str) -> str:
    if not texto or not isinstance(texto, str):
        return ""

    doc = nlp(texto.lower().strip())

    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
        and not token.like_num
        and token.is_alpha
    ]

    return " ".join(tokens)