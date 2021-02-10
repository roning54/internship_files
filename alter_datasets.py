#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:15:17 2021

@author: rongomez
"""

import pandas as pd

list = ['cary','charlotte', 'dobson', 'kernersville', 'newton', 'pleasantgarden', 'wilmington']

def cel_to_fahrenheit(tempC):
    """Convert celcius to fahrenheit
    
    Returning fahrenheit"""
    fahrenheit = (tempC * 9/5) + 32
    return fahrenheit


for i in list:
    df = pd.read_csv('/Users/rongomez/Desktop/RoninFiles_Internship/actual_datasets/{}.csv'.format(i))
    df['date_time'] = pd.to_datetime(df.date_time)
    df['Week of day'] = df['date_time'].dt.day_name()
    df['month'] = df['date_time'].dt.month
    df['day'] = df['date_time'].dt.day
    df['year'] = df['date_time'].dt.year
    df['hour'] = df['date_time'].dt.hour
    df['tempF'] = cel_to_fahrenheit(df['tempC'])
    
    
    df.to_csv("/Users/rongomez/Desktop/RoninFiles_Internship/actual_datasets/{}.csv".format(i), index = False)
    print(df.head(5))

