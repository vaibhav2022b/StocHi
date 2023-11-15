import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Page title and icon
st.set_page_config(
    page_title="Multipage App",
    page_icon="👻"
)
#Page main data
st.title("Stoc-Hi Pvt Ltd.")
st.write("Trading App - The app where you can check the instant history of company's stocks")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Animation

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_2u5mihz8.json")

st_lottie(
    lottie_hello,
    height = 500,
    width = 500,
    quality = "high",
)


