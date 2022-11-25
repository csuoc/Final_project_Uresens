# Import box

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar

# Head

st.set_page_config(page_title="Submit your results", page_icon="📮")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

# Initialize connection.

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        cur.close()
        return conn.close()

# Body

st.title("Submit your results")


# Insert into MySQL

patientid = st.text_input("Enter your name")
blood_pressure = st.text_input("Enter your blood pressure value (diastolic)")
albumin = st.text_input("Enter your albumin value (0-5)")
sugar = st.text_input("Enter your sugar value (0-5)")
blood_urea = st.text_input("Enter your blood urea levels")
creatinine = st.text_input("Enter your creatinine levels")
hypertension = st.text_input("Do you have hypertension?")


if st.button("Submit your results"):

    st.success("Results submitted succesfully", icon="✅")
    st.balloons()
    insertSQL = f"""INSERT INTO samples
     (patientid, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension) 
        VALUES ('{patientid}', '{blood_pressure}', '{albumin}', '{sugar}', '{blood_urea}', '{creatinine}', '{hypertension}');
    """
    run_query(insertSQL)

