import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import pandas as pd
import requests
from streamlit_lottie import st_lottie
import time
import yfinance as yf



#User Authentication
names = ["Vaibhav Burkul","Saurabh Yenurkar"]
usernames =["Vaibhav", "Saurabh"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names , usernames , hashed_passwords, "sales_dashboard", "abcdef", cookie_expiry_days = 30)

names, authentication_status , usernames = authenticator.login("Login", "main")

if authentication_status == False:
    audio1 = open("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/very-infectious-laughter-meme-117727.mp3","rb")
    st.audio(audio1)
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_szusawu8.json")

    st_lottie(
        lottie_hello,
        height = None,
        width = 250,
        quality = "high",
    )

if authentication_status == None:
    st.warning("Please enter valid credentials")
if authentication_status:
    
    def get_input():
        st.header("Stoc-Hi Dashboard")
        Name = st.sidebar.text_input("E-mail","example@gmail.com")

        start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime("2012-01-01"))
        end_date = st.sidebar.date_input('End Date', value=pd.to_datetime("2022-01-01"))
        stock_symbol = st.sidebar.selectbox("Company Symbol",('EXMP','AMZN','TSLA','GOOG','SMSG','SBUX','SBIN.NS','HDFC.NS','AAPL','MSFT','META'))

        return start_date, end_date,stock_symbol, Name


    def get_company_name(symbol):
        if symbol == 'AMZN':
            return 'Amazon '
        elif symbol == 'TSLA':
            return 'Tesla'
        elif symbol == 'GOOG':
            return 'Alphabet '
        elif symbol == 'SMSG':
            return 'Samsung '
        elif symbol == 'SBUX':
            return 'Starbucks '
        elif symbol == 'SBIN.NS':
            return 'State Bank of India '
        elif symbol == 'HDFC.NS':
            return 'Housing Development Finance Corporation.Ltd '
        elif symbol =='AAPL':
            return 'Apple '
        elif symbol == 'META':
            return 'Facebook '
        elif symbol == 'MSFT':
            return 'Microsoft '
        elif symbol == 'EXMP':
            return 'Example'
        else:
            'None'




    def get_data(symbol, start, end):
        if symbol.upper() == 'AMZN':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/AMZN.csv")
        elif symbol.upper() == 'TSLA':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/TSLA.csv")
        elif symbol.upper() == 'GOOG':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/GOOG.csv")
        elif symbol.upper() == 'SMSG':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/005930.KS.csv")
        elif symbol.upper() == 'SBUX':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/SBUX.csv")
        elif symbol.upper() == 'SBIN.NS':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/SBIN.NS.csv")
        elif symbol.upper() == 'HDFC.NS':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/HDFCBANK.NS.csv")
        elif symbol.upper() == 'AAPL':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/AAPL.csv")
        elif symbol.upper() == 'META':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/META.csv")
        elif symbol.upper() == 'MSFT':
            df = pd.read_csv("C:/Users/Kiran/PycharmProjects/pythonProject/stocks/MSFT.csv")
        elif symbol.upper() == 'EXMP':
            st.warning("Enter your Email please")
            st.warning("Oops! You did not select the company symbol")
        else:
            df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])
        authenticator.logout("Logout", "sidebar")

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

        def get_ticker(name):
            company = yf.Ticker(name)
            return company

        if symbol == "AMZN":
            company=get_ticker("AMZN")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "TSLA":
            company = get_ticker("TSLA")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "GOOG":
            company = get_ticker("GOOG")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "SMSG":
            company = get_ticker("005930.KS")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "SBUX":
            company = get_ticker("SBUX")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol  == "SBIN.NS":
            company = get_ticker("SBIN.NS")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "HDFC.NS":
            company = get_ticker("HDFC.NS")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "AAPL":
            company = get_ticker("AAPL")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "META":
            company = get_ticker("META")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        elif symbol == "MSFT":
            company = get_ticker("MSFT")
            string_logo = '<img src=%s>' % company.info['logo_url']
            st.markdown(string_logo, unsafe_allow_html=True)
            st.subheader(company.info['longName'])
            st.success(company.info['longBusinessSummary'])
        else:
            st.success("No Data Found")

        start = pd.to_datetime(start)
        end = pd.to_datetime(end)


        start_row = 0
        end_row = 0

        for i in range(0, len(df)):
            if start <= pd.to_datetime(df['Date'][i]):
                start_row = i
                break

        for j in range(0, len(df)):
            if end >= pd.to_datetime(df['Date'][len(df) - 1 - j]):
                end_row = len(df) - 1 - j
                break

        df = df.set_index(pd.DatetimeIndex(df['Date'].values))

        return df.iloc[start_row:end_row + 1, :]


    start, end, symbol, Name = get_input()

    df = get_data(symbol, start, end)

    company_name = get_company_name(symbol.upper())

    st.balloons()


    st.header(company_name + "Open Price\n")
    st.line_chart(df['Open'])

    st.header(company_name + "Close Price\n")
    st.line_chart(df['Close'])

    st.header(company_name + "Volume\n")
    st.line_chart(df['Volume'])

    st.header('Data Statistics')
    st.write(df.describe())




