from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from json import loads

from keras.models import load_model

import spacy

from Objects.Analysers.Functions.get_word_pairs import get_wp_in_line_hard


nlp_type_of_event_extraction = spacy.load('../../PipeLines/WordsExtraction/words_extract/')
nlp_classic = spacy.load('ru_core_news_sm')
kcm_extraction_model = load_model('../../PipeLines/Coder/coder_from_spacy_to_kcm__01_04_2023')
# is_description_model = load_model('../../PipeLines/Classification/check_is_descriptor')


def vectorize_word_paires():
    pass


def get_skills(vectorised_words):
    pass


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
    # description = loads(json_description)
    results = dict()
    results['id'] = description['id']
    types_of_events = list(map(str, nlp_type_of_event_extraction(description['name_of_event']).ents))
    # skills = 
    results['types_of_events'] = types_of_events
    predicted = (kcm_extraction_model.predict(nlp_classic(description['descriptor']).vector)[0] + 1) / 2
    results['skills'] = {'know': predicted[1],
                         'can': predicted[2], 
                         'master': predicted[0]}
    # print(len(types_of_events), types_of_events[0])

    return results

