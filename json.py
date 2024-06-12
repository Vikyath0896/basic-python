import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset included within the code
sample_data_json = """
[
{"X": 1, "y": 10},
{"X": 2, "y": 15},
{"X": 3, "y": 20},
{"X": 4, "y": 25},
{"X": 5, "y": 30}
]
"""

# Load sample dataset from JSON string
data = json.loads(sample_data_json)

# Extract features (X) and target variable (y) from the loaded data
X_json = np.array([entry['X'] for entry in data]).reshape(-1, 1)
y_json = np.array([entry['y'] for entry in data])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_json, y_json, test_size=0.2, random_state=42)

# Visualize the dataset
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='red', label='Testing data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Sample Dataset from JSON')
plt.legend()
plt.show()

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)

print(f"Training MSE: {train_mse}")
print(f"Testing MSE: {test_mse}")

# Visualize the linear regression line
X_range = np.linspace(min(X_json), max(X_json), 100).reshape(-1, 1)
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='red', label='Testing data')
plt.plot(X_range, model.predict(X_range), color='green', label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
