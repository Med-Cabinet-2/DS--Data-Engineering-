"""code for med cab app""" 

from flask import Flask, render_template, request, jsonify
import basilica
import numpy as np
import pandas as pd 
 

app = Flask(__name__)

@app.route('/')
def root(): 
    return 'Welcome to the Intuitive Med Cab App!'

@app.route('/strains', methods=['Post'])
def strains():
    """route expects json object w/ one key"""

    # recieve input
    # get data from json
    # validate input (optional)
    # predict
    # give output to sender

@app.route('/sympton', methods=['Post'])
def symptom():
    """route expects json objext w/ one key"""
    
    # recieve input
    # get data from json
    # validate input (optional)
    # predict
    # give output to sender

@app.route('/general', methods=['Post'])
def general():
    """route expects json object w/ one key"""
    
    # recieve input
    # get data from json
    # validate input (optional)
    # predict
    # give output to sender

# User Input
user_input_sym = ""

def predict_symptons(user_input_symp):
    # unpickling file of embedded data
    # getting data
