#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:35:20 2021

@author: Ronin Gomez

Weather API: https://pypi.org/project/wwo-hist/
"""

from address import AddressParser
import pandas as pd
from wwo_hist  import retrieve_hist_data
import os


course =  {
        'Larry McAfee Course at McAlpine Park' : "8711 Monroe Rd, Charlotte, NC 28212",
        'Ivey Redmon Sports Complex' : '788 Beeson Rd, Kernersville, NC 27284',
        'Hugh McRae Park/Long Life Park' : '314 Pine Grove Dr, Wilmington, NC 28409',
        'Fisher River Park' : '251 County Home Rd, Dobson, NC 27017',
        'Southside Park' : '1775 Southwest Blvd, Newton, NC 28658',
        'Hagan Stone Park' : '5920 Hagan-Stone Park Rd, Pleasant Garden, NC 27313',
        'WakeMed Soccer Complex': 'Soccer Park Dr, Cary, NC 27511'
 }
    
def address_picker(string):
    '''
    Function contains a selector to obtain the address 
    from any of the following park.

    Parameters
    ----------
    string : STRING
        contains the park name

    Returns
    -------
    STRING
        returns the address corresponding to the course dictionary

    '''
    
    if string in ['Larry McAfee Course', 'larry mcafee course', 'larry mcafee'] :
        return course['Larry McAfee Course at McAlpine Park']
    
    elif string in ['Ivery Redmon Sports Complex', 'ivery redmon sports', 'ivery redmon']:
        return course['Ivey Redmon Sports Complex']
    
    elif string in ['Hugh McRae Park/Long Life Park', 'hugh mcrae park', 'hugh mcrae']:
        return course['Hugh McRae Park/Long Life Park']
    
    elif string in ['Fisher River Park', 'fisher river park', 'fisher river']:
        return course['Fisher River Park']
    
    elif string in ['Southside Park', 'southside park']:
        return course['Southside Park']
    
    elif string in ['Hagan Stone Park', 'hagan stone park', 'hagan stone']:
        return course['Hagan Stone Park']
    
    elif string in ['WakeMed Soccer Complex', 'wakemed soccer complex']:
        return course['WakeMed Soccer Complex']
    
    elif string == "0":
        add = str(input("Please enter an address: "))
        return add
    
    else:
        print("ERROR")
        
def cel_to_fahrenheit(tempC):
    '''
    Function that contains the formula to convert celcius to fahrenheit

    Parameters
    ----------
    tempC : INT
        contains the celcius temperature 

    Returns
    -------
    fahrenheit : INT
        returns the converted fahrenheit integer

    '''
    fahrenheit = (tempC * 9/5) + 32 # formula
    return fahrenheit # returns fahrenheit integer

def changes_to_datasets(list, city = None):
    '''
    Function makes changes to the datasets in csv format

    Parameters
    ----------
    list : LIST
        contains strings that corresponds to csv filenames
    city : STRING, optional
        contains the string name of the city obtained by the address parser
    '''
    # for loop got through each named file
    for i in list:
        df = pd.read_csv('/Users/rongomez/Desktop/{}.csv'.format(i)) #read the csv file located in the directory
        
        df['date_time'] = pd.to_datetime(df.date_time)       #changes the date_time column to the datetime data type
        df['Week of day'] = df['date_time'].dt.day_name()  #appends a new column and inserts the day of week based on the date_time column
        df['month'] = df['date_time'].dt.month                   #appends a new column and inserts the month based on the date_time column
        df['day'] = df['date_time'].dt.day                         #appends a new column and inserts the day based on the date_time column
        df['year'] = df['date_time'].dt.year                     #appends a new column and inserts the year based on the date_time column
        df['hour'] = df['date_time'].dt.hour                    #appends a new column and inserts the hour based on the date_time column
        df['tempF'] = cel_to_fahrenheit(df['tempC'])     #appends a new column and inserts the fahrenheit column based on the tempC column
        
        df['city'] = "{}".format(city)                             #appends a new column and inserts the city name associated with the zip code obtained in the address parser
        
        
        df.to_csv("/Users/rongomez/Desktop/{}.csv".format(i), index = False) #updates each csv file with all the changes made above

def wwo_api(city_name, address_zip):
    '''
    Contains the wwo api function call to obtain csv

    Parameters
    ----------
    city_name : STRING
        contains the city name string obtained by the address parser
    address_zip : STRING
        contains the zip code string obtained by the address parser
    '''
    os.chdir("/Users/rongomez/Desktop/") #create file and puts it in the following directory
    frequency= int(input("Hourly Rate: ")) #set a hourly set
    
    #start_date and end_date contains the date asked from the user
    start_date , end_date = str(input('Start Date (Format = DD-MMM-YYYY): ')), str(input('End Date (Format = DD-MMM-YYYY): '))
    
    api_key = '6a16ec63db1a4b8d87f204159210202' #contains api key from the website
    location_list = [address_zip] #list contains the zip code of 
    
    #retrieve the history data function that retrieves the data frame from wwo website
    retrieve_hist_data(api_key,
                                        location_list,
                                        start_date,
                                        end_date,
                                        frequency,
                                        location_label = False,
                                        export_csv = True,
                                        store_df = True)
        
    
def main():
    
    ap = AddressParser() #ap object contains the AddressParser class
    
    print('\nPARK NAMES:\n\nLarry McAfee Course at McAlpine Park \nIvey Redmon Sports Complex \nHugh McRae Park/Long Life Park \nFisher River Park \nSouthside Park \nHagan Stone Park \nWakeMed Soccer Complex')
    print('\n\nTo obtain weather data...')
    string = str(input("\nPlease enter a track course name or enter 0 if park name is NOT included in list: ")) #user enters the name of track course
    selected = address_picker(string) #function call of address_picker and is contained in the selected variable
    
    address = ap.parse_address(selected) #parse_address function call is contained in the address variable
    print("\nCITY: {}\nZIP: {}".format(address.city, address.zip)) #prints the city and zip by calling it from the address object

    wwo_api(address.city, address.zip) #wwo_api function call is used based on the city and zip code
    
    changes_to_datasets(address.zip, address.city) #creates new columns
    
    military_time = [int(input("Enter an integer relative to military time: "))] #military time variable contains the input given by the user
    
    df = pd.read_csv("{}.csv".format(address.zip)) #reads the csv file based on the zip code
    df.set_index("hour", inplace = True) #sets the index to hour
    
    col = ['date_time', 'Week of day', 'month', 'day', 'year', 'tempF', 'winddirDegree', 'windspeedKmph'] # list contains the columns needed
    
    print(df.loc[military_time,col]) # prints the results
    
    
    
if __name__ == "__main__":
    main()





