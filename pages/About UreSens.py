import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar

st.set_page_config(page_title="About", page_icon="ℹ")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

st.write("Hello world! I'm Carles, the creator of UreSens")

cover = Image.open("images/Carles2.jpg")
st.image(cover, width=400)
