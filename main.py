from flask import Flask, request, jsonify
from flask_cors import CORS
from model import MangoPriceModel
import pandas as pd

app = Flask(__name__)
CORS(app)

# Initialize the model
mango_model = MangoPriceModel('data/mango_data.csv')  # Update the path to your CSV file
mango_model.load_data()
mango_model.train()
mango_model.evaluate()  # Print evaluation results in the terminal

def predict(model, new_data):
    """
    Predict the mango prices using the trained model.

    Parameters:
    - model: An instance of MangoPriceModel, which should have been trained.
    - new_data: A DataFrame containing the new data to predict prices for.

    Returns:
    - predictions: A NumPy array of predicted prices.
    """
    new_data_encoded = pd.get_dummies(new_data)
    new_data_encoded = new_data_encoded.reindex(columns=model.X_train.columns, fill_value=0)
    predictions = model.model.predict(new_data_encoded)
    return predictions

@app.route('/predict', methods=['POST'])
def predict_route():
    # Get JSON data from the request
    data = request.json

    # Convert the incoming JSON data to a DataFrame
    new_data = pd.DataFrame([data])

    # Make predictions using the correct model variable
    predictions = predict(mango_model, new_data)

    # Return predictions as JSON
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(debug=True)
