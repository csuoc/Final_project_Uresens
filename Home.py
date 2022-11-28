import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
from streamlit_card import card


st.set_page_config(
    page_title="UreSens Labs",
    page_icon="💊",
)

add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()

colored_header(
    label="WELCOME TO URESENS LABS",
    description="Chronic kidney disease (CKD) is a long-term condition where the kidneys don't work as well as they should",
    color_name="red-70"
)



card(
    title="What is CKD?",
    text="Symptoms, causes and treatment",
    image="https://i.ibb.co/kXHVk0J/CKD1.jpg",
    url="/Chronic_Kidney_Disease",
)

card(
    title="Instructions",
    text="How to use the urine strips?",
    image="",
    url="/Instructions",
)

card(
    title="Submit your results",
    text="Take an urine test and upload here your results",
    image="https://i.ibb.co/FVSTQR5/urinetest.jpg",
    url="/Submit_your_results",
)

card(
    title="Your results",
    text="Check what UreSens says about you",
    image="https://i.ibb.co/LrtVvjL/results.jpg",
    url="/Your_medical_records",
)

card(
    title="About UreSens",
    text="Discover who's behind the app",
    image="https://i.ibb.co/G9TQPn0/Carles.jpg",
    url="/About",
)

