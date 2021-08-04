# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

import streamlit as st
from PIL import Image
image = Image.open('brain-illustration_208293872.jpg')
st.image(image, caption='Brain Volume Analysis')


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("Bclassifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Head_size_scaling,PGMV_normalised,PGMV,CSFV_normalised,CSFV,GMV_normalised,GMV,WMV_indexed,WMV,BrainV_normalised,BrainV,Gender):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Head_size_scaling
        in: query
        type: number
        required: true
      - name: PGMV_normalised
        in: query
        type: number
        required: true
      - name: PGMV
        in: query
        type: number
        required: true
      - name: CSFV_normalised
        in: query
        type: number
        required: true
      - name: CSFV
        in: query
        type: number
        required: true
      - name: GMV_normalised
        in: query
        type: number
        required: true
      - name: GMV
        in: query
        type: number
        required: true
      - name: WMV_indexed
        in: query
        type: number
        required: true
      - name: WMV
        in: query
        type: number
        required: true
      - name: BrainV_normalised
        in: query
        type: number
        required: true
      - name: BrainV
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Head_size_scaling,PGMV_normalised,PGMV,CSFV_normalised,CSFV,GMV_normalised,GMV,WMV_indexed,WMV,BrainV_normalised,BrainV,Gender]])
    print(prediction)
    return prediction



def main():
    st.title("COVID 19 Prediction Software (BRAIN VOLUME ANALYSIS)")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Check your COVID 19 status today </h2>
    </div>

    <div style="background-color:tomato;padding:10px">
    <h3 style="color:yellow;text-align:left;">Result: </h3>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h4 style="color:yellow;text-align:left;">1-You have COVID 19 </h4>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h5 style="color:yellow;text-align:left;">0-You are free from the VIRUS </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Head_size_scaling = st.text_input("Head_size_scaling","Type Here")
    PGMV_normalised = st.text_input("PGMV_normalised","Type Here")
    PGMV = st.text_input("PGMV","Type Here")
    CSFV_normalised = st.text_input("CSFV_normalised","Type Here")
    CSFV = st.text_input("CSFV","Type Here")
    GMV_normalised = st.text_input("GMV_normalised","Type Here")
    GMV = st.text_input("GMV","Type Here")
    WMV_indexed = st.text_input("WMV_indexed","Type Here")
    WMV = st.text_input("WMV","Type Here")
    BrainV_normalised = st.text_input("BrainV_normalised","Type Here")
    BrainV = st.text_input("BrainV","Type Here")
    Gender = st.text_input("Gender","input (1) for male and (0) for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Head_size_scaling,PGMV_normalised,PGMV,CSFV_normalised,CSFV,GMV_normalised,GMV,WMV_indexed,WMV,BrainV_normalised,BrainV,Gender)
    st.success('Your COVID 19 Chances {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by Henry")

if __name__=='__main__':
    main()
    
    
    