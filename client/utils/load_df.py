import pandas as pd

class MyUtils:
    def load_data(self,path):
        df = pd.read_csv(path)
        return df