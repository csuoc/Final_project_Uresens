# Import box

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
import matplotlib.image as mpimg
from PIL import Image
# Head

st.set_page_config(page_title="Instructions", page_icon="📮")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

from streamlit_extras.colored_header import colored_header

colored_header(
    label="My New Pretty Colored Header",
    description="This is a description",
    color_name="violet-70",
)
from streamlit_image_select import image_select


img = image_select(
    label="Select a cat",
    images=[
        "./images/logo2.png",
        "./images/Carles.JPG",
        "./images/logo.png",
    ],
    captions=["A cat", "Another cat", "Guess what, a cat..."]
)

st.write(img)