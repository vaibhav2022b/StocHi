import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
#from fbprophet import Prophet
#from fbprophet.plot import plot_plotly
import requests
from streamlit_lottie import st_lottie

#def load_lottieurl(url: str):
    #r = requests.get(url)
    #if r.status_code != 200:
        #return None
    #return r.json()


#lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_10jxod3a.json")

#st_lottie(
    #lottie_hello,
    #=None,
    #width=None,
    #quality="high",
#)
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock predication")

stocks = ('TSLA','AAPL','GOOG','AMZN','SBIN.NS','MSFT','HDFC.NS','BTC.USD','ETH.US')
selected_stock = st.selectbox("Select Ticker", stocks)

n_years = st.slider("Years of prediction:",1,4)
period = n_years*365

@st.cache
def load_data(ticker):
    data = yf.download(ticker,START,TODAY )
    data.reset_index(inplace=True)
    return data
data_load_state = st.text("Load Data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...")

st.subheader("Stock Data")
st.write(data.tail())

def plot_stock_data():
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data["Date"],y=data["Open"],name="Stock_Open"))
    fig1.add_trace(go.Scatter(x=data["Date"],y=data["Close"],name="Stock_Close"))
    #fig1.add_trace(go.Scatter(x=data["Date"], y=data["Volume"], name="Stock_Volume"))
    fig1.layout.update(title_text="Time Series data",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig1)

plot_stock_data()

#Forerecating
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date":"ds","Close":"y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast Data")
st.write(forecast.tail())


st.write("Forecast Data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast Components")
fig2 = m.plot_components(forecast)
st.write(fig2)
