import streamlit as st
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
from PIL import Image

# Head

st.set_page_config(page_title="About", page_icon="ℹ")
add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()

# Body

colored_header(
    label="Hello! My name is Carles Sunyol",
    description="",
    color_name="red-70"
)

img = Image.open("./images/Carles.jpg")

st.image(img, width=400)
