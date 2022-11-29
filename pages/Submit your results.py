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
add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

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
    label="📧 Submit your results",
    description="Only for in vitro diagnostic",
    color_name="red-70"
)

st.write("""**Urine strips** are test strips for in vitro diagnostic use only and for the rapid testing of different compounds in urine, such
        as **Leucocytes, Nitrites, Proteins, pH, Blood, Specific gravity, Ketones, Bilirubin, Glucose, Microalbumin and Creatinin**. 
        The test result can provide information on the status of carbohydrate metabolism, kidney and liver function, acid-base balance 
        and urinary tract infections. They are interpreted by comparing each colour of the strip with the included colour chart. 
        The strips can be read visually or instrumentally, using professional urine chemistry analysers.
        """
        )

img = mpimg.imread("./images/urinetest.jpg")
st.image(img, use_column_width=True)

st.write('**Please fill the following form. Input the required parameters marked with a "*". Then select the resulting color of each component in your sample**')

########## Insert into MySQL ##########

# Name

patientid = st.text_input("🧍‍♂️🧍‍♀️ Who are you?*")

# Date

date = st.date_input("🗓 Input the current date*")

#Blood pressure

blood_pressure = st.number_input("🩺 Enter your blood pressure value (diastolic):*", 0, 200)

# Hypertension

