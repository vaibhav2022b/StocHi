import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.title('About')
rad = st.radio("Navigation",['About','Support','Help'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}<style>',unsafe_allow_html=True)
if rad =='About':
    st.write("This app is made only for study purpose . Using this app you can check the previous 10 years history of company stocks , where you can compare the prize and volume of the previous year's stock and this year stock.")
    st.write("Live Compare feature allows you to compare the Close price and Volume of the different companies. ")
    st.write("Stock forecast feature help you to predict the price of stock.")

if rad =='Support':
    #st.image()
    st.write('Scan the QR code and the support the Patreon')
    import requests
    from streamlit_lottie import st_lottie


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_kop8vvlu.json")

    st_lottie(
        lottie_hello,
        height=None,
        width=400,
        quality="high",
    )
if rad == 'Help':

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_cykipy5n.json")
    st_lottie(
            lottie_hello,
            height = None,
            width = 250,
            quality = "high",
        )
    st.write('You can contact us on Discord : https://discord.gg/vaibhavstreamlit')