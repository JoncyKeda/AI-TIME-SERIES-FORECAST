import matplotlib.pyplot as plt

def plot_results(actual, predicted):
    plt.figure(figsize=(10,5))
    plt.plot(actual, label="Actual")
    plt.plot(predicted, label="Predicted")
    plt.legend()
    plt.title("Time Series Forecast")
    plt.show()
