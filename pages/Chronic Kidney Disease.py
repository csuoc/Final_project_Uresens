import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header
import matplotlib.image as mpimg

# Head

st.set_page_config(page_title="Chronic Kidney Disease", page_icon="🩺")
add_logo("https://i.ibb.co/TTF105V/logo2.png")
add_text_sidebar()

colored_header(
    label="What is Chronic Kidney Disease?",
    description="Chronic kidney disease (CKD) is a long-term condition where the kidneys don't work as well as they should",
    color_name="red-70"
)

img = mpimg.imread("./images/CKD1.jpg")
st.image(img, use_column_width=True)

# Body

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

colored_header(
    label="Symptoms",
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

colored_header(
    label="Causes",
    description="Chronic kidney disease occurs when a disease or condition impairs kidney function, causing kidney damage to worsen over several months or years.",
    color_name="red-70"
)

st.write("Diseases and conditions that cause chronic kidney disease include:")

st.write("""
        - Type 1 or type 2 diabetes
        - High blood pressure
        - Glomerulonephritis (gloe-mer-u-low-nuh-FRY-tis), an inflammation of the kidney's filtering units (glomeruli)
        - Interstitial nephritis (in-tur-STISH-ul nuh-FRY-tis), an inflammation of the kidney's tubules and surrounding structures
        - Polycystic kidney disease or other inherited kidney diseases
        - Prolonged obstruction of the urinary tract, from conditions such as enlarged prostate, kidney stones and some cancers
        - Vesicoureteral (ves-ih-koe-yoo-REE-tur-ul) reflux, a condition that causes urine to back up into your kidneys
        - Recurrent kidney infection, also called pyelonephritis (pie-uh-low-nuh-FRY-tis)
        """)

colored_header(
    label="Risk factors",
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