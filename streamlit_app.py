import numpy as np
import pandas as pd
import streamlit as st

email = st.text_area("Text to be analyzed",key='email')

btn1 = st.button('Analyse')

if btn1:
    st.write(email)
