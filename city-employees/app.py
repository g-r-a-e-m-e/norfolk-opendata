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
from transform import transform_all

##### Helper functions #####

# refresh_data will pull current data available from https://data.norfolk.gov
def refresh_data(refresh = False):
    if refresh == True:
        transform_all()


##### Create Pandas DataFrames from /data #####
census_df = pd.read_csv('data/census.csv')
demographics_df = pd.read_csv('data/demographics.csv')
salaries_df = pd.read_csv('data/salaries.csv') 




## TO-DO: Need primary key to perform 1:1 join.

med_salary_by_dept_div_pos = salaries_df.groupby(['department', 'division', 'job_title'])['annual_salary'].agg('median').reset_index()

xref_df = demographics_df.merge(med_salary_by_dept_div_pos,
                                left_on = ['department', 'division', 'position_title'],
                                right_on = ['department', 'division', 'job_title'],
                                how = 'inner',
                                suffixes = ['_demo', '_sal'])


##### Create Plotly figures #####

med_salary_by_dept = salaries_df.groupby('department')['annual_salary'].agg('median').reset_index()
med_salary_by_dept_bar = px.bar(data_frame = med_salary_by_dept,
                                   y = 'department',
                                   x = 'annual_salary',
                                   labels = {'department' : 'Department',
                                             'annual_salary' : 'Annual Salary ($)'},
                                   title = 'Median Annual Salary by Department')

salary_dist = px.histogram(salaries_df,
                           x = 'annual_salary',
                           labels = {'annual_salary': 'Annual Salary ($)',
                                     'count' : 'Number of Employees'}, 
                           title = 'Annual Salary Distribution',
                           nbins = 60)
                           
                           
salary_vs_tenure_scatter = px.scatter(xref_df,
                                      x = 'tenure',
                                      y = 'annual_salary', 
                                      labels = {'tenure' : 'Employee Tenure (years)',
                                                'annual_salary' : 'Median Annual Salary ($)'},
                                      title = 'Median Annual Salary vs. Employee Tenure',
                                      color = 'ethnicity')


##### Streamlit configuration #####

st.title('City of Norfolk Employee Data')

tabs = ['Median Salary by Department', 'Salary Distribution', 'Median Salary vs. Tenure']

tab_1, tab_2, tab_3 = st.tabs(tabs)
tab_1.plotly_chart(med_salary_by_dept_bar)
tab_2.plotly_chart(salary_dist)
tab_3.plotly_chart(salary_vs_tenure_scatter)