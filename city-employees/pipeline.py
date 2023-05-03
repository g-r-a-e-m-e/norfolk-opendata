#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pipeline.py

Data pipeline to pull city employee data from https://data.norfolk.gov

Data included:
    Employee Salaries
    Employee Demographics
    Current Census

Created on Tue May  2 16:10:48 2023

@author: https://github.com/g-r-a-e-m-e
"""

# Import packages
import pandas as pd

# Specify endpoints
salaries = 'https://data.norfolk.gov/resource/4fsk-z8s8.json'
demographics = 'https://data.norfolk.gov/resource/vv96-9m5c.json'
census = 'https://data.norfolk.gov/resource/dijs-dhze.json'

# Specify endpoints 
endpoints = {'salaries': salaries,
             'demographics': demographics,
             'census': census}

# Function to pull current current data
def pull_data(endpoints = endpoints):
    # Loop over endpoints and pull data
    for idx, nm in enumerate(endpoints):
        print(f'\nPulling {nm} data...\n')
        # Read in json data to Pandas DataFrame
        df = pd.read_json(endpoints[nm] + '?$limit=10000')
        # Write out dataframe to data directory
        df.to_csv(f'data/{nm}.csv')
    return print('\nDone!\n')