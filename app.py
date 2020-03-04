"""Code for The Intuitive Medical Marijuana App""" 

from flask import Flask, render_template, request, jsonify
from scipy import spatial
import basilica
import numpy as np
import pandas as pd
import pickle 

app = Flask(__name__)

@app.route('/')
def root(): 
    return 'Welcome to the Intuitive Medical Marijuana App!'

@app.route('/strains', methods=['Post'])
def strains():
    """route expects json object w/ one key"""

    # receive input
    lines = request.get_json(force=True)
    # get data from json
    text = lines['input'] #json key tbd
    # validate input (optional)
    assert isinstance(text, str)
    # predict
    output = predict(text)
    # output to sender
    return output

@app.route('/sympton', methods=['Post'])
def symptom():
    """route expects json objext w/ one key"""
    
    # receive input
    lines = request.get_json(force=True)
    # get data from json
    text = lines['input'] #json key tbd
    # validate input (optional)
    assert isinstance(text, str)
    # predict
    output = predict_symptons(text)
    # output to sender
    return output

@app.route('/general', methods=['Post'])
def general():
    """route expects json object w/ one key"""
    
    # receive input
    lines = request.get_json(force=True)
    # get data from json
    text = lines['input'] #json key tbd
    # validate input (optional)
    assert isinstance(text, str)
    # predict
    output = predict_all(text)
    # output to sender
    return output

###User Input###

user_input_symp = ''

def predict_symptons(user_input_symp):
    
    # [TO FINISH w/ link] unpickling file of embedded data
    unpickled_df_test = pd.read_pickle('')
    # get data
    df = pd.read_csv('')

    # Objective 1: a function to calculate_user_text_embedding to save the embedding
    """saves embedding value in session memory"""
    user_input_embedding = 0

    def calculate_user_text_embedding(input, user_input_embedding):
        
        # string of two sentences to compare
        sentences = [input]
        # [TO FINISH w/ link] calculating embedding for both user_entered_text and for features
        with basilica.Connection('') as c:
            user_input_embedding = list(c.embed_sentences(sentences))
        
        return user_input_embedding
    
    # Objective 2: define score user input from embedding from stored values
    score = 0

    def score_user_input_from_embedding_from_stored_values(input, score, row1, user_input_embedding):
        # obtain pre-calculated valued from pickled dataframe of arrays
        embedding_stored = unpickled_df_test.loc[row1, 0]
        # calculate the similarity of user_text vs product description
        score = 1 - spatial.distance.cosine(embedding_stored, user_input_embedding)
        # return a variable that can be used outside of the function
        return score
    
    # Objective 3: call function to set the value of 'score' which is the score of the user input
    for i in range(2351):
        score = score_user_input_from_embedding_from_stored_values(user_input_symp, score, i, user_input_embedding)
        # store score in df
        df.loc[i, 'score'] = score
    
    # Objective 4: return all data for the top five results as a json obj

    # Objective 5: output
    
