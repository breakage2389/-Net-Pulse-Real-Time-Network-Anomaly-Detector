from sklearn.ensemble import IsolationForest
import pandas as pd

model = IsolationForest(contamination=0.05 , random_state=42)

def train_model(training_data):
    model.fit(training_data[['size' , 'protocol']])
    print('Brain has been trained on normal traffic.')

def predict_model(training_data):
    prediction = model.predict(training_data[['size' , 'protocol']])
    return prediction[0]