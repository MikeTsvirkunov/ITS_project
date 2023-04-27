from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from json import loads

from keras.models import load_model

import tensorflow as tf
import numpy as np
import spacy

from Objects.Analysers.Functions.get_word_pairs import get_wp_in_line_hard
import pandas as pd

nlp_type_of_event_extraction = spacy.load('../../PipeLines/WordsExtraction/words_extract/')
nlp_classic = spacy.load('ru_core_news_sm')
kcm_extraction_model = tf.keras.models.load_model(
    '../../PipeLines/Coder/coder_from_spacy_to_kcm_onh5.h5')
# kcm_extraction_model.evaluate
is_description_model = load_model('../../PipeLines/Classifications/checker_is_discriptor_spacy_vectorize.h5')
def get_vectorized_wp_and_wp(text, vectorizer):
    list_of_wp = list()
    list_of_vectors = list()
    for sentence in text.split('.'):
        for wp in get_wp_in_line_hard(sentence):
            list_of_vectors.append(vectorizer(wp))
            list_of_wp.append(wp)
    return np.array(list_of_wp), np.array(list_of_vectors)


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

@app.get('/')
def home():
    return {"key": "Hello"}


@app.post('/students_event_description/')
def sendStudentJson(description=Body()):
    results = dict()
    results['id'] = description['id']
    types_of_events = list(map(str, nlp_type_of_event_extraction(description['name_of_event']).ents))
    results['types_of_events'] = types_of_events
    wp_of_event, wp_of_event_vectorized = get_vectorized_wp_and_wp(description['event_description'], lambda text: nlp_classic(text).vector)
    is_wp_descriptor = is_description_model.predict(wp_of_event_vectorized) > 0.992
    # print(is_wp_descriptor)
    descriptors_vectorized = wp_of_event_vectorized[is_wp_descriptor.T[0]]
    descriptors_name = wp_of_event[is_wp_descriptor.T[0]]
    # print(descriptors_name)
    predict = kcm_extraction_model.predict(descriptors_vectorized) 
    skills = dict()
    for name, kcm in zip(descriptors_name, predict):
        skills[name] = {'know': float((kcm[1]+1)/2), 'can': float((kcm[2]+1)/2), 'master': float((kcm[0]+1)/2)}
    
    results['skills'] = skills


    # mod_descr = np.array([nlp_classic(description['descriptor']).vector])
    
    # predicted = list(kcm_extraction_model.predict(mod_descr)[0])
    # print(predicted[1])
    # results['skills'] = {description['descriptor']: {'know': float(
    #     predicted[1]), 'can': float(predicted[2]), 'master': float(predicted[0])}}

    return results

# # перплексия
# # жокара
# # metrics learning

