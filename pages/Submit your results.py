########## Import box ##########

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header

########## Head ##########

st.set_page_config(page_title="Submit your results", page_icon="📮")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

########## Initialize connection ##########

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

########## Perform query ##########

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        cur.close()
        return conn.close()

########## Body ##########

colored_header(
    label="Submit your results",
    description="Insert",
    color_name="red-70"
)

########## Insert into MySQL ##########

patientid = st.text_input("Enter your name")
date = st.date_input("Input your date")

#color = st.color_picker('#ff5733')

blood_pressure = st.number_input("Enter your blood pressure value (diastolic)", 0, 200)
albumin = st.number_input("Enter your albumin value (0-5)", 0, 5)
sugar = st.number_input("Enter your sugar value (0-5)", 0, 5)
blood_urea = st.number_input("Enter your blood urea levels", 0, 100)
creatinine = st.number_input("Enter your creatinine levels", 0, 100)

hypertension = st.selectbox("Do you have hypertension?",
                            ("Yes", "No"))
if hypertension == "Yes":
    hypertension = 1
elif hypertension == "No":
    hypertension = 0


if st.button("Submit your results"):

    st.success("Results submitted succesfully", icon="✅")
    st.balloons()
    insertSQL = f"""INSERT INTO samples
     (patientid, date, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension) 
        VALUES ('{patientid}', '{date}', '{blood_pressure}', '{albumin}', '{sugar}', '{blood_urea}', '{creatinine}', '{hypertension}');
    """
    run_query(insertSQL)

