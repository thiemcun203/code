import numpy as np
import pandas as pd

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('/Applications/Python 3.10/code/practise3/class/real_estate.csv', index_col='No')
        self.dataframe = df
    
    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        self.X=self.dataframe.values[:,:-1]
        self.y=self.dataframe.values[:,-1]
    def thiem(self,attributes_list=[0,1,2,3,4,5]):
        return self.X[:,attributes_list]
dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
print('First house\'s age:', dp.X[0][1])
print('House price/unit are:', dp.y[0])
print(dp.thiem(attributes_list=[2,4,5]))