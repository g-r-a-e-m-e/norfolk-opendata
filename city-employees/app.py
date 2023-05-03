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
import transform

##### Helper functions #####

# refresh_data will pull current data available from https://data.norfolk.gov
def refresh_data(refresh = False):
    if refresh == True:
        transform

##### Create Pandas DataFrames from /data #####
census_df = pd.read_csv('data/census.csv')
demographics_df = pd.read_csv('data/demographics.csv')
salaries_df = pd.read_csv('data/salaries.csv') 

##### Create Plotly figures #####

med_salary_by_dept = salaries_df.groupby('department')['annual_salary'].agg('median').reset_index()
med_salary_by_dept_bar = px.bar(data_frame = med_salary_by_dept,
                                   y = 'department',
                                   x = 'annual_salary',
                                   labels = {'department' : 'Department',
                                             'annual_salary' : 'Annual Salary ($)'},
                                   title = 'Median Annual Salary by Department')

salary_dist = px.histogram(data_frame = salaries_df,
                           x = 'annual_salary',
                           labels = {'annual_salary': 'Annual Salary ($)',
                                     'count' : 'Number of Employees'}, 
                           title = 'Annual Salary Distribution',
                           nbins = 60)
                           
                           

##### Streamlit configuration #####
st.title('City of Norfolk Employee Data')

tab_1, tab_2 = st.tabs(['Median Salary by Department', 'Salary Distribution'])
tab_1.plotly_chart(med_salary_by_dept_bar)
tab_2.plotly_chart(salary_dist)