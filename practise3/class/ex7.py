import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataPreprocessing(): #pack all works into a class
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        # df = pd.read_csv('/Applications/Python 3.10/code/practise3/class/real_estate.csv', index_col='No')
        df = pd.read_csv('real_estate.csv', index_col='No')
        
        self.dataframe = df
    
    def set_attributes_and_output(self):
        # Set X and y   to data attributes and output from the dataframe
        self.X=self.dataframe.values[:,:-1]
        self.y=self.dataframe.values[:,-1]
    
    def final_train_test_data(self, attributes_list=[0,1,2,3,4,5], test_size=0.2):
        # Split the data X and output y into training data and testing data
        # Output: a tuple (X_train, X_test, y_train, y_test), using train_test_split with random_state=42
        
        X_train, X_test, y_train, y_test = train_test_split(self.X[:,attributes_list],self.y,test_size=test_size, random_state=42)
        return X_train, X_test, y_train, y_test

dp=DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
