from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from json import loads

from keras.models import load_model

import tensorflow as tf
import numpy as np
import spacy
from scipy.spatial.distance import cosine

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
    for sentence in filter(lambda a: len(a.split(' ')) > 2, description['event_description'].split('.')[:-1]):
        wp_of_event = np.array(get_wp_in_line_hard(sentence))
        wp_of_event_vectorized = get_vectorized_wp(word_pairs=wp_of_event, vectorizer=lambda text: nlp_classic(str(text)).vector)
        is_wp_descriptor = is_description_model.predict(wp_of_event_vectorized) > 0.992
        descriptors_name = np.array([remove_proper_names(str(d)) for d in wp_of_event[is_wp_descriptor.T[0]]])
        descriptors_vectorized = get_vectorized_wp(word_pairs=descriptors_name, vectorizer=lambda text: nlp_classic(str(text)).vector)
        if len(descriptors_name) != 0:
            print('res:\n', descriptors_name)
            distances = np.argsort(list(map(lambda a: np.array(a).mean(), 
                                            get_distances_between_wp(descriptor_vector=descriptors_vectorized, 
                                                                     metric_function=cosine))))
            predict = kcm_extraction_model.predict([descriptors_vectorized[distances[0:2]]])
            for name, kcm in zip(descriptors_name[distances[0:5]], predict):
                skills[name] = {'know': float((kcm[1]+1)/2), 'can': float((kcm[2]+1)/2), 'master': float((kcm[0]+1)/2)}
        
    results['skills'] = skills
    return results


