
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# choropleth
chor1 = Image.open('images/chor1.png')
chor2 = Image.open('images/chor2.png')
chor3 = Image.open('images/chor3.png')
#graduated_symbol
grad1 = Image.open('images/grad1.png')
grad2 = Image.open('images/grad2.png')
grad3 = Image.open('images/grad3.png')

st. set_page_config(layout="wide")
st.title('Choropleth Maps vs Graduated Symbols Maps')
colu1,col2,colu3 = st.beta_columns(3)
with colu1:
  choice = st.selectbox('select a type of map to view',['Choropleth','Graduated Symbols'])
a1,a2,a3,a4,a5,a6,a7 = st.beta_columns(7)
with a1:
  tex_reset = st.button('Texas = 10')
with a2:
  tex_30 = st.button('Texas = 30')
with a3:
  tex_50 = st.button('Texas = 50')
col1, col2 = st.beta_columns(2)

if choice == 'Choropleth':
  with col1:
    st.write('A random distribution of numbers in the range(0,10) for each state in the US')
    st.write("see what happens when you change Texas' value to 30 or 50")
    chart1 = chor1
    if tex_50 == True:
      chart1 = chor2
    if tex_30 == True:
      chart1 = chor3
    if tex_reset == True:
      chart1 = chor1
    st.image(chart1)
  with col2:
    st.title('Choropleth Map')
    st.write('Choropleth maps are data maps that use differences in shading/coloring within predefined areas to indicate the average values of a property or quantity in those areas.')
    st.write('They are good for: ')
    st.write('- Displaying large amounts of data across large spatial extents')
    st.write('- Easily identifying outliers')
    st.write('A disatvantage of using choropleth maps: ')
    st.write('- Choosing a different boundary, for example county lines vs. state senate districts, could imply completely different spatial relationships')
    st.write("Read more [here](https://datavizcatalogue.com/methods/choropleth.html)")
if choice == 'Graduated Symbols':
  with col1:
    st.write('A random distribution of numbers in the range(0,10) for each state in the US')
    st.write("see what happens when you change Texas' value to 30 or 50")
    chart2 = grad1
    if tex_50 == True:
      chart2 = grad2
    if tex_30 == True:
      chart2 = grad3
    if tex_reset == True:
      chart2 = grad1
    st.image(chart2)
  with col2:
    st.title('Graduated Sybmols Map')
    st.write("Graduated symbols maps use data classification to apply symbols to number ranges. The classification method that you use will depend on the data you're using and the information you want to convey on your map.")
    st.write('They are good for: ')
    st.write('- Flexibility: you can display many different types of data spatially')
    st.write('- Easily identifying large or small outliers')
    st.write('A disatvantage of using choropleth maps: ')
    st.write('- Larger symbols can overlap with each other, blocking some potentially important data')
