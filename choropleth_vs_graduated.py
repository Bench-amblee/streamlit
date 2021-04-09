import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time

# choropleth
chor1 = Image.open('images/chor1.png')
chor2 = Image.open('images/chor2.png')
#graduated_symbol
grad1 = Image.open('images/grad1.png')
grad2 = Image.open('images/grad2.png')

st. set_page_config(layout="wide")
st.title('Choropleth Maps vs Graduated Symbols Maps')
time.sleep(5)
col1, col2 = st.beta_columns(2)

with col1:
  st.title('Choropleth Map')
  chart1 = chor1
  if st.button('Value = 50'):
    chart1 = chor2
  st.image(chart1)
with col2:
  st.title('Graduated Symbols Map')
  chart2 = grad1
  if st.button('Graduated Value = 50'):
    chart2 = grad2
  st.image(chart2)
