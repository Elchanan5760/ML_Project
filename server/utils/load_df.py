import pandas as pd

class Util:
    def load_data(self):
        #file_path = os.path.join(os.path.dirname(__file__), 'Data', 'PlayTennis.csv')

        df = pd.read_csv("Data/PlayTennis.csv")
        return df