hypertension = st.selectbox("📈 Have you been diagnosed with hypertension?*",
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

if urobilinogen == u_01:
    urobilinogen = 0.1
elif urobilinogen == u_1:
    urobilinogen = 1
elif urobilinogen == u_2:
    urobilinogen = 2
elif urobilinogen == u_4:
    urobilinogen = 4
else:
    urobilinogen = 8

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


# Microalbumin

m_1 = resize_images(image_path="./images/Microalbumin/1.jpg", width=1, height=1)
m_3 = resize_images(image_path="./images/Microalbumin/3.jpg", width=1, height=1)
m_8 = resize_images(image_path="./images/Microalbumin/8.jpg", width=1, height=1)
m_15 = resize_images(image_path="./images/Microalbumin/15.jpg", width=1, height=1)

microalbumin = image_select(use_container_width=False,
    label="🤏🥚 Select your MICROALBUMIN results:",
    images=[m_1, m_3, m_8, m_15],
    captions=["1(10)", "3(30)", "8(80)", "15(150)"]
)

if microalbumin == m_1:
    microalbumin = 1
elif microalbumin == m_3:
    microalbumin = 3
elif microalbumin == m_8:
    microalbumin = 8
else:
    microalbumin = 15

# Creatinine

c_10 = resize_images(image_path="./images/Creatinine/10.jpg", width=1, height=1)
c_50 = resize_images(image_path="./images/Creatinine/50.jpg", width=1, height=1)
c_100 = resize_images(image_path="./images/Creatinine/100.jpg", width=1, height=1)
c_200 = resize_images(image_path="./images/Creatinine/200.jpg", width=1, height=1)
c_300 = resize_images(image_path="./images/Creatinine/300.jpg", width=1, height=1)

creatinine = image_select(use_container_width=False,
    label="💪 Select your CREATININE results:",
    images=[c_10, c_50, c_100, c_200, c_300],
    captions=["10(0.1)0.9", "50(0.5)4.4", "100(1.0)8.8", "200(2.0)17.7", "300(3.0)26.5"]
)

if creatinine == c_10:
    creatinine = 10
elif creatinine == c_50:
    creatinine = 50
elif creatinine == c_100:
    creatinine = 100
elif creatinine == c_200:
    creatinine = 200
else:
    creatinine = 300

# Submitting

st.markdown("**Once you're finished, don't forget to click on the Submit button!**")
st.write("👇👇👇")

if st.button("**SUBMIT YOUR RESULTS**"):

    st.success("Results submitted succesfully", icon="✅")
    insertSQL = f"""INSERT INTO samples
     (patientid, date, blood_pressure, albumin, sugar, erythrocytes, hypertension, leucocytes, nitrite, 
     urobilinogen, ph, gravity, ketones, bilirubin, microalbumin, creatinine, micro_creat_ratio) 
        VALUES ('{patientid}', '{date}', '{blood_pressure}', '{albumin}', '{sugar}', '{erythrocytes}', 
                '{hypertension}', '{leucocytes}', '{nitrite}', '{urobilinogen}', '{ph}', '{gravity}',
                '{ketones}', '{bilirubin}', '{microalbumin}', '{creatinine}', '{microalbumin/creatinine}');
    """
    run_query(insertSQL)

# Information
st.write("\n")
st.write("\n")

colored_header(
    label="📃 Technical information about the procedures and components",
    description="",
    color_name="red-70"
)

st.write("""
        **Urobilinogen**: The test is based on the Ehrlich reaction. The colour changes from light orange-pink to dark pink.
        Ingredients: 4-Methoxy-benzene diazonium 2,9 mg.
        """
        )

st.write("""
        **Glucose**: Glucose oxidase catalyses the oxidation of glucose to form hydrogen peroxide. The hydrogen peroxide thus formed then oxidises a chromogen on the reactive pad by the action of peroxidase.
        Ingredients: Glucose oxidase 430U, Peroxidase 200U, Potassium iodide 12 mg
        """
        )

st.write("""
        **Bilirubin**: Azo coupling reaction of bilirubin with a diazonium salt in an acid medium to form an azo dye. The colour changes from light brown to beige or light pink.
        Ingredients: Sodium nitrite 0.733 mg, 2,4-dizionium dichlorobezene 2.3 mg, Sulfosalicílic acid 25 mg.
        """
        )

st.write("""
        **Ketones**: Legal test - nitroprusside reaction. Acetoacetic acid in an alkaline medium reacts with nitroferricanide to produce a beige to purple colour change.
        Ingredients: Sodium nitroprusside 23.0 mg.
        """
        )

st.write("""
        **pH**: Dual indicator system. The indicator methyl red and bromothymol blue are used to give distinct colour changes from orange to green to blue (pH 5.0 to 9.0).
        Ingredients: Methyl red 0.05 mg, Bromothymol blue 0.5 mg
        """
        )

st.write("""
        **Blood**: The test is based on the pseudo-peroxidase activity of the heme fraction of haemoglobin and myoglobin. The chromogen is oxidised by a hydroperoxide in the presence of heme and changes colour from yellow to blue.
        Ingredients: Coumene hydroperoxide 12 mg, o-Tolidine 0.5 mg
        """
        )

st.write("""
        **Specific gravity (SG)**: Ionic solutes in urine cause the release of protons from a polyelectrolyte. As the protons are released the pH decreases and produces a colour change in bromothymol blue from green-blue to yellow-green.
        Ingredients: Bromothymol blue 0.5 mg
        Poly vinyl ether - ALT anhydrous maleic acid 140.5 mg
        """
        )

st.write("""
        **Proteins**: Protein "indicator error". When the pH is kept constant by means of a buffer, the indicator dyes H+ ions due to the presence of the protein and the colour changes from yellow (or yellow-green) to blue-green.
        Ingredients: Tetrabromophenol blue 0.34 mg
        """
        )

st.write("""
        **Nitrite**: The test is based on the diazotization reaction of nitrite with an aromatic amine to produce a diazionium salt. This is followed by an azo coupling reaction of this diazonium salt with an aromatic compound on the reagent pad. The azo dye produced causes a colour change from white to pink.
        Ingredients: p-arsan lico acid 4.5 mg
        """
        )

st.write("""
        **Leukocytes**: This test pad contains a deindoxyl ester and diazonium salt. This is followed by an azo coupling reaction of the aromatic amine formed by leucocyte esterase with a diazonium salt on the reagent pad. The azo dye produced causes a colour change from beige to violet.
        Ingredients: Induced amino indole acid ether 1.3 mg
        """
        )

st.write("""
        **Microalbumin**: This test is based on the binding of the dye with sulphonaphthalein dye. At a constant pH, the albumin binds with the sulphonaphthalein dye to develop a blue colour. The resulting colour varies from pale green to aquamarine blue.
        Ingredients: 2,6-dichloro indophenol sodium salt 0.8 mg
        """
        )

st.write("""
        **Creatinine**: This test is based on the reaction of creatinine with a dye/metal complex. In alkaline conditions, creatinine reacts with a dye-metal complex to form a purplish-brown complex.
        Ingredients: picric acid 0.3 mg, borax 20 mg
        """
        )

# Limitations
st.write("\n")

colored_header(
    label="💡 Limitations",
    description="",
    color_name="red-70"
)
st.write("**Urobilinogen**: The absence of urobilinogen in the sample cannot be determined. The test area reacts with interfering substances known to react with the Ehrlich reagent, such as p-aminosalicylic acid. Drugs containing azo-ganstrisin may give a masking golden colour. The test is not a reliable method for the detection of porphobilinogen.")
st.write("**Glucose**: a high Specific Gravity (> 1.020) with high pH urine and ascorbic acid (greater than 40 mg/dL) may give a false negative for samples containing a small amount of glucose (100 mg/dL). Reactivity may be influenced by urine EG and temperature.")
st.write("**Bilirubin**: Drug metabolites, such as pyridium and selenium, which give a colour at low pH, can cause false positives. Indoxyl sulphate (indicate) can produce a yellow-orange to red colour response, which can interfere with the interpretation of negative or positive bilirubin readings. Ascorbic acid (>30 mg/dL) may cause false negative results.")
st.write("**Ketones**: Positive results (trace or less) may occur with highly pigmented urine samples or samples containing large amounts of levodopa metabolites. Some urines with high SG and low pH may give a false positive result. Phenolsulfonphthalein may cause false positives.")
st.write("**Blood**: Elevated specific gravity or protein in the urine may reduce the reactivity of the blood test portion. Microbial peroxidase associated with urinary tract infection may cause false positive results. Ascorbic acid concentrations (>30 mg/dL) may cause false negatives in the low blood level.")
st.write("**Specific gravity (SG)**: Highly buffered alkaline urine may cause decreased results, while highly buffered acidic urine may cause slightly elevated results.")
st.write("**Proteins**: False positive results can be found in strongly basic urine (pH 9). Interpretation of results is also difficult in cloudy urine samples.")
st.write("**Nitrite**: Ascorbic acid (> 30 mg/dL) may cause false negative results with low levels of nitrite content (<0.03 mg) in the urine. A negative result does not always mean that the patient is free of bacteriuria. Pink spots or pink borders should not be interpreted as a positive result. A negative result may occur when urinary tract infections are caused by organisms that do not contain nitrate reductase, when urine has not been retained in the bladder long enough (four hours or more) for reduction of nitrate to nitrite, or when nitrate in the diet is absent.")
st.write("**Leukocytes**: The test result may not always be consistent with the number of leukocyte cells from a microscopic examination. High glucose concentration, high specific gravity, high albumin level, high formaldehyde concentration or the presence of blood may cause decreased test results. False positive results may occasionally be due to contamination of the sample by vaginal discharge.")
st.write("**Microalbumin**: The following substances may cause false positive results: a large amount of hemoglobin (> 5 mg/dL), visibly bloody urine, highly alkaline urine (pH > 8), or disinfectant including quaternary ammonium compound.")
st.write("**Creatinine**: dark brown urine may affect the results. Substances that cause abnormal urine colour, such as medications containing azo dyes, nitrofurantoin and riboflavin, may affect the results.")
st.write("**Microalbumin to creatinine ratio**: A low microalbumin result (10 mg/L) in combination with strongly dilute urine (creatinine result of 10 mg/dL) may indicate a microalbumin concentration below the limit of sensitivity. In this case, consider testing a new sample, preferably a first collection in the morning, in order to have more confidence in the result.")