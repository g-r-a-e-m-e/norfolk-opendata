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
import pandas as pd
import numpy as np

# Read in data
census_df = pd.read_csv('data/census.csv')
demographics_df = pd.read_csv('data/demographics.csv')
salaries_df = pd.read_csv('data/salaries.csv')

# Functions to transform features in each DataFrame
def census_transform(data = census_df):
    # Census data are taken every 10 years.
    # Creating decadal_delta fields to compare values between each census
    data['decadal_delta_2020_vs_2010'] = data['census_2020'] - data['census_2010']
    data['decadal_delta_2000_vs_2000'] = data['census_2010'] - data['census_2000']
    
    return data.to_csv('data/census.csv')