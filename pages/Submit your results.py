########## Import box ##########

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from functions.functions import resize_images
from streamlit_extras.colored_header import colored_header
import matplotlib.image as mpimg
from streamlit_image_select import image_select


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

img = mpimg.imread("./images/urinetest.jpg")
st.image(img, use_column_width=True)

########## Insert into MySQL ##########

patientid = st.text_input("🧍‍♂️🧍‍♀️ Enter your name")
date = st.date_input("🗓 Input your date")

#Blood pressure

blood_pressure = st.number_input("🩺 Enter your blood pressure value (diastolic):", 0, 200)



# Protein

a_neg = resize_images(image_path="./images/Protein/neg.jpg", width=1, height=1)
a_trace = resize_images(image_path="./images/Protein/trace.jpg", width=1, height=1)
a_30 = resize_images(image_path="./images/Protein/30.jpg", width=1, height=1)
a_100= resize_images(image_path="./images/Protein/100.jpg", width=1, height=1)
a_300 = resize_images(image_path="./images/Protein/300.jpg", width=1, height=1)
a_1000 = resize_images(image_path="./images/Protein/1000.jpg", width=1, height=1)

albumin = image_select(use_container_width=False,
    label="🥚 Select your protein results:",
    images=[a_neg, a_trace, a_30, a_100, a_300, a_1000],
    captions=["Negative", "Trace levels", "+30(0.3)", "++100(1.0)", "+++300(3.0)", "++++1000(10)"]
)

if albumin == a_neg:
    albumin = 0
elif albumin == a_trace:
    albumin = 1
elif albumin == a_30:
    albumin = 2
elif albumin == a_100:
    albumin = 3
elif albumin == a_300:
    albumin = 4
else:
    albumin = 5

# Sugar

s_neg = resize_images(image_path="./images/Sugar/neg.jpg", width=1, height=1)
s_100 = resize_images(image_path="./images/Sugar/100.jpg", width=1, height=1)
s_250 = resize_images(image_path="./images/Sugar/250.jpg", width=1, height=1)
s_500= resize_images(image_path="./images/Sugar/500.jpg", width=1, height=1)
s_1000 = resize_images(image_path="./images/Sugar/1000.jpg", width=1, height=1)
s_2000 = resize_images(image_path="./images/Sugar/2000.jpg", width=1, height=1)

sugar = image_select(use_container_width=False,
    label="🍭 Select your glucose results:",
    images=[s_neg, s_100, s_250, s_500, s_1000, s_2000],
    captions=["Negative", "+-100(5.5)", "+250(14)", "++500(28)", "+++1000(55)", "++++2000(111)"]
)

if sugar == s_neg:
    sugar = 0
elif sugar == s_100:
    sugar = 1
elif sugar == s_250:
    sugar = 2
elif sugar == s_500:
    sugar = 3
elif sugar == s_1000:
    sugar = 4
else:
    sugar = 5


# Blood levels

b_neg = resize_images(image_path="./images/Blood/neg.jpg", width=1, height=1)
b_trace = resize_images(image_path="./images/Blood/trace.jpg", width=1, height=1)
b_25 = resize_images(image_path="./images/Blood/25.jpg", width=1, height=1)
b_80= resize_images(image_path="./images/Blood/80.jpg", width=1, height=1)
b_200= resize_images(image_path="./images/Blood/200.jpg", width=1, height=1)
b_nh10 = resize_images(image_path="./images/Blood/nh10.jpg", width=50, height=50)
b_nh80 = resize_images(image_path="./images/Blood/nh80.jpg", width=50, height=50)

erythrocytes = image_select(use_container_width=False,
    label="🩸 Enter your blood results:",
    images=[b_neg, b_trace, b_25, b_80, b_200, b_nh10, b_nh80],
    captions=["Negative", "Hemolysis trace", "+25", "++80", "+++200", "Non-hemolysis + 10", "Non-hemolysis ++ 80"]
)

if erythrocytes == b_neg or b_trace:
    erythrocytes = 1
else:
    erythrocytes = 0

# Hypertension

hypertension = st.selectbox("📈 Do you have hypertension?",
                            ("Yes", "No"))
if hypertension == "Yes":
    hypertension = 1
elif hypertension == "No":
    hypertension = 0

# Submitting

if st.button("Submit your results"):

    st.success("Results submitted succesfully", icon="✅")
    insertSQL = f"""INSERT INTO samples
     (patientid, date, blood_pressure, albumin, sugar, erythrocytes, hypertension) 
        VALUES ('{patientid}', '{date}', '{blood_pressure}', '{albumin}', '{sugar}', '{erythrocytes}', '{hypertension}');
    """
    run_query(insertSQL)

