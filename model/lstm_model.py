from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_model(X, y):
    model = Sequential()
    model.add(LSTM(50, return_sequences=False, input_shape=(X.shape[1], 1)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=10, verbose=0)

    return model

def predict_future(model, X, scaler):
    preds = model.predict(X)
    return scaler.inverse_transform(preds)
