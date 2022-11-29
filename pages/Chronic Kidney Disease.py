import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
import matplotlib.image as mpimg

########## Head ##########

st.set_page_config(page_title="Chronic Kidney Disease", page_icon="🤒")
add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

colored_header(
    label="❓ What is Chronic Kidney Disease?",
    description="Chronic kidney disease (CKD) is a long-term condition where the kidneys don't work as well as they should",
    color_name="red-70"
)

img = mpimg.imread("./images/CKD1.jpg")
st.image(img, use_column_width=True)

########## Body ##########

st.write("""
        **Chronic kidney disease**, also called chronic kidney failure, involves a gradual loss of kidney function. 
        Your kidneys filter wastes and excess fluids from your blood, which are then removed in your urine. 
        Advanced chronic kidney disease can cause dangerous levels of fluid, electrolytes and wastes to build up in your body. 
        In the early stages of chronic kidney disease, you might have few signs or symptoms. 
        You might not realize that you have kidney disease until the condition is advanced.
        Treatment for chronic kidney disease focuses on slowing the progression of kidney damage, usually by controlling the cause. 
        But, even controlling the cause might not keep kidney damage from progressing. 
        Chronic kidney disease can progress to end-stage kidney failure, which is fatal without artificial filtering (dialysis) 
        or a kidney transplant.
        """)

st.video("https://www.youtube.com/watch?v=za78Uqroios&t=104s&ab_channel=NationalKidneyFoundation")

########## Symptoms ##########

colored_header(
    label="❗ Symptoms",
    description="Signs and symptoms of chronic kidney disease develop over time if kidney damage progresses slowly.",
    color_name="red-70"
)

st.write("""
        Loss of kidney function can cause a buildup of fluid or body waste or electrolyte problems. 
        Depending on how severe it is, loss of kidney function can cause:
        """
        )

st.write("""
         - Nausea
         - Vomiting
         - Loss of apetite
         - Fatigue and weakness
         - Sleep problems
         - Urinating more or less
         - Decreased mental sharpness
         - Muscle cramps
         - Swelling of feet and ankles
         - Dry, itchy skin
         - High blood pressure (hypertension) that's difficult to control
         - Shortness of breath, if fluid builds up in the lungs
         - Chest pain, if fluid builds up around the lining of the heart
         """   )

st.write("""
        Signs and symptoms of kidney disease are often nonspecific. This means they can also be caused by other illnesses. 
        Because your kidneys are able to make up for lost function, you might not develop signs and symptoms until 
        irreversible damage has occurred.
        """
        )

########## Causes ##########

colored_header(
    label="🤔 Causes",
    description="Chronic kidney disease occurs when a disease or condition impairs kidney function, causing kidney damage to worsen over several months or years.",
    color_name="red-70"
)

st.write("Diseases and conditions that cause chronic kidney disease include:")

st.write("""
        - Type 1 or type 2 diabetes
        - High blood pressure
        - High coloresterol
        - Glomerulonephritis (gloe-mer-u-low-nuh-FRY-tis), an inflammation of the kidney's filtering units (glomeruli)
        - Interstitial nephritis (in-tur-STISH-ul nuh-FRY-tis), an inflammation of the kidney's tubules and surrounding structures
        - Polycystic kidney disease or other inherited kidney diseases
        - Prolonged obstruction of the urinary tract, from conditions such as enlarged prostate, kidney stones and some cancers
        - Vesicoureteral (ves-ih-koe-yoo-REE-tur-ul) reflux, a condition that causes urine to back up into your kidneys
        - Recurrent kidney infection, also called pyelonephritis (pie-uh-low-nuh-FRY-tis)
        """)

########## Risk factors ##########

colored_header(
    label="📊 Risk factors",
    description="",
    color_name="red-70"
)

st.write("Factors that can increase your risk of chronic kidney disease include:")

st.write("""
        - Diabetes
        - High blood pressure
        - Heart (cardiovascular) disease
        - Smoking
        - Obesity
        - Being Black, Native American or Asian American
        - Family history of kidney disease
        - Abnormal kidney structure
        - Older age
        - Frequent use of medications that can damage the kidneys
        """)

########## Complications ##########

colored_header(
    label="🩹 Complications",
    description="",
    color_name="red-70"
)

st.write("Chronic kidney disease can affect almost every part of your body. Potential complications include:")

st.write("""
        - Fluid retention, which could lead to swelling in your arms and legs, high blood pressure, or fluid in your lungs (pulmonary edema)
        - A sudden rise in potassium levels in your blood (hyperkalemia), which could impair your heart's function and can be life-threatening
        - Anemia
        - Heart disease
        - Weak bones and an increased risk of bone fractures
        - Decreased sex drive, erectile dysfunction or reduced fertility
        - Damage to your central nervous system, which can cause difficulty concentrating, personality changes or seizures
        - Decreased immune response, which makes you more vulnerable to infection
        - Pericarditis, an inflammation of the saclike membrane that envelops your heart (pericardium)
        - Pregnancy complications that carry risks for the mother and the developing fetus
        - Irreversible damage to your kidneys (end-stage kidney disease), eventually requiring either dialysis or a kidney transplant for survival
        """)

