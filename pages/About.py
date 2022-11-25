import streamlit as st
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
import matplotlib.image as mpimg

# Head

st.set_page_config(page_title="About", page_icon="ℹ")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

# Body

st.write("Hello world! I'm Carles, the creator of UreSens")

img = mpimg.imread("./images/Carles.JPG")

st.image(img, width=400)
