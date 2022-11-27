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

# Hypertension

hypertension = st.selectbox("📈 Do you have hypertension?",
                            ("Yes", "No"))
if hypertension == "Yes":
    hypertension = 1
elif hypertension == "No":
    hypertension = 0

# Leucocytes

l_neg = resize_images(image_path="./images/Leucocytes/neg.jpg", width=1, height=1)
l_trace = resize_images(image_path="./images/Leucocytes/trace.jpg", width=1, height=1)
l_70 = resize_images(image_path="./images/Leucocytes/70.jpg", width=1, height=1)
l_125 = resize_images(image_path="./images/Leucocytes/125.jpg", width=1, height=1)
l_500 = resize_images(image_path="./images/Leucocytes/500.jpg", width=1, height=1)

leucocytes = image_select(use_container_width=False,
    label="⚔ Select your LEUCOCYTE results:",
    images=[l_neg, l_trace, l_70, l_125, l_500],
    captions=["Negative", "Trace levels", "+70", "++125", "+++500"]
)

if leucocytes == l_neg:
    leucocytes = 0
elif leucocytes == l_trace:
    leucocytes = 0
elif leucocytes == l_70:
    leucocytes = 70
elif leucocytes == l_125:
    leucocytes = 125
else:
    leucocytes = 500

# Nitrite

n_neg = resize_images(image_path="./images/Nitrite/neg.jpg", width=1, height=1)
n_trace = resize_images(image_path="./images/Nitrite/trace.jpg", width=1, height=1)
n_pos = resize_images(image_path="./images/Nitrite/pos.jpg", width=1, height=1)

nitrite = image_select(use_container_width=False,
    label="🦠 Select your NITRITE results:",
    images=[n_neg, n_trace, n_pos],
    captions=["Negative", "Trace levels", "Positive"]
)

if nitrite == n_neg:
    nitrite = 0
elif nitrite == n_trace:
    nitrite = 0
else:
    nitrite = 1

# Urobilinogen

u_01 = resize_images(image_path="./images/Urobilinogen/0.1.jpg", width=1, height=1)
u_1 = resize_images(image_path="./images/Urobilinogen/1.jpg", width=1, height=1)
u_2 = resize_images(image_path="./images/Urobilinogen/2.jpg", width=1, height=1)
u_4 = resize_images(image_path="./images/Urobilinogen/4.jpg", width=1, height=1)
u_8 = resize_images(image_path="./images/Urobilinogen/8.jpg", width=1, height=1)

urobilinogen = image_select(use_container_width=False,
    label="🤢 Select your UROBILINOGEN results:",
    images=[u_01, u_1, u_2, u_4, u_8],
    captions=["0.1", "1(16)", "2(33)", "4(66)", "8(131)"]
)

# Sugar

s_neg = resize_images(image_path="./images/Sugar/neg.jpg", width=1, height=1)
s_100 = resize_images(image_path="./images/Sugar/100.jpg", width=1, height=1)
s_250 = resize_images(image_path="./images/Sugar/250.jpg", width=1, height=1)
s_500= resize_images(image_path="./images/Sugar/500.jpg", width=1, height=1)
s_1000 = resize_images(image_path="./images/Sugar/1000.jpg", width=1, height=1)
s_2000 = resize_images(image_path="./images/Sugar/2000.jpg", width=1, height=1)

