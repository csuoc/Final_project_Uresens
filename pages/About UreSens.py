import streamlit as st
from PIL import Image

st.set_page_config(page_title="About", page_icon="ℹ")

st.write("Hello world! I'm Carles, the creator of UreSens")

cover = Image.open("images/Carles2.jpg").rotate(90)
st.image(cover, width=400)
