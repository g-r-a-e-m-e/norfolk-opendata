#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
app.py

This is the Streamlit app to explore and analyze city employee data from 
https://data.norfolk.gov

Created on Tue May  2 16:40:13 2023

@author: https://github.com/g-r-a-e-m-e
"""

# Import packages
import pandas as pd
import plotly.express as px
import streamlit as st
from pipeline import pull_data

##### Helper functions #####

# refresh_data will pull current data available from https://data.norfolk.gov
def refresh_data(refresh = False):
    if refresh == True:
        pull_data()

##### Create Pandas DataFrames from /data #####
census_df = pd.read_csv('data/census.csv')
demographics_df = pd.read_csv('data/demographics.csv')
salaries_df = pd.read_csv('data/salaries.csv') 

##### Create Plotly figures #####

avg_salary_by_dept_div = salaries_df.groupby(['department', 'division'])['annual_base_rate'].agg('mean').reset_index()
avg_salary_by_dept_div_violin = px.violin(data_frame = avg_salary_by_dept_div,
                                          x = 'department',
                                          y = 'annual_base_rate',
                                          )

##### Streamlit configuration #####
st.title('City of Norfolk Employee Data')

st.plotly_chart(avg_salary_by_dept_div_violin)