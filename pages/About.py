import streamlit as st
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
from PIL import Image
from streamlit_card import card

# Head

st.set_page_config(page_title="About", page_icon="ℹ")
add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()
st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

colored_header(
    label="Hello! 👋",
    description="",
    color_name="red-70"
)

########## Body ##########

st.write("""
        My name is **Carles Sunyol** and I'm the creator of **UreSens**. I was born in 1994 in Reus, Tarragona (Spain) and 
        I studied **Chemistry** at Rovira i Virgili University in Tarragona. 
        Later on, I studied for a master's degree in **Nanoscience, Materials and Processes** at the same place.
        """
        )

st.markdown('<center><img src="https://i.ibb.co/JqQjkmK/Carles.jpg" width=400></center>', unsafe_allow_html=True)
st.write("\n")

st.write("""
        Four years ago I started working as a **Product Stewardship** in a chemical company, leading more than 30 European projects 
        that involved developing the next generation of **sustainable materials** for the automotive industry. 
        However, in my last years, I realized **I had to make a change** and start something new. 
        My passion to understand data and storytelling brought me to Ironhack Spain, where I coursed a **2-month Bootcamp in Data Analytics**.
        """)
st.write("""
         I enrolled on the course **without any single clue of what Python was** and much less about machine learning. 
         But with a lot of effort, consistency and hours spent learning I soon realized that **nothing is impossible**.
         """)
st.write("""
        **UreSens is the culmination** of the Data Analytics bootcamp at Ironhack and all you see was entirely made in one week. 
        I can't be more proud of myself for what I have done in such a time.
        """
        )

st.write("""
        **Thank you** for visiting my webpage and I hope this could be the start of a new adventure. 
        You can contact me on my **LinkedIn profile** in case of any doubts.
        """)

st.write("**#FromZeroToHero**")
card(
    title="LinkedIn",
    text="See my profile",
    image="https://i.ibb.co/HPHYMBc/P1045520.jpg",
    url = "https://www.linkedin.com/in/carlessunyolocon/"
)   