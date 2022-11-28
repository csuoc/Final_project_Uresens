import streamlit as st
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
import matplotlib.image as mpimg

# Head

st.set_page_config(page_title="About", page_icon="ℹ")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

# Body

colored_header(
    label="Hello!",
    description="",
    color_name="red-70"
)

img = mpimg.imread("./images/Carles.jpg")

st.image(img, width=400)
