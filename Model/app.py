from statistics import variance
import uvicorn
from fastapi import FastAPI

import numpy as np
import pandas as pd
from BankNotes import BankNote
import pickle


app=FastAPI()
pickle_in=open("classifier.pkl","rb")

classifier= pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/name')
def get_name(name:str):
    return {'message':f'Hello, {name}'}

@app.post('predict')
def predict_banknote(data:BankNote): # data is a temporary variable  that capture the POST input that we are giving 
    data=data.dict()
    print(data)
    print("Hello okok")
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload