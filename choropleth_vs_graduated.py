import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# choropleth
chor1 = Image.open('images/chor1.png')
chor1 = Image.open('images/chor2.png')
#graduated_symbol
grad1 = Image.open('images/grad1.png')
grad2 = Image.open('images/grad2.png')

st. set_page_config(layout="wide")
st.title('Choropleth Maps vs Graduated Symbols Maps')

col1, col2 = st.beta_columns(2)

with col1:
  st.title('Choropleth Map')
  st.image(chor1)
with col2:
  st.title('Graduated Symbols Map')
  st.image(chor2)
