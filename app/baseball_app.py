import streamlit as st
import settings
from PIL import Image

st.write('Hello World.')

image_footer = Image.open(settings.img_loc + '/SAS_logo.png')
st.image(image_footer,caption='Powered by SAS',width=100)