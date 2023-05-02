#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
app.py

This is the Streamlit app to explore and analyze City of Norfolk OpenData

Created on Tue May  2 16:40:13 2023

@author: https://github.com/g-r-a-e-m-e
"""

# Import packages
import pandas as pd
import plotly.express as px
import streamlit as st
from pipeline import pull_data

## Helper functions
#def refresh_data(refresh = False):
#    if refresh == True:
#        pull_data()

##### Streamlit configuration #####
st.title('City of Norfolk Employee Data')
