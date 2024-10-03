from PIL import Image
from urllib.request import urlopen
import random
import seaborn as sns
import colorgram
import colorsys
import streamlit as st
import matplotlib.pyplot as plt
import matplot.cm

st.set_option('deprecation.showPyplotGlobalUse', False)

image1 = Image.open('images/forest.jpg')
image2 = Image.open('images/sunset.jpg')
image3 = Image.open('images/coffee.jpg')
white = Image.open('images/white.jpg')
random_url = "https://picsum.photos/600"
random_image = Image.open(urlopen(random_url))

images = {'forest': image1,'sunset':image2,'coffee':image3,'random':random_image,'upload':white}

#images = {'forest': image1,'sunset':image2,'coffee':image3,'upload':white}

# title 
st.title('Color Palette Generator')
st.write("Created by Ben Chamblee [Github](https://github.com/Bench-amblee/streamlit/edit/main/color_palette.py)")
st.write('select an image, a color palette based on the most prominent colors will generate below')

choice = st.selectbox('select an image, generate a random image, or upload your own:',['forest','sunset','coffee','random','upload'])

#choice = st.selectbox('select an image, or upload your own:',['forest','sunset','coffee','random','upload'])

#choice = st.selectbox('select an image, or upload your own:',['forest','sunset','coffee','upload'])


if choice == 'random':
    if st.button('New Image'):
        random_url = random_url
    else:
        random_url = random_url

if choice == 'upload':
    uploaded_file = st.file_uploader("Choose Files ", type=['png','jpg','JPG','PNG'])
    if uploaded_file is not None:
        uploaded_file = Image.open(uploaded_file)
        images['upload'] = uploaded_file
    else: uploaded_file = white
else: uploaded_file = white
rgb = []
hls = []
hex_0 = []
def image_display(pic):
    display_img = images[pic].resize((800,500))
    st.image(display_img)
    img = images[pic]
    colors = colorgram.extract(img,10)
    for i in range(len(colors)):
        color = colors[i]
        values = color.rgb
        red = values[0]
        green = values[1]
        blue = values[2]
        rgb.append((red,green,blue))
    for i in range(len(colors)):
        color = colors[i]
        values = color.hsl
        hue = values[0]
        light = values[1]
        saturation = values[2]
        hls.append((hue,saturation,light))
    for i in rgb:
        hex_0.append('#%02x%02x%02x' % i)

#Alternate shades:
new_rgb_1 = []
hex_1 = []
def palette(hls,hue_val,light_val,sat_val,num_colors,string):
    for i,x in enumerate(hls): 
        hls_div = tuple(h/255 for h in hls[i])
        rgb_div = colorsys.hls_to_rgb(hls_div[0]*hue_val,
                                      hls_div[1]*light_val,
                                      hls_div[2]*sat_val)
        rgb_test = tuple(r*255 for r in rgb_div)
        rgb_test = list(rgb_test)
        for i, x in enumerate(rgb_test):
            x = int(x)
            rgb_test[i] = abs(x)
        rgb_test = tuple(rgb_test)
        new_rgb_1.append(rgb_test)
    for i in new_rgb_1:
        hex_1.append('#%02x%02x%02x' % i)
    og = sns.palplot(hex_1[:num_colors])
    plt.style.use("dark_background")
    st.write(string)
    st.pyplot(og)

image_display(choice)
palette(hls,1,1,1,6,'original color palette')
st.title('hex values:')
for i in range(6):
    st.write(i+1,':',hex_0[i])
    
