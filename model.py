import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score, explained_variance_score)

class MangoPriceModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestRegressor(random_state=42)  # Initialize the model here
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        mango_data = pd.read_csv(self.data_path)
        mango_data = pd.get_dummies(mango_data)

        new_order = ['Year', 'Price', 'Type_Carabao', 'Type_Indian', 'Type_Pico',
                     'Class_Class A', 'Class_Class B', 'Class_Class C',
                     'Class_Class D', 'Class_Class E',
                     'Month_January', 'Month_February', 'Month_March',
                     'Month_April', 'Month_May', 'Month_June', 'Month_July',
                     'Month_August', 'Month_September', 'Month_October',
                     'Month_November', 'Month_December']
        mango_data = mango_data[new_order]

        X = mango_data.drop(['Price'], axis=1)
        y = mango_data['Price']

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        mae = mean_absolute_error(y_pred, self.y_test)
        mse = mean_squared_error(y_pred, self.y_test)
        r2 = r2_score(y_pred, self.y_test)
        ev = explained_variance_score(y_pred, self.y_test)

        n = len(self.y_test)
        p = self.X_train.shape[1]
        adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

        # Print the metrics
        print(f'Mean Absolute Error (MAE): {mae}')
        print(f'Mean Squared Error (MSE): {mse}')
        print(f'Root Mean Square Error (RMSE): {np.sqrt(mse)}')  # Correct RMSE calculation
        print(f'R-Squared: {r2}')
        print(f'Adjusted R-Squared: {adjusted_r2}')
        print(f'Explained Variance Score: {ev}')
