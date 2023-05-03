#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transform.py

This script performs data transformations on city employee data from 
https://data.norfolk.gov

Created on Wed May  3 10:17:05 2023

@author: https://github.com/g-r-a-e-m-e
"""

# Import packages
import datetime as dt
import pandas as pd
from pipeline import pull_data

# Functions to transform features in each DataFrame
def census_transform(data):
    # Census data are taken every 10 years.
    # Creating decadal_delta fields to compare values between each census
    data['decadal_delta_2020_vs_2010'] = data['census_2020'] - data['census_2010']
    data['decadal_delta_2000_vs_2000'] = data['census_2010'] - data['census_2000']
    
    # Print status
    print('\nCreating additional census features...\n')
    
    # Write to /data
    data.to_csv('data/census.csv')
    
    return print('\nDone!\n')


def demographics_transform(data):
    # Create current_year variable to create additional fields
    current_year = int(dt.datetime.now().strftime('%Y'))
    
    # Create tenure field to specify length of time with City of Norfolk
    data['tenure'] = data['startyear'].apply(lambda x: current_year - x)
    
    # Create age field to determine employee age
    data['age'] = data['birthyear'].apply(lambda x: current_year - x)
    
    # Print status
    print('\nCreating additional demographics features...\n')
    
    # Write to /data
    data.to_csv('data/demographics.csv')
    
    return print('\nDone!\n')


def salaries_transform(data):
    # Create start_year field from start_date
    data['start_year'] = data['start_date'].apply(lambda x: int(dt.datetime.fromisoformat(x).strftime('%Y')))
    
    # Some annual_base_rates are in hourly amounts
    # Create annual_salary from annual_base_rates < $250
    data['annual_salary'] = data['annual_base_rate'].apply(lambda x: x if (x > 250) else x * 40 * 52)
    
    # Create employee_status field from employee_classification
    def employee_status(record):
        # FT - Full-time
        if 'FULL-TIME' in record.upper():
            emp_stat = 'FT'
        # PT - Part-time
        elif 'PART-TIME' in record.upper():
            emp_stat = 'PT'
        # RET - Retirement
        elif 'RETIRE' in record.upper():
            emp_stat = 'RET'
        # TEMP - Temporary
        elif 'TEMP' in record.upper():
            emp_stat = 'TEMP'
        else:
            emp_stat = 'OTHER'
        
        return emp_stat
    
    data['employee_status'] = data['employee_classification'].apply(lambda x: employee_status(x))
    
    
    # Print status
    print('\nCreating additional salaries features...\n')
    
    # Write to /data
    data.to_csv('data/salaries.csv')
    
    return print('\nDone!\n')


# Function to pull data and perform transformations
def transform_all():
    # Pull current data
    pull_data()

    # Read in data
    census_df = pd.read_csv('data/census.csv')
    demographics_df = pd.read_csv('data/demographics.csv')
    salaries_df = pd.read_csv('data/salaries.csv')
    
    # Perform transformations
    census_transform(census_df)
    demographics_transform(demographics_df)
    salaries_transform(salaries_df)