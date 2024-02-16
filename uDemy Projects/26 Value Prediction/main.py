from model import Prediction  # from model.py file

import numpy as np 
import pandas as pd   # pip install pandas
import matplotlib.pyplot as plt   # pip install matplotlib
# pip install scikit-learn
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
  if len(inputs) != len(outputs):
    raise Exception('Lenth of "inputs" and "outputs" must match.')
  
  # Create a dataframe for our data
  df = pd.DataFrame({"inputs": inputs, "outputs": outputs})

  # Reshape the data using Numpy (X: Inputs, y: Outputs) <- ML
  X = np.array(df["inputs"]).reshape(-1, 1)
  y = np.array(df["outputs"]).reshape(-1, 1)

  # Split the date into training data to test our model
  train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=.20)

  # Initialize the model and test it
  model = LinearRegression()
  model.fit(train_X, train_y)
  
  # Prediction
  y_prediction = model.predict([[input_value]])
  y_line = model.predict(X)

  # Testing for accuracy
  y_test_prediction = model.predict(test_X)

  # Plot
  if plot:
    raise NotImplementedError("Plot has not been created!")
  
  return Prediction(value=y_prediction[0][0],
                    r2_score=r2_score(test_y, y_test_prediction),
                    slope=model.coef_[0][0],
                    intercept=model.intercept_[0],
                    mean_absolute_error=mean_absolute_error(test_y, y_test_prediction))


make_prediction([1,2], [3,4], 0)