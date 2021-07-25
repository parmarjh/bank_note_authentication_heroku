#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 00:06:11 2021

@author: ashishsapra
"""


import pandas as pd
import numpy as np
import pickle
import streamlit as st
#import flasgger
#from flasgger import Swagger

#app = Flask(__name__)
#Swagger(app)

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in) 

#@app.route('/')
def welcome():
    return "Welcome All"



def predict_note_authentication(variance, skewness, curtosis, entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
   
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction


def main():
    st.title("Bank Authentication")
    html_temp = """
    <div style="background-color:green:padding:10px"
    <h2 style="color:white;text-align:center;">Bank Authenticator ML app<h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type here")
    skewness = st.text_input("Skewness","Type here")
    curtosis = st.text_input("Curtosis","Type here")
    entropy = st.text_input("Entropy","Type here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.success('The Output is {}'.format(result))
    if st.button("About"):
        st.text("App build by Ashish Sapra")
        st.text("Contact on : ashish.sapra.28@gmail.com")




if __name__ == '__main__':
     main()