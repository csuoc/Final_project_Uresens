import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_card import card
import matplotlib.image as mpimg

st.set_page_config(
    page_title="UreSens App",
    page_icon="💊",
)

add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()


card(
    title="About UreSens",
    text="Discover who's behind the app",
    image="https://i.ibb.co/JqQjkmK/Carles.jpg",
    url="http://localhost:8501/About#hello",
)

card(
    title="What is CKD?",
    text="Symptoms, causes, treatment",
    image="https://i.ibb.co/m4Dr1t0/CKD1.jpg",
    url="http://localhost:8501/About#hello",
)

card(
    title="Submit your results",
    text="Take an urine test and upload here your results",
    image="https://i.ibb.co/gV5K0kS/urinetest.jpg",
    url="http://localhost:8501/About#hello",
)

