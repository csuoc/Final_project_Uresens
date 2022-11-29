# Import box

import streamlit as st
import mysql.connector
from streamlit_extras.app_logo import add_logo
from functions.functions import add_text_sidebar
from streamlit_extras.colored_header import colored_header

########## Head ##########

st.set_page_config(page_title="Instructions", page_icon="📄")
add_logo("https://i.ibb.co/kcSSdhP/logo2.png")
add_text_sidebar()
st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


colored_header(
    label="Instructions",
    description="",
    color_name="red-70"
)

st.image("./images/urinetest2.jpg")

########## Info ##########

st.subheader("Information about sample collection and preparation")
st.write("""Collect urine in a **clean, dry container** that allows **complete immersion** of all fields of the test strip. 
        Do not add preservatives. **Test the sample as soon as possible**, with the sample well mixed but not centrifuged. 
        The use of fresh morning urine is recommended for optimal nitrite testing, as well as for the valid 
        determination of bilirubin and urobilinogen, as these compounds are unstable when exposed to light.
        """
        ) 
st.write("""
        **If immediate testing is not possible, the sample should be stored in the refrigerator**, but not frozen, 
        and then brought to room temperature before use for testing. Unpreserved room temperature urine may be 
        subject to pH changes due to microbial growth, which may interfere with protein determination. 
        If cleanly voided samples are not collected from females, positive results may be found for leukocytes 
        due to external contamination of the urinary tract. Skin cleansers containing chlorhexidine may affect 
        protein test results if contamination of the sample occurs.
        """
        )
st.video("./videos/introsample.mp4")

########## Visual test ##########

st.subheader("Procedure to perform an urine test")

# Step 1
st.write("""
        The procedure must be followed exactly to achieve reliable results. Do not compare the strips with the 
        colour chart before dipping the strip into the urine.

        1. **Dip the strip** into the urine up to the test area for no more than two seconds.
        2. **Rest the edge of the strip** along the rim of the container to remove excess urine; at this time, do not make the test areas touch the rim of the container. Turn the strip on its side and touch the strip once on an absorbent cloth to remove any remaining urine; excess urine on the strip may cause an interaction of chemicals between two adjacent test pads, so that an incorrect result may be produced.
        """)
st.video("./videos/1-dipstrip.mp4")

# Step 2
st.write("""
        3. **Compare the colours** of the pads after 60 seconds (for leucocytes after 90 - 120 seconds) with the colour chart on the container label, in good light. During the comparison, keep the strip horizontal to avoid possible mixing of chemicals if there is excess urine.
        """
        )
st.video("./videos/2-reading.mp4")

# Step 3
st.write("""
        4. **Input data**
        """
        )
st.video("./videos/3-howtosubmitdata.webm")