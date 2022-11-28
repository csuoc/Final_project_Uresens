# Import box

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar


# Head

st.set_page_config(page_title="Instructions", page_icon="📮")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

from streamlit_extras.colored_header import colored_header

colored_header(
    label="Instructions",
    description="Instructions",
    color_name="red-70"
)