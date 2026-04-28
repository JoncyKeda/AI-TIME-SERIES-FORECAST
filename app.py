import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.preprocess import prepare_data
from model.lstm_model import train_model, predict_future

st.set_page_config(page_title="AI Time Series Forecasting", layout="wide")

st.title("📈 AI Time Series Forecasting System (LSTM)")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Assume second column is value
    series = df.iloc[:, 1].values

    # Prepare data
    X, y, scaler = prepare_data(series)

    st.subheader("⚙️ Training Model...")
    model = train_model(X, y)

    # Predictions
    predictions = predict_future(model, X, scaler)

    st.subheader("📊 Forecast Results")

    fig, ax = plt.subplots()
    ax.plot(series, label="Actual")
    ax.plot(predictions, label="Predicted")
    ax.legend()

    st.pyplot(fig)
