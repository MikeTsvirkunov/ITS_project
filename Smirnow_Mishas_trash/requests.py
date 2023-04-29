from fastapi import FastAPI, Body, status
import uvicorn
from model import request_body
from model import clf
from model import iris

app = FastAPI()


# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to predict!'}


@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to GeeksforGeeks!, {name}'}
#Endpoint
@app.post('/predict')
def predict(data : request_body):
    test_data = [[
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
    ]]
    class_idx = clf.predict(test_data)[0]
    return { 'class' : iris.target_names[class_idx]}