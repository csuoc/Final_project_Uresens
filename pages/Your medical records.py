# Import box

import pandas as pd
import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from functions.functions import rename_columns
import plotly.express as px
import h2o

# Head

st.set_page_config(page_title="Medical records", page_icon="📜")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

# Initialize connection.

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Query function

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Body

st.title("Your medical records")

# Retrieve from MySQL

getSQL = f"""SELECT date, blood_pressure, albumin, sugar, blood_urea, creatinine FROM samples
            WHERE patientid="Carles";
        """
result = pd.read_sql_query(getSQL, con=conn)

# Convert as dataframe

df = pd.DataFrame(result)

# Rename columns

new_name=["Date", "Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Blood Urea mg/dL", "Serum Creatinine mg/dL", "Hypertension Yes/No"]
for i, j in zip(df.columns, new_name):
    rename_columns(df, i, j)

# Plot
y_axis_val = st.selectbox("Select Y axis", options=["Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Blood Urea mg/dL", "Serum Creatinine mg/dL"])
fig = px.scatter(df, x=df["Date"], y=y_axis_val)
st.plotly_chart(fig)

# Prediction

h2o.init()

# Retrieve from MySQL the required parameters

pred = f"""SELECT blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension FROM samples
            WHERE patientid="Test1";
        """
result2 = pd.read_sql_query(pred, con=conn)
df2 = pd.DataFrame(result2)

# Rename columns

new_name=["Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Blood Urea mg/dL", "Serum Creatinine mg/dL", "Hypertension Yes/No"]
for i, j in zip(df2.columns, new_name):
    rename_columns(df2, i, j)

#######################################

st.title("Prediction")

# Load file

test = h2o.H2OFrame(df2)

# Load the model

my_model = h2o.load_model("./models/XRT_1_AutoML_1_20221124_232959")

# Predict

predictions = my_model.predict(test)

if predictions["predict"] == 1:

    st.write("You probably have Chronic Kidney Disease")

elif predictions["predict"] == 0:

    st.write("The model predicts you don't have Chronic Kidney Disease")