"""Define Advisor class to predict strains from user input"""

import basilica
from joblib import load
import numpy as np 
import os 

class Advisor(): 
    """generate five strains to advise from user input"""
    def __init__(self): 
        self.scaler = load('pickles/scaler.pkl')
        self.pca = load('pickles/pca.pkl')
        self.normalizer = load('pickles/normalizer.pkl')
        self.nn = load('pickles/nnmodel.pkl')
        self.API_KEY = os.getenv('API_KEY')

    def strain_advisor(self, input, neighbors=5):
        """embed input from user and return strains"""
        with basilica.Connection(self.API_KEY) as c:
            embedded_sentence = c.embed_sentence(input)
        
        embedded = np.stack([embedded_sentence], axis=0)
        scaled = self.scaler.transform(embedded)
        pca = self.pca.transform(scaled)
        normalized = self.normalizer.transform(pca)

        results = self.nn.kneighbors(normalized, neighbors)[1][0].tolist()

        return results