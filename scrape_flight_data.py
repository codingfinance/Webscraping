#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:20:56 2020

@author: Snow
"""

# =============================================================================
# Import libraries
# =============================================================================

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import options
import numpy as np
import pandas as pd
import re

# =============================================================================
# Set the Browser as headless
# =============================================================================

opt = options.Options()
opt.headless = True

# =============================================================================
# Set our search criteria
# =============================================================================

origin = 'IAH'
destination = 'LAX'

start_date = '2020-08-10'
end_date = '2020-09-10'

url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + start_date + "/" + end_date + "?sort=bestflight_a&fs=stops=0"

# =============================================================================
# Start the headless browser
# =============================================================================

driver = webdriver.Firefox(options = opt)

driver.get(url)

# =============================================================================
# Convert to soup object
# =============================================================================

soup = BeautifulSoup(driver.page_source, 'lxml')

# =============================================================================
# Extract the departure and arrival times
# =============================================================================

dep_times = soup.find_all('span', attrs={'class': 'depart-time base-time'})

dep_times = [i.getText() for i in dep_times]

arr_times = soup.find_all('span', attrs={'class': 'arrival-time base-time'})

arr_times = [i.getText() for i in arr_times]

time_meridiem = soup.find_all('span', attrs={'class': 'time-meridiem meridiem'})

time_meridiem = [i.getText() for i in time_meridiem]

# =============================================================================
# Reshape the data
# =============================================================================

dep_times = np.asarray(dep_times)
dep_times = dep_times.reshape(int(len(dep_times) / 2) , 2)



arr_times = np.asarray(arr_times)
arr_times = arr_times.reshape(int(len(arr_times) / 2) , 2)


time_meridiem = np.asarray(time_meridiem)
time_meridiem = time_meridiem.reshape(int(len(time_meridiem) / 4) , 4)


dep_time_origin = [i + str(j) for i,j in zip(dep_times[:,0], time_meridiem[:,0])]

dep_time_destination = [i + str(j) for i,j in zip(dep_times[:,1], time_meridiem[:,2])] 

                                                  
arr_time_destination = [i + str(j) for i,j in zip(arr_times[:,0], time_meridiem[:,1])]

arr_time_origin = [i + str(j) for i,j in zip(arr_times[:,1], time_meridiem[:,3])]

                                                  

# =============================================================================
# Get Price data
# =============================================================================

regex = re.compile('Common-Booking-MultiBookProvider (.*)multi-row Theme-featured-large(.*)')

price_list = soup.find_all('div', attrs={'class': regex})

price = [i.text.split('\n')[3] for i in price_list]

# =============================================================================
# Build a data frame
# =============================================================================

df = pd.DataFrame({'origin' : origin,
                  'destination' : destination,
                  'start_date' : start_date,
                  'end_date' : end_date,
                  'dep_time_origin':dep_time_origin,
                  'arr_time_destination':arr_time_destination,
                  'dep_time_destination':dep_time_destination,
                  'arr_time_origin':arr_time_origin,
                  'price':price}) 
















