# from utils.load_df import MyUtils
# import pandas as pd
# from calc_naive_bayes.classify_naive import Classify
class Train:
    def __init__(self,df,target):
        self.df = df
        self.target = target
    def create_counter(self):
        print(self.df[self.target])
        values = self.df[self.target].unique()
        # print(values)
        list_instance = []
        for option in values:
            list_instance.append(self.df[(self.df[self.target] == option)])
        data = {}
        for variable in list_instance:
            dict_col = {}
            for col in variable:
                dict_val = dict.fromkeys(self.df[col].unique(),1)
                for val in variable[col]:
                    dict_val[val] += 1
                dict_col[col] = dict_val
            data[variable.head(1)[self.target].iloc[0]] = dict_col
        return data

    def calculate(self):
        dataframe_dict = self.create_counter()
        for i, variable in enumerate(dataframe_dict.keys()):
            print(dataframe_dict)
            for j,col in enumerate(dataframe_dict[variable]):
                for val in dataframe_dict[variable][col].keys():
                    print(self.df[col])
                    if self.target == col:
                        dataframe_dict[variable][col][val] = dataframe_dict[variable][col][val] / (dataframe_dict[variable][col][val] + len(self.df[col].unique()))
                    else:
                        dataframe_dict[variable][col][val] = dataframe_dict[variable][col][val] / (len(self.df) + len(self.df[col].unique()))
        print(dataframe_dict)
        return dataframe_dict
# o1 = pd.read_csv('C:\\Users\HOME\PycharmProjects\\Naive_Bayes\Data\PlayTennis.csv')
#
# a = Train(o1,'PlayTennis')
# da = a.calculate(a.create_counter())
# b = Classify(o1)
# print(b.predict(da,'PlayTennis',{'Outlook': 'Sunny','Temperature': 'Hot','Humidity': 'High','Windy': False}))
