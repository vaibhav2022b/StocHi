import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Live Dashboard')

tickers = ('TSLA','AAPL','GOOG','AMZN','SBIN.NS','MSFT','HDFC.NS','BTC.USD','ETH.USD','META', '005930.KS','SBUX')
dropdown = st.multiselect('Company Name',tickers)

start = st.date_input('Start',value=pd.to_datetime("2021-01-01"))
end = st.date_input('End',value=pd.to_datetime("2022-09-09"))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod()-1
    cumret= cumret.fillna(0)
    return cumret


if len(dropdown)>0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header('Close price of {} '.format(dropdown))
    st.line_chart(df)
    df = relativeret(yf.download(dropdown,start, end)['Volume'])
    st.header('Volume of {}'.format(dropdown))
    st.line_chart(df)

