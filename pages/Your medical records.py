########## Import box ##########

import pandas as pd
import streamlit as st
import mysql.connector

from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from functions.functions import rename_columns
from streamlit_extras.colored_header import colored_header
import plotly.express as px
import h2o

########## Head ##########

st.set_page_config(page_title="Medical records", page_icon="📜")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

########## Initialize connection ##########

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Query function

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

########## Body ##########

colored_header(
    label="Your results",
    description="Insert",
    color_name="red-70"
)

st.markdown("**❗ As with all laboratory tests, diagnostic or therapeutic decisions should not be based on a single method result. Substances that cause abnormal urine colour may affect the readability of the test pads on urine test strips.**")

########## Plots ##########

# Select person

getnames = f"""SELECT DISTINCT(patientid) from samples;
            """
names = pd.read_sql_query(getnames, con=conn)
patientid = st.selectbox("Select your name", options=names)

# Retrieve from MySQL
getresults = f"""SELECT date, blood_pressure, albumin, sugar, erythrocytes, leucocytes, nitrite, urobilinogen, ph,
                        gravity, ketones, bilirubin, microalbumin, creatinine FROM samples
                            WHERE patientid="{patientid}";
              """
result = pd.read_sql_query(getresults, con=conn)
# Convert as dataframe
df = pd.DataFrame(result)
# Rename columns
new_name=["Date", "Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Erythrocytes levels Ok/NOk", 
          "Leucocytes WBC/µL", "Nitrite", "Urobilinogen mg/dL", "pH", "Specific Gravity", "Ketones mg/dL", "Bilirubin",
          "Microalbumin mg/dL", "Creatinine mg/dL"
        ]
for i, j in zip(df.columns, new_name):
    rename_columns(df, i, j)
# Plot
y_axis_val = st.selectbox("Select variable to get all the details", options=["Blood Pressure mm/Hg diastolic", 
                          "Albumin (0-5)", "Sugar (0-5)", "Erythrocytes levels Ok/NOk", "Leucocytes WBC/µL", 
                          "Nitrite", "Urobilinogen mg/dL", "pH", "Specific Gravity", "Ketones mg/dL",
                          "Bilirubin", "Microalbumin mg/dL", "Creatinine mg/dL"])
fig = px.line(df, x=df["Date"], y=y_axis_val, markers=True)
#fig.update_xaxes(tickformat="%b %d\n%Y")

MAX_DAYS_WITH_DTICK_FORMAT = 10 # you can change this!
# compute number of days in date range of date column
max_date = pd.to_datetime(df["Date"]).max()
min_date = pd.to_datetime(df["Date"]).min()
num_days = (max_date - min_date).days
# set tick interval if number of days within specified limit
if num_days < MAX_DAYS_WITH_DTICK_FORMAT:
    fig.update_xaxes(dtick=86400000)
st.plotly_chart(fig)

########## Expected results##########

st.subheader("Expected results")

if y_axis_val == "Urobilinogen mg/dL":
    st.write("The normal range of urobilinogen is 0.1 to 1.0 Ehrlich units/dL. If results exceed 2.0 mg/ dL, the patient and urine sample should be further evaluated.")
elif y_axis_val == "Sugar (0-5)":
    st.write("Small amounts of glucose are normally excreted by the kidney. Concentrations of 100 mg/dL may be considered abnormal if found repeatedly.")
elif y_axis_val == "Bilirubin":
    st.write("Bilirubin is normally not detectable in urine, even by the most sensitive methods. Only small amounts of bilirubin are already sufficiently abnormal to require further investigation.")
elif y_axis_val == "Ketones mg/dL":
    st.write("Ketone bodies should not be detected in normal urine samples with this reagent.")
elif y_axis_val == "pH":
    st.write("Urine pH values generally range from 5 to 9.")
elif y_axis_val == "Erythrocytes levels Ok/NOk":
    st.write("Normally, haemoglobin is not detectable in urine (0.010 mg/dL; 3 red blood cells/µL). When haemoglobin appears in the urine, it indicates kidney disease or a urinary tract disorder. Blood can often be found in the urine of menstruating women.")
elif y_axis_val == "Specific Gravity":
    st.write("Normal specific gravity in urine ranges from 1.001 to 1.035.")
elif y_axis_val == "Albumin (0-5)":
    st.write("Normal urine samples usually contain little protein (<20 mg/dL), therefore only persistently elevated urine protein levels indicate kidney or urinary tract disease. Persistent results of trace or more indicate significant proteinuria and therefore further clinical trials are needed to evaluate the significance of the results.")
elif y_axis_val == "Nitrite":
    st.write("Nitrites are normally not detectable in urine.")
elif y_axis_val == "Leucocytes WBC/µL":
    st.write("Leukocytes are not normally detectable in urine.")
elif y_axis_val == "Microalbumin mg/dL":
    st.write("Normal urine albumin levels are less than 2 mg/dL. Microalbumin is indicated with results of 3 ~ 30 mg/dL.")
elif y_axis_val == "Creatinine mg/dL":
    st.write("The urine of healthy individuals contains 10 ~ 300 mg/dL creatinine. Very low creatinine results may be caused by adulteration of the urine sample or severe renal insufficiency.")
#elif y_axis_val =="Microalbumin mg/dL":
#    st.write("*Microalbumin is normally present in urine at concentrations of less than 30 mg albumin/g creatinine. Microalbumin is indicated at a result ratio of 30 ~300 mg/g (abnormal) and clinical albuminuria at a result ratio of > 300 mg/g (high abnormal).")

########## Prediction ##########

colored_header(
    label="Prediction",
    description="Insert",
    color_name="red-70"
)

# Retrieve from MySQL the required parameters
info = f"""SELECT AVG(blood_pressure), AVG(albumin), AVG(sugar), MAX(erythrocytes), MAX(hypertension) from samples
           WHERE patientid="{patientid}";
        """
sqlex = pd.read_sql_query(info, con=conn)
df2 = pd.DataFrame(sqlex)
# Rename columns
new_name=["Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Erythrocytes levels Ok/NOk", "Hypertension Yes/No"]
for i, j in zip(df2.columns, new_name):
    rename_columns(df2, i, j)

@st.cache(suppress_st_warning=True)
def prediction(dataframe):
    #Connect with H2O
    h2o.init()
    # Load file
    test = h2o.H2OFrame(dataframe)
    # Load the model
    my_model = h2o.load_model("./models/GBM_grid_1_AutoML_1_20221127_175518_model_1")
    predictions = my_model.predict(test)
    return predictions

st.write("Based on your current values, the prediction is")

predictions=prediction(df2)
data = h2o.as_list(predictions, use_pandas=False)

if int(data[1][0]) == 1:
    st.write(f"{patientid}, you probably have Chronic Kidney Disease")
elif int(data[1][0]) == 0:
    st.write("The model predicts you don't have Chronic Kidney Disease")
    #st.balloons()
else:
    st.error("Something went wrong, please try again later")

########## Reload cache ##########
if st.button('Reload prediction'):
    try:
        predictions=prediction(df2)
    except:
        st.error("Something went wrong, please try again later")


