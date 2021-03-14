from PIL import Image
from collections import Counter
from PIL import Image
from urllib.request import urlopen
import random
import seaborn as sns
import colorgram
import colorsys
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

image1 = Image.open('images/forest.jpg')
image2 = Image.open('images/sunset.jpg')
image3 = Image.open('images/coffee.jpg')
random_url = "https://source.unsplash.com/random/1920x1080?sig=1"
random_image = Image.open(urlopen(random_url))

images = {'forest': image1,'sunset':image2,'coffee':image3,'random':random_image}

st.title('Image Palette Generator')
st.write('select an image below, a color palette based on the most prominent colors will generate below')

choice = st.selectbox('select an image or upload your own (coming soon!',['forest','sunset','coffee','random'])
if choice == 'random':
    if st.button('New Image'):
        random_url = random_url[:len(random_url)-1]
        x = random.randint(1,9)
        random_url += str(x)
    else:
        random_url = random_url
def image_display(pic):
    st.image(images[pic])
    img = images[pic]
    colors = colorgram.extract(img,10)
    rgb = []
    for i in range(len(colors)):
        color = colors[i]
        values = color.rgb
        red = values[0]
        green = values[1]
        blue = values[2]
        rgb.append((red,green,blue))
    hls = []
    for i in range(len(colors)):
        color = colors[i]
        values = color.hsl
        hue = values[0]
        light = values[1]
        saturation = values[2]
        hls.append((hue,saturation,light))
    hex_0 = []
    for i in rgb:
        hex_0.append('#%02x%02x%02x' % i)

    #Alternate shades:
    new_rgb = []
    hex_1 = []
    def color_change(hls,hue_val,light_val,sat_val,num_colors):
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
            new_rgb.append(rgb_test)
        for i in new_rgb:
            hex_1.append('#%02x%02x%02x' % i)
        og = sns.palplot(hex_0[:num_colors])
        st.write('original colors')
        st.pyplot(og)
        new = sns.palplot(hex_1[:num_colors])
        st.write('hue shift')
        st.pyplot(new)
    color_change(hls,0.5,1,1,6)
    
image_display(choice)
