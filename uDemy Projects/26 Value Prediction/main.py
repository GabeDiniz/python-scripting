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

  print(X)
  print(y)

make_prediction([1,2], [3,4], 0)