import pandas as pd
from .sanitize import my_sanitize

class Classify:
    def __init__(self,df):
        self.df = df
    def predict(self,dataframe_dict, target, my_values):
        print(my_values)
        my_values = my_sanitize(my_values)
        dict_of_res = {}
        for variable in dataframe_dict.keys():
            res = 1
            print(dataframe_dict)
            for col in dataframe_dict[variable]:
                print(col)
                if col != target:
                    print(my_values[col])
                    res *= dataframe_dict[str(variable)][str(col)][str(my_values[col])]
            dict_of_res[variable] = res
            print(f'{res} * ({(dataframe_dict[variable][target][variable])} / {(len(self.df) + len(dataframe_dict[variable][target]))})')
            dict_of_res[variable] = res * ((dataframe_dict[variable][target][variable]) / (len(self.df) + len(dataframe_dict[variable][target])-1))
        return dict_of_res

