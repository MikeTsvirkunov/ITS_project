import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
tokens = nlp("dog cat banana afskfsd")
print(tokens)
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)