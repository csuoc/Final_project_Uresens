# Import box

import pandas as pd
import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
import plotly.express as px

# Head

st.set_page_config(page_title="Medical records", page_icon="📜")
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
        return cur.fetchall()

# Body

st.title("Your medical records")

# Retrieve from MySQL

getSQL = f"""SELECT date, blood_pressure, albumin, sugar, blood_urea, creatinine FROM samples;
        """
result = pd.read_sql_query(getSQL, con=conn)

# Save as dataframe

df = pd.DataFrame(result)

# Plot
y_axis_val = st.selectbox("Select Y axis", options=["blood_pressure", "albumin", "sugar", "blood_urea", "creatinine"])
fig = px.line(df, x=df["date"], y=y_axis_val)
st.plotly_chart(fig)