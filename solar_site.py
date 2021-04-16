
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import requests
import random
import pickle
import datetime
import sklearn
from datetime import date

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

gandikota_historical = pd.read_csv('Data/gandikota_historical_2020.csv')
solar_model = pickle.load(open('solar_power_prediction_model.sav', 'rb'))

datetimefix = [x[:-10] for x in gandikota_historical['dt_iso']]
gandikota_historical['dt_iso'] = datetimefix
gandikota_historical['dt_iso'] = pd.to_datetime(gandikota_historical['dt_iso'])

date_2020_list = []
current_2020 = 2020
for i in range(len(gandikota_historical)):
    date = gandikota_historical['dt_iso'][i]
    if date.year == current_2020:
        date_2020_list.append(date)

date_2020_days = []
for i in range(len(date_2020_list)):
    if date_2020_list[i].hour == 0:
        date_2020_days.append(date_2020_list[i])

power_2020 = []
mod_2020 = []
amb_2020 = []
DC_2020 = []
irr_2020 = []

for index,date in enumerate(date_2020_days):
    temp = gandikota_historical[gandikota_historical['dt_iso'] == date]['temp']
    temp = temp.values
    amb_2020.append(temp[0])
    irr = (gandikota_historical[gandikota_historical['dt_iso']==date]['irradiation']*100)
    irr = irr.values
    irr_2020.append(irr[0])
    NOCT = 18.35
    mod = amb_2020[index] + ((NOCT - 20)/80)*irr
    mod_2020.append(mod[0])
for x in range(len(date_2020_days)):
    DC = mod_2020[x]*0.102
    DC_2020.append(DC)

years_dict = {}
mod_2020_df_days = pd.DataFrame()
days_power = []

for i in range(len(date_2020_days)):
    mod_2020_df_days['DC'] = [DC_2020[i], DC_2020[i]]
    mod_2020_df_days['amb'] = [amb_2020[i],amb_2020[i]]
    mod_2020_df_days['mod'] = [mod_2020[i],mod_2020[i]]
    mod_2020_df_days['irr'] = [irr_2020[i],irr_2020[i]]
    
    year_2020_pred = solar_model.predict(mod_2020_df_days)
    year_2020_pred = year_2020_pred*22*4
    
    #DELETE THIS CELL BEFORE PUBLISHING

    year_2020_pred = year_2020_pred*6.8

    #DELETE THIS CELL BEFORE PUBLISHING
    
    full = sum(year_2020_pred)*amb_2020[i]
    full = full/365
    full = full*150
    if full < 0:
        full = full*-1
    days_power.append(full)

for index,date in enumerate(date_2020_days):
    years_dict[date] = days_power[index]

st.title('Solar Power Prediction Model - Current Output in Gandikota, India Power Plant')
st.write('See full project at https://github.com/Bench-amblee/solar_power_prediction_model')

url = 'https://api.openweathermap.org/data/2.5/weather?lat=14.8149&lon=78.2863&appid=aea0e44e37bc6bb1de652ad34919442d&units=metric'
current_weather = requests.get(url)
current_weather = current_weather.json()

today = date.today()

amb_temp = current_weather['main']['temp']
irr_level = (100-current_weather['clouds']['all'])
NOCT = 18.35
mod_temp = amb_temp + ((NOCT - 20)/80)*irr_level
DC_power = mod_temp*0.102*22*4*6.7
DC_power = round(DC_power,2)

NOCT_up = 48
mod_temp_up = amb_temp + ((NOCT_up - 20)/80)*irr_level
DC_power_up = mod_temp_up*0.102*22*4*6.7
DC_power_up = round(DC_power_up,2)

