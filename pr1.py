import json
import numpy as np
from sklearn.linear_model import LinearRegression

def train_linear_regression_model(data):
    X = np.array([[day["temperature"]] for day in data])
    y = np.array([day["next_day_temperature"] for day in data])

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_temperature(model, today_temperature):
    return model.predict([[today_temperature]])[0]

def decide_to_bring_umbrella(predicted_temperature, threshold=20):
    if predicted_temperature <= threshold:
        return "Bring Umbrella"
    else:
        return "Don't Bring Umbrella"

def main():
    # Example JSON data with 10 rows
    json_data = '''
    {
        "historical_data": [
            {"day": "2024-01-01", "temperature": 25.0, "next_day_temperature": 24.0},
            {"day": "2024-01-02", "temperature": 24.5, "next_day_temperature": 23.8},
            {"day": "2024-01-03", "temperature": 23.8, "next_day_temperature": 22.5},
            {"day": "2024-01-04", "temperature": 22.0, "next_day_temperature": 21.2},
            {"day": "2024-01-05", "temperature": 21.5, "next_day_temperature": 20.0},
            {"day": "2024-01-06", "temperature": 20.2, "next_day_temperature": 19.5},
            {"day": "2024-01-07", "temperature": 19.8, "next_day_temperature": 18.5},
            {"day": "2024-01-08", "temperature": 18.3, "next_day_temperature": 17.5},
            {"day": "2024-01-09", "temperature": 17.5, "next_day_temperature": 16.0},
            {"day": "2024-01-10", "temperature": 16.0, "next_day_temperature": 15.5}
        ]
    }
    '''
    data = json.loads(json_data)["historical_data"]

    # Train the linear regression model
    model = train_linear_regression_model(data)

    # Make predictions for the next day
    for day in data:
        predicted_temperature = predict_temperature(model, day["temperature"])
        decision = decide_to_bring_umbrella(predicted_temperature)
        print(f"Day: {day['day']}, Predicted Temperature: {predicted_temperature:.2f}°C, Decision: {decision}")

if __name__ == "__main__":
    main()
