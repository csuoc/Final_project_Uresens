import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar

# Head

st.set_page_config(page_title="Chronic Kidney Disease", page_icon="🩺")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()