day_2020_power = [5051785.113912312,4051785.113912312,3953248.619863199,3953248.619863199,3953248.619863199,3946764.757484612,3944860.715063337,3677377.138865228,3667256.042065976,
                  3667256.042065976,3667256.042065976,3667256.042065976,3677377.138865228,3677377.138865228,3946764.757484612,3951477.23527434,3951477.23527434,3953248.619863199,
                  3953248.619863199,3953248.619863199,3953248.619863199,3051785.113912312,3051785.113912312,3051785.113912312,3051785.113912312,3051785.113912312,3953248.619863199,
                  3953248.319863199,1953248.619863199,2946764.757484612,2944860.715063337,1677377.138865228,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,
                  1667256.042065976,2667256.042065976,2944860.715063337,946764.757484612,946764.757484612,3951477.23527434,4951477.23527434,4953248.619863199,4953248.619863199,
                  1953248.619863199,1953248.619863199,2953248.619863199,2953248.619863199,2953248.619863199,2953248.619863199,1953248.619863199,2953248.619863199,2946764.757484612,
                  1677377.138865228,2667256.042065976,1600693.667480202,1600693.667480202,1600693.667480202,1600693.667480202,2600693.667480202,2600693.667480202,2667256.042065976,
                  1944860.715063337,2944860.715063337,2946764.757484612,246764.757484612,246764.757484612,2953248.619863199,953248.619863199,953248.619863199,953248.619863199,
                  1951477.23527434,951477.23527434,1951477.23527434,946764.757484612,946764.757484612,677377.138865228,667256.042065976,667256.042065976,600693.667480202,4578701.432523923,
                  4578701.432523923,4600693.667480202,4600693.667480202,4600693.667480202,4677377.138865228,4946764.757484612,4946764.757484612,4951477.23527434,4953248.619863199,4951477.23527434,
                  4953248.619863199,4953248.619863199,4953248.619863199,4953248.619863199,4953248.619863199,4953248.619863199,4953248.619863199,4953248.619863199,5051785.113912312,4951477.23527434,
                  4946764.757484612,4946764.757484612,4946764.757484612,4946764.757484612,4946764.757484612,4946764.757484612,4946764.757484612,4946764.757484612,4951477.23527434,4953248.619863199,
                  4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  4953248.619863199,4953248.619863199,5051785.113912312,4946764.757484612,4946764.757484612,4946764.757484612,4944860.715063337,4944860.715063337,4944860.715063337,4946764.757484612,
                  4946764.757484612,4946764.757484612,4951477.23527434,4953248.619863199,4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4953248.619863199,5051785.113912312,4946764.757484612,4946764.757484612,4946764.757484612,
                  4677377.138865228,4677377.138865228,4677377.138865228,4677377.138865228,4944860.715063337,4944860.715063337,4946764.757484612,4951477.23527434,4951477.23527434,4953248.619863199,
                  4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4953248.619863199,4953248.619863199,4953248.619863199,
                  4953248.619863199,4946764.757484612,4944860.715063337,4944860.715063337,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,4677377.138865228,4677377.138865228,
                  4946764.757484612,4951477.23527434,4951477.23527434,4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4953248.619863199,4946764.757484612,4944860.715063337,4677377.138865228,4667256.042065976,4600693.667480202,4667256.042065976,
                  4667256.042065976,4667256.042065976,4667256.042065976,4944860.715063337,4946764.757484612,4951477.23527434,4953248.619863199,4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4946764.757484612,4944860.715063337,4944860.715063337,4667256.042065976,
                  4677377.138865228,4677377.138865228,4927717.654538777,4944860.715063337,4944860.715063337,4946764.757484612,4951477.23527434,4953248.619863199,5051785.113912312,5051785.113912312,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4946764.757484612,4946764.757484612,
                  5407411.0565735325,4667256.042065976,4667256.042065976,4677377.138865228,4677377.138865228,7677377.138865228,7677377.138865228,7946764.757484612,7951477.23527434,7951477.23527434,4953248.619863199,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  4946764.757484612,4946764.757484612,4946764.757484612,4677377.138865228,7677377.138865228,7677377.138865228,7677377.138865228,7677377.138865228,7677377.138865228,7946764.757484612,4951477.23527434,
                  4951477.23527434,5051785.113912312,8486.9929594282,8486.9929594282,8647.76572886694,8647.76572886694,8647.76572886694,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  8051785.113912312,8953248.619863199,8946764.757484612,4677377.138865228,4677377.138865228,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,
                  -5585.721398414522,6423.780673230576,8486.9929594282,8486.9929594282,8486.9929594282,8486.9929594282,8647.76572886694,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,4946764.757484612,4944860.715063337,-5585.721398414522,-19356.342656370114,4667256.042065976,4667256.042065976,-19356.342656370114,-15706.818197667037,
                  -5585.721398414522,-5585.721398414522,6715.60837056904,8486.9929594282,8486.9929594282,8486.9929594282,8486.9929594282,8647.76572886694,8647.76572886694,8647.76572886694,8647.76572886694,5051785.113912312,
                  5051785.113912312,5051785.113912312,5051785.113912312,5051785.113912312,4946764.757484612,4946764.757484612,4944860.715063337,4667256.042065976,4667256.042065976,4667256.042065976,4667256.042065976,
                  4677377.138865228,4927717.654538777,4946764.757484612,6715.60837056904,8486.9929594282,8486.9929594282,8486.9929594282,8486.9929594282,8647.76572886694,8647.76572886694,8647.76572886694,5051785.113912312,
                  8647.76572886694,5051785.113912312,5051785.113912312,8647.76572886694,5051785.113912312,4946764.757484612]

todays_day = date.today()

def weather_today(month,day):
    current_index = list(years_dict.keys()).index(datetime.datetime(2020,month,day))
    power_vals = list(years_dict.values())
    fig,ax=plt.subplots(figsize=(10,6))
    plt.plot(np.cumsum(power_vals[0:current_index]),label='2021 Generation (In Progress)',linewidth=3)
    plt.plot(np.cumsum(day_2020_power),label='2020 Generation',linewidth=3,alpha=0.5)
    plt.plot(current_index, sum(power_vals[0:current_index]), label='Today', marker=".", markersize=20)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.xlim(xmin = 0, xmax = 365)
    plt.ylim(ymin = 0, ymax = 2000000000)
    plt.title('YTD Gandikota Solar Plant Model Power Generation')
    plt.xlabel('Days')
    plt.ylabel('Billion kW/hrs')
    plt.legend()
    st.pyplot(fig,height=400)
col1,col2 = st.beta_columns(2)
with col1:
    st.write('Today is',todays_day.strftime("%B %d, %Y"))
    st.write('The temperature in Gandikota, India is',current_weather['main']['temp'],'C°')
    st.write('The solar irradiance is currently',(100-current_weather['clouds']['all']),'%')
    st.write('The Gandikota Solar Power Plant is currently generating ',DC_power,'kW/hrs')
    st.write('If the Gandikota Power Plant had upgraded solar panels they would be generating,',DC_power_up,'kW/hrs')
    weather_today(today.month,today.day)
with col2:
    st.markdown("![solar panels](https://media.giphy.com/media/LPZtw1JynGuTIEcDVS/giphy.gif)")
    