sugar = image_select(use_container_width=False,
    label="🍭 Select your GLUCOSE results:",
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

# pH

ph_5 = resize_images(image_path="./images/pH/5.jpg", width=1, height=1)
ph_6 = resize_images(image_path="./images/pH/6.jpg", width=1, height=1)
ph_65 = resize_images(image_path="./images/pH/6.5.jpg", width=1, height=1)
ph_7 = resize_images(image_path="./images/pH/7.jpg", width=1, height=1)
ph_75 = resize_images(image_path="./images/pH/7.5.jpg", width=1, height=1)
ph_8 = resize_images(image_path="./images/pH/8.jpg", width=1, height=1)
ph_85 = resize_images(image_path="./images/pH/8.5.jpg", width=1, height=1)

ph = image_select(use_container_width=False,
    label="🌡 Select your pH levels:",
    images=[ph_5, ph_6, ph_65, ph_7, ph_75, ph_8, ph_85],
    captions=["5", "6", "6.5", "7", "7.5", "8", "8.5"]
)

if ph == ph_5:
    ph = 5
elif ph == ph_6:
    ph = 6
elif ph == ph_65:
    ph = 6.5
elif ph == ph_7:
    ph = 7
elif ph == ph_75:
    ph = 7.5
elif ph == ph_8:
    ph = 8
else:
    ph = 8.5

# Specific gravity

g_1000 = resize_images(image_path="./images/Specific Gravity/1.000.jpg", width=1, height=1)
g_1005 = resize_images(image_path="./images/Specific Gravity/1.005.jpg", width=1, height=1)
g_1010 = resize_images(image_path="./images/Specific Gravity/1.010.jpg", width=1, height=1)
g_1015 = resize_images(image_path="./images/Specific Gravity/1.015.jpg", width=1, height=1)
g_1020 = resize_images(image_path="./images/Specific Gravity/1.020.jpg", width=1, height=1)
g_1025 = resize_images(image_path="./images/Specific Gravity/1.025.jpg", width=1, height=1)
g_1030 = resize_images(image_path="./images/Specific Gravity/1.030.jpg", width=1, height=1)

gravity = image_select(use_container_width=False,
    label="⚖ Select your SPECIFIC GRAVITY results:",
    images=[g_1000, g_1005, g_1010, g_1015, g_1020, g_1025, g_1030],
    captions=["1.000", "1.005", "1.010", "1.015", "1.020", "1.025", "1.030"]
)

if gravity == g_1000:
    gravity = 1.000
elif gravity == g_1005:
    gravity = 1.005
elif gravity == g_1010:
    gravity = 1.010
elif gravity == g_1015:
    gravity = 1.015
elif gravity == g_1020:
    gravity = 1.020
elif gravity == g_1025:
    gravity = 1.025
else:
    gravity = 1.030

# Blood levels

b_neg = resize_images(image_path="./images/Blood/neg.jpg", width=1, height=1)
b_trace = resize_images(image_path="./images/Blood/trace.jpg", width=1, height=1)
b_25 = resize_images(image_path="./images/Blood/25.jpg", width=1, height=1)
b_80= resize_images(image_path="./images/Blood/80.jpg", width=1, height=1)
b_200= resize_images(image_path="./images/Blood/200.jpg", width=1, height=1)
b_nh10 = resize_images(image_path="./images/Blood/nh10.jpg", width=50, height=50)
b_nh80 = resize_images(image_path="./images/Blood/nh80.jpg", width=50, height=50)

erythrocytes = image_select(use_container_width=False,
    label="🩸 Enter your BLOOD results:",
    images=[b_neg, b_trace, b_25, b_80, b_200, b_nh10, b_nh80],
    captions=["Negative", "Hemolysis trace", "+25", "++80", "+++200", "Non-hemolysis + 10", "Non-hemolysis ++ 80"]
)

if erythrocytes == b_neg or b_trace:
    erythrocytes = 1
else:
    erythrocytes = 0

# Ketones

k_neg = resize_images(image_path="./images/Ketones/neg.jpg", width=1, height=1)
k_5 = resize_images(image_path="./images/Ketones/5.jpg", width=1, height=1)
k_15 = resize_images(image_path="./images/Ketones/15.jpg", width=1, height=1)
k_40 = resize_images(image_path="./images/Ketones/40.jpg", width=1, height=1)
k_80 = resize_images(image_path="./images/Ketones/80.jpg", width=1, height=1)
k_160 = resize_images(image_path="./images/Ketones/160.jpg", width=1, height=1)

ketones = image_select(use_container_width=False,
    label="💅 Enter your KETONE results:",
    images=[k_neg, k_5, k_15, k_40, k_80, k_160],
    captions=["Negative", "+-5(0.5)", "+15(1.5)", "++40(3.9)", "+++80(8)", "++++160(16)"]
)

if ketones == k_neg:
    ketones = 0
elif ketones == k_5:
    ketones = 5
elif ketones == k_15:
    ketones = 15
elif ketones == k_40:
    ketones = 40
elif ketones == k_80:
    ketones = 80
else:
    ketones = 160

# Bilirubin

b_neg = resize_images(image_path="./images/Bilirubin/neg.jpg", width=1, height=1)
b_p = resize_images(image_path="./images/Bilirubin/+.jpg", width=1, height=1)
b_pp = resize_images(image_path="./images/Bilirubin/++.jpg", width=1, height=1)
b_ppp = resize_images(image_path="./images/Bilirubin/+++.jpg", width=1, height=1)

bilirubin = image_select(use_container_width=False,
    label="💩 Select your BILIRUBIN results:",
    images=[b_neg, b_p, b_pp, b_ppp],
    captions=["Negative", "+", "++", "+++"]
)

if bilirubin == b_neg:
    bilirubin = 0
elif bilirubin == b_p:
    bilirubin = 1
elif bilirubin == b_pp:
    bilirubin = 2
else:
    bilirubin = 3

# Protein

a_neg = resize_images(image_path="./images/Protein/neg.jpg", width=1, height=1)
a_trace = resize_images(image_path="./images/Protein/trace.jpg", width=1, height=1)
a_30 = resize_images(image_path="./images/Protein/30.jpg", width=1, height=1)
a_100= resize_images(image_path="./images/Protein/100.jpg", width=1, height=1)
a_300 = resize_images(image_path="./images/Protein/300.jpg", width=1, height=1)
a_1000 = resize_images(image_path="./images/Protein/1000.jpg", width=1, height=1)

albumin = image_select(use_container_width=False,
    label="🥚 Select your PROTEIN results:",
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








# Submitting

if st.button("Submit your results"):

    st.success("Results submitted succesfully", icon="✅")
    insertSQL = f"""INSERT INTO samples
     (patientid, date, blood_pressure, albumin, sugar, erythrocytes, hypertension, leucocytes, nitrite, 
     urobilinogen, ph, gravity, ketones, bilirubin) 
        VALUES ('{patientid}', '{date}', '{blood_pressure}', '{albumin}', '{sugar}', '{erythrocytes}', 
                '{hypertension}', '{leucocytes}', '{nitrite}', '{urobilinogen}', '{ph}', '{gravity}',
                '{bilirubin}');
    """
    run_query(insertSQL)

