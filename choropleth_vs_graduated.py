import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# choropleth
chor1 = Image.open('images/chor1.png')
chor2 = Image.open('images/chor2.png')
chor3 = Image.open('images/chor3.png')
chor_ex1 = Image.open('images/chor_ex1.png')
chor_ex2 = Image.open('images/chor_ex2.png')
chor_ex3 = Image.open('images/chor_ex3.png')
#graduated_symbol
grad1 = Image.open('images/grad1.png')
grad2 = Image.open('images/grad2.png')
grad3 = Image.open('images/grad3.png')

st. set_page_config(layout="wide")
st.title('Choropleth Maps vs Graduated Symbols Maps')
colu1,col2,colu3 = st.beta_columns(3)
with colu1:
  choice = st.selectbox('select a type of map to view',['Choropleth','Graduated Symbol'])
col1, col2 = st.beta_columns(2)

if choice == 'Choropleth':
  with col1:
    st.write('A random distribution of numbers in the range(0,10) for each state in the US')
    st.write("see what happens when you change Texas' value to 30 or 50")
    chart1 = chor1
    chor_button_reset = st.button('Texas = 10')
    chor_button_2 = st.button('Texas = 30')
    chor_button =  st.button('Texas = 50')
    if chor_button == True:
      chart1 = chor2
    if chor_button_2 == True:
      chart1 = chor3
    if chor_button_reset == True:
      chart1 = chor1
    st.image(chart1)
  with col2:
    st.title('Choropleth Map')
    st.write('Choropleth maps are data maps that use differences in shading/coloring within predefined areas to indicate the average values of a property or quantity in those areas.')
    st.write('They are good for: ')
    st.write('- displaying large amounts of data across large spatial extents')
    st.write('- Easily identifying outliers')
    st.write('A disatvantage of using choropleth maps: ')
    st.write('- Choosing a different boundary, for example county lines vs. state senate districts, could imply completely different spatial relationships')
  bl1,bl2,bl3,ex1,ex2,ex3 = st.beta_columns(6)
  with ex1:
    st.image(chor_ex1)
  with ex2:
    st.image(chor_ex2)
  with ex3:
    st.image(chor_ex3)

if choice == 'Graduated Symbol':
  with col1:
    st.title('Choropleth Map')
    chart1 = grad1
    if st.button('Value = 50'):
      chart1 = grad2
    st.image(chart1)
  with col2:
    st.title('Graduated Symbols Map')
    chart2 = grad1
    if st.button('Graduated Value = 50'):
      chart2 = grad2
    st.image(chart2)
