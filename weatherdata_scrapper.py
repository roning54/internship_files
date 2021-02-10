#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:35:20 2021

@author: Ronin Gomez

Weather API: https://pypi.org/project/wwo-hist/
"""

import pandas as pd
from wwo_hist  import retrieve_hist_data
import os

os.chdir("/Users/rongomez/Desktop/")

frequency= 1
start_date = '01-JAN-2012'
end_date = '31-DEC-2019'
api_key = '6a16ec63db1a4b8d87f204159210202'
location_list = ['27511'] 


hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

print(hist_weather_data)








