import spacy

def find_entities(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak on April 1, 1976. It is headquartered in Cupertino, California."

    entities = find_entities(text)
    print(entities)
