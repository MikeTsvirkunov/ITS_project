from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from json import loads

from keras.models import load_model

import tensorflow as tf
import numpy as np
import spacy
from scipy.spatial.distance import cosine
import re

from Objects.Functions.get_word_pairs import get_wp_in_line_hard, get_vectorized_wp_and_wp, get_vectorized_wp
from Objects.Functions.get_types_of_event import get_types_of_event_spacy
from Objects.Functions.get_wp_distances import get_distances_between_wp
from Levenshtein import distance
from Objects.Functions.remove_proper_names import remove_proper_names
# tf.config.run_functions_eagerly(True)


nlp_classic = spacy.load('ru_core_news_sm')
nlp_type_of_event_extraction = spacy.load('../../PipeLines/WordsExtraction/words_extract/')
kcm_extraction_model = load_model('../../PipeLines/Coder/coder_from_spacy_to_kcm_onh5.h5')
kcm_extraction_model.compile(run_eagerly=True)
is_description_model = load_model('../../PipeLines/Classifications/checker_is_discriptor_spacy_vectorize.h5')

sentence_confines = lambda a: len(a.split(' ')) > 2
sentence_separator = '\.|\?\!|\n'
excess_patterns = r'[\"\'«\(\[\{\\].*?[\"\'»\)\]\}\\]|\»|\,|\.|\:|\;|\'|\"'
classic_vectorizer = lambda text: nlp_classic(str(text)).vector
min_chance_of_be_descriptor = 0.9

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://localhost:8000/",
        "https://localhost:8080/",
        "https://91.185.86.61:8080/",
        "http://91.185.86.61:8080/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/students_event_description/')
def sendStudentJson(description=Body()):
    results = dict()
    results['id'] = description['id']
    types_of_events = get_types_of_event_spacy(name=description['name_of_event'], 
                                               nlp_with_type_ent=nlp_type_of_event_extraction)
    skills = dict()
    results['types_of_events'] = types_of_events
    sentences = re.split(sentence_separator, description['event_description'])
    for sentence in filter(sentence_confines, sentences):
        wp_of_event = np.array(get_wp_in_line_hard(sentence.replace('.', '')))
        wp_of_event_vectorized = get_vectorized_wp(word_pairs=wp_of_event, 
                                                   vectorizer=classic_vectorizer)
        is_wp_descriptor = is_description_model.predict(wp_of_event_vectorized) > min_chance_of_be_descriptor
        descriptors_name = np.array([re.sub(excess_patterns, '', str(d)) for d in wp_of_event[is_wp_descriptor.T[0]]])
        descriptors_vectorized = get_vectorized_wp(word_pairs=descriptors_name, 
                                                   vectorizer=lambda text: nlp_classic(str(text)).vector)
        if len(descriptors_name) != 0:
            distances = np.argsort(list(map(lambda a: np.array(a).mean(), 
                                            get_distances_between_wp(descriptor_vector=descriptors_vectorized, 
                                                                     metric_function=cosine))))
            predict = kcm_extraction_model.predict([descriptors_vectorized[distances[0:1]]])
            for name, kcm in zip(descriptors_name[distances[0:5]], predict):
                skills[name] = {'know': max(float(kcm[1]), 0), 
                                'can': max(float(kcm[2]), 0), 
                                'master': max(float(kcm[0]), 0)}
        
    results['skills'] = skills
    return results


