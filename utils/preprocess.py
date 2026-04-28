import numpy as np
from sklearn.preprocessing import MinMaxScaler

def prepare_data(data, window=5):
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data.reshape(-1, 1))

    X, y = [], []

    for i in range(len(data) - window):
        X.append(data[i:i+window])
        y.append(data[i+window])

    return np.array(X), np.array(y), scaler
