#!/usr/bin/env python3

import cgi
import cgitb
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Enable CGI traceback for debugging
cgitb.enable()

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple Logistic Regression model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X, y)

# Function to predict species based on input features
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    try:
        # Convert inputs to float and reshape into a 2D array for prediction
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]], dtype=float)
        prediction = model.predict(input_data)[0]
        predicted_species = iris.target_names[prediction]
        return predicted_species
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    form = cgi.FieldStorage()

    if "sepal_length" in form and "sepal_width" in form and "petal_length" in form and "petal_width" in form:
        try:
            sepal_length = float(form.getvalue("sepal_length"))
            sepal_width = float(form.getvalue("sepal_width"))
            petal_length = float(form.getvalue("petal_length"))
            petal_width = float(form.getvalue("petal_width"))

            predicted_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
            print(f"Content-Type: text/plain")
            print()
            print(f"Predicted Species: {predicted_species}")
        except ValueError:
            print(f"Content-Type: text/plain")
            print()
            print("Error: Input values must be numeric.")
    else:
        print(f"Content-Type: text/plain")
        print()
        print("Error: Required parameters missing.")

if __name__ == "__main__":
    main()
