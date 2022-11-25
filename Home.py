import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar


st.set_page_config(
    page_title="UreSens App",
    page_icon="💊",
)

add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()


cover = Image.open("images/logo2.png")
st.image(cover)
st.write("Hello world!")
st.markdown("This is **bold** and this is _italics_")
st.title('My first title')