########## Prevention ##########

colored_header(
    label="💡 Prevention",
    description="",
    color_name="red-70"
)

st.write("To reduce your risk of developing kidney disease:")

st.write("""
        - **Follow instructions on over-the-counter medications**. When using nonprescription pain relievers, such as aspirin, ibuprofen (Advil, Motrin IB, others) and acetaminophen (Tylenol, others), follow the instructions on the package. Taking too many pain relievers for a long time could lead to kidney damage.
        - **Maintain a healthy weight**. If you're at a healthy weight, maintain it by being physically active most days of the week. If you need to lose weight, talk with your doctor about strategies for healthy weight loss.
        - **Don't smoke**. Cigarette smoking can damage your kidneys and make existing kidney damage worse. If you're a smoker, talk to your doctor about strategies for quitting. Support groups, counseling and medications can all help you to stop.
        - **Manage your medical conditions with your doctor's help**. If you have diseases or conditions that increase your risk of kidney disease, work with your doctor to control them. Ask your doctor about tests to look for signs of kidney damage.
        """)

########## Tests for CKD ##########

colored_header(
    label="🔬 Tests for CKD",
    description="",
    color_name="red-70"
)

st.write("""
         CKD can be diagnosed using **blood and urine tests**. These tests look for high levels of certain substances in your blood and urine that are signs your kidneys aren't working properly.
         If you're at a high risk of developing kidney disease (for example, you have a known risk factor such as high blood pressure or diabetes), you may be advised to have regular tests to check for CKD so it's found at an early stage.
         The results of your blood and urine tests can be used to tell the stage of your kidney disease. This is a number that reflects how severe the damage to your kidneys is, with a higher number indicating more serious CKD.
        """)

st.subheader("Blood test")
st.write("""The main test for kidney disease is a blood test. The test measures the levels of a waste product called creatinine in your blood.
        Your doctor uses your blood test results, plus your age, size, gender and ethnic group to calculate how many millilitres of waste your kidneys should be able to filter in a minute.
        This calculation is known as your estimated glomerular filtration rate (eGFR).
        Healthy kidneys should be able to filter more than 90ml/min. You may have CKD if your rate is lower than this.
        """)

st.subheader("Urine test")
st.write("""
        A urine test is also done to:
        - check the levels of substances called albumin and creatinine in your urine – known as the albumin:creatinine ratio, or ACR
        - check for blood or protein in your urine
        Alongside your eGFR, urine tests can help give a more accurate picture of how well your kidneys are working.
        """)

st.subheader("Other tests")
st.write("""
        Sometimes other tests are also used to assess the level of damage to your kidneys.
        These may include:
        - an ultrasound scan, MRI scan or CT scan – to see what the kidneys look like and check whether there are any blockages
        - a kidney biopsy – a small sample of kidney tissue is removed using a needle and the cells are examined under a microscope for signs of damage
        """)

########## Test results ##########

colored_header(
    label="📚 Test results and stages of CKD",
    description="Your test results can be used to determine how damaged your kidneys are, known as the stage of CKD.",
    color_name="red-70"
)

st.write("Your eGFR results is given as a stage from 1 of 5:")

st.write("""
        - **Stage 1 (G1)**: a normal eGFR above 90ml/min, but other tests have detected signs of kidney damage
        - **Stage 2  (G2)**: a slightly reduced eGFR of 60 to 89ml/min, with other signs of kidney damage
        - **Stage 3a (G3a)**: an eGFR of 45 to 59ml/min
        - **Stage 3b (G3b)**: an eGFR of 30 to 44ml/min
        - **Stage 4 (G4)**: an eGFR of 15 to 29ml/min
        - **stage 5 (G5)**: an eGFR below 15ml/min, meaning the kidneys have lost almost all of their function
        """)

st.write("Your ACR result is given as a stage from 1 to 3:")

st.write("""
        - **A1**: an ACR of less than 3mg/mmol
        - **A2**: an ACR of 3 to 30mg/mmol
        - **A3**: an ACR of more than 30mg/mmol
        """)

st.write("For both eGFR and ACR, a higher stage indicates more severe kidney disease.")

########## Overview ##########

colored_header(
    label="📜 Overview",
    description="",
    color_name="red-70"
)

st.write("""
        CKD can range from a mild condition with no or few symptoms, to a very serious condition where the kidneys stop working, sometimes called kidney failure.
        Most people with CKD will be able to control their condition with medicine and regular check-ups. CKD only progresses to kidney failure in around 1 in 50 people with the condition.
        If you have CKD, even if it's mild, you're at an increased risk of developing other serious problems, such as cardiovascular disease. This is a group of conditions affecting the heart and blood vessels, which includes heart attack and stroke.
        Cardiovascular disease is one of the main causes of death in people with kidney disease, although healthy lifestyle changes and medicine can help reduce your risk of developing it.
        """
        )

########## Sources ##########

colored_header(
    label="➡ Sources",
    description="",
    color_name="red-70"
)

st.write("""
        - Kidney.org: https://www.kidney.org/atoz/content/about-chronic-kidney-disease
        - Mayo Clinic: https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521
        - NHS.co.uk: https://www.nhs.uk/conditions/kidney-disease/
        """)