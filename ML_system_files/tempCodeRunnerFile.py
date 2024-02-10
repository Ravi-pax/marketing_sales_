# import packages
import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

##
model_path = r'model3.pkl'

with open(model_path,'rb') as model_file:
    loaded_model = pickle.load(model_file)

