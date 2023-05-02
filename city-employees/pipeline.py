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

# Function to pull current current data
def pull_data(json_path, filename: str):
    # Read in json data to Pandas DataFrame
    df = pd.read_json(json_path)
    # Write out dataframe to data directory
    return df.to_csv(f'data/{filename}')

# Specify endpoints 
endpoints = {'salaries': salaries,
             'demographics': demographics,
             'census': census}

# Loop over endpoints and pull current data, stage to current 
for idx, nm in enumerate(endpoints):
    print(f'\nPulling {nm} data...\n')
    pull_data(endpoints[nm], f'{nm}.csv')

print('Done!')