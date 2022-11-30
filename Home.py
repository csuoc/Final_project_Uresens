import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
from streamlit_card import card

########## Head ##########

st.set_page_config(
    page_title="UreSens Labs",
    page_icon="💊",
)

add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.write("#")

colored_header(
    label="WELCOME TO URESENS LABS",
    description="",
    color_name="red-70"
)

########## Body ##########

st.markdown("<h1 style='text-align: center;'>The next generation of kidney diagnostics</h1>", unsafe_allow_html=True)
st.image("./images/home1.gif", use_column_width=True)

st.markdown("<h1 style='text-align: center;'>🏃 Fast 🏃‍♀️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Take an urine test and upload the results in less than 2 minutes. We'll do the rest for you.</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>👌 Non-invasive 👌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>No needles nor blood involved. Because we care about your fears.</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🎯 Reliable 🎯</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>We have developed an Artificial Intelligence model with 99% accuracy to diagnose early stages of Chronic Kidney Disease.</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>✅ Easy to use ✅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Computer, laptop or mobile phone. Finally, technology and health on the palm of your hand.</p>", unsafe_allow_html=True)

st.write("\n")
st.write("\n")
st.markdown('<center><img src="https://i.ibb.co/zZysCK2/home2.gif"></center>', unsafe_allow_html=True)
st.write("\n")
st.write("\n")

########## Cards ##########

st.markdown("<h1 style='text-align: center;'>Check out what can we offer for you</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>👇👇👇</h1>", unsafe_allow_html=True)

card(
    title="What is CKD?",
    text="Symptoms, causes and treatment",
    image="https://i.ibb.co/kXHVk0J/CKD1.jpg",
    url = "/Chronic_Kidney_Disease"
)   

card(
    title="Instructions",
    text="How to use the urine strips?",
    image="https://i.ibb.co/FVSTQR5/urinetest.jpg",
    url="/Instructions",
)

card(
    title="Submit your results",
    text="Take an urine test and upload here your results",
    image="https://i.ibb.co/BwPc4QK/submitresults.jpg",
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

st.markdown('<center><img src="https://i.ibb.co/kcSSdhP/logo2.png"></center>', unsafe_allow_html=True)