import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express

df = pd.read_csv("")

st.set_page_config(
    page_title='Real-Time Data Science Dashboard',
    page_icon='(:',
    layout = 'wide'
)

st.title("Real-Time/Live Data Science Dashboard")
job_filter = st.selectbox("Select the job",pd.unique(df['job']))
placeholder = st.empty()

df = df[df['job']==job_filter]