
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:23:27 2023

@author: Pulsara
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import pycountry
import geopandas

def get_country_code(column): 
    country_code = []
    for country in column: 
        try: 
            temp = pycountry.countries.get(name=country).alpha_2
            country_code.append(temp)
        except:
            country_code.append('None')
    return country_code

happiness_2019 = pd.read_csv('2019.csv')
happiness_2018 = pd.read_csv('2018.csv')
happiness_2017 = pd.read_csv('2017.csv')
happiness_2016 = pd.read_csv('2016.csv')
happiness_2015 = pd.read_csv('2015.csv')
# happiness_2019['Country_code'] = get_country_code(happiness_2019['Country or region'])

# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# world.columns=['pop_est', 'continent', 'name', 'Country_code', 'gdp_md_est', 'geometry']
# merge=pd.merge(world,happiness_2019,on='Country_code')

# location=pd.read_csv('https://raw.githubusercontent.com/melanieshi0120/COVID-19_global_time_series_panel_data/master/data/countries_latitude_longitude.csv')
# merge=merge.merge(location,on='name')
# print(happiness_2019.head())
# print(merge)
# # plot confirmed cases world map 
# merge.plot(column='Happiness Score',
#            figsize=(25, 20),
#            legend=True,cmap='coolwarm')
# plt.title('Happiness Score of each country',fontsize=25)
# # add countries names and numbers 
# for i in range(0,10):
#     plt.text(float(merge.longitude[i]),float(merge.latitude[i]),"{}\n{}".format(merge.name[i],merge.Confirmed_Cases[i]),size=10)
# plt.show()

plt.figure()
plt.scatter(happiness_2019['Score'],happiness_2019['Generosity'],c=happiness_2019['Healthy life expectancy'], cmap='summer')
plt.scatter(happiness_2018['Score'],happiness_2018['Generosity'],c=happiness_2018['Healthy life expectancy'], cmap='spring')
#plt.scatter(happiness_2016['Score'],happiness_2016['Generosity'],c=happiness_2016['Healthy life expectancy'], cmap='summer')
plt.xlabel('Happiness Score')
plt.ylabel('Genoristy')
plt.title('World happiness score vs Generosity')
plt.colorbar()
plt.show